from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, QThread, Signal, Slot, Qt
from ui_main_window import Ui_MainWindow
from ui_change_zone import Ui_Zone_changing
from personDetector import Detector
from email_server import Email_server
import numpy as np
import sys
import cv2
import time
import supervision as sv



class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    def __init__(self, detector: Detector, cap, is_active_detector: bool, activate_detector_every_n_frames: int):
        super().__init__()
        # person detector based on YOLOv5 nano
        self.detector = detector
        # cv2 video capture
        self.cap = cap
        # is it necessary to detect on the current frame or not
        self.is_active_detector = is_active_detector
        # is used to speed up performance, responsible for how many frames will be skipped between detections
        self.activate_detector_every_n_frames = activate_detector_every_n_frames

        # email info. wiil be changed when user input this data in settings
        self.reciever_email = None
        self.sender_server = None
        
        # annotators that are used in skipped frames
        self.box_annotator = None
        self.detections = None
        self.zone_annotator = None

    def set_email_settings(self, sender: Email_server, reciever_email: str) -> None:
        '''
        save emails to follow up alert sending
        '''
        self.sender_server = sender
        self.reciever_to_alert = reciever_email

    def set_active_detector(self, is_active: bool) -> None:
        '''
        Set is_active_detector to is_active value
        '''
        self.is_active_detector = is_active


    def run(self):
        last_send = 0
        frame_num = 0
        while True:
            _, frame = self.cap.read()
            frame = cv2.resize(frame, (1280, 720))

            frame_num += 1

            if self.is_active_detector and frame_num == self.activate_detector_every_n_frames:
                # detect every self.activate_detector_every_n_frames (default 5) frames for performance boost
                frame_num = 0
                was_human_detected_in_zone, frame, self.box_annotator, self.zone_annotator, self.detections = self.detector.detect(frame)
                self.save()
                #if was_human_detected_in_zone and self.sender_server and self.reciever:
                    #curr_time = time.time()
                    #if curr_time - last_send > 60 * 5 and ...
                    #self.sender.send_email(self.reciever_to_alert, frame)
                    #add sending email and push notification to mobile app
            elif self.is_active_detector and self.zone_annotator and self.box_annotator:
                # skip detection phase for performance boost

                # annotate from previous detection annotators
                frame = self.box_annotator.annotate(scene=frame, detections=self.detections)
                frame = self.zone_annotator.annotate(scene=frame)

                # save frame to video file
                self.save(frame)
            else:
                self.realise()
                frame_num = self.activate_detector_every_n_frames - 1
            self.change_pixmap_signal.emit(frame)


class HumanDetectorDesktopApp(QMainWindow):
    def __init__(self, video_stream_path: str = 0) -> None:
        '''
        args: 
                video_stream_path: path to video stream, default = 0 (video stream from web camera)
        '''
        super(HumanDetectorDesktopApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.detector = Detector(resolution=(1280, 720), zone=np.array([1000, 0, 500, 0, 500, 720, 1000, 720], dtype=int).reshape((4, 2)))
        # activate people detection every n frames, if 1 - always active 
        self.activate_detector_every_n_frames = 5

        #self.cap = cv2.VideoCapture(video_stream_path)
        #self.cap = cv2.VideoCapture('udp://192.168.126.228:40002', cv2.CAP_FFMPEG)
        self.cap = cv2.VideoCapture('http://192.168.0.183:4747/video', cv2.CAP_FFMPEG)

        # Waiting for video stream reception
        while not self.cap.isOpened():
            #self.cap = cv2.VideoCapture('udp://192.168.126.228:40002', cv2.CAP_FFMPEG)
            self.cap = cv2.VideoCapture('http://192.168.0.183:4747/video', cv2.CAP_FFMPEG)
            print("Ожидание получения видеопотока...")

        print("Видеопоток получен!")
        self.email_server = None
        self.reciever_email = None

        self.ui.settings.triggered.connect(self.open_settings_window)

        self.video_stream = self.ui.video_stream
        self.is_active_detector = False
        
        self.ui.activate_people_detector.clicked.connect(self.activate_detector_button_clicked)

        self.thread = VideoThread(self.detector, self.cap, self.is_active_detector, self.activate_detector_every_n_frames)
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    # connected to click on settings
    def open_settings_window(self):
        '''
        Create new window where you can 
            change zone, 
            resolution, 
            sender and reciever emails 
        and some more things will be added)
        '''
        self.new_window = QtWidgets.QDialog()
        self.ui_settings_window = Ui_Zone_changing()
        self.ui_settings_window.setupUi(self.new_window)
        self.ui_settings_window.btn_save_zone.clicked.connect(self.save_new_cords)

        self.ui_settings_window.btn_save_resolution.clicked.connect(self.save_new_resolution)
        self.ui_settings_window.btn_save_reciever.clicked.connect(self.save_reciever)
        self.ui_settings_window.btn_save_sender.clicked.connect(self.save_sender)

        self.new_window.show()
    
    # connected to click on button btn_save_reciever
    def save_reciever(self):
        '''
        initialize email server and set it in video thread if sender server already initialized
        '''
        self.reciever_email = self.ui_settings_window.le_reciever_email.text()
        if self.email_server:
            self.thread.set_email_settings(self.email_server, self.reciever_email)

    # connected to click on button btn_save_sender
    def save_sender(self):
        '''
        initialize email server and set it in video thread if reciever email already initialized
        '''
        self.email_server = Email_server(
            self.ui_settings_window.le_sender_email.text(),
            self.ui_settings_window.le_sender_pass.text()
        )
        if self.reciever_email:
            self.thread.set_email_settings(self.email_server, self.reciever_email)

    # connected to click on button btn_save_resolution
    def save_new_resolution(self):
        '''
        change video thread resolution
        '''
        self.resolution = map(int, self.ui_settings_window.le_resolution.text().split())

    # connected to click on button btn_save_zone
    def save_new_cords(self):
        '''
        change protected area 
        '''
        cords = list(map(int, self.ui_settings_window.le_right_top_cords.text().split()))
        cords.extend(list(map(int, self.ui_settings_window.le_left_top_cords.text().split())))
        cords.extend(list(map(int, self.ui_settings_window.le_left_bottom_cords.text().split())))
        cords.extend(list(map(int, self.ui_settings_window.le_right_bottom_cords.text().split())))
        self.detector.change_zone(np.array(cords, dtype=int).reshape((4, 2)))

    # connected to click on button activate_people_detector
    def activate_detector_button_clicked(self):
        '''
        change text on activate_people_detector button,
        change is_active_detector in thread (video stream)
        '''
        if self.is_active_detector:
            self.is_active_detector = False
            self.ui.activate_people_detector.setText('Включить\nраспознавание людей\nна видео')
        else:
            self.is_active_detector = True
            self.ui.activate_people_detector.setText('Выключить\nраспознавание людей\nна видео')

        self.thread.set_active_detector(self.is_active_detector)

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.video_stream.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        '''
        convert image from cv2 format to qt format
        '''
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(1280, 720, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HumanDetectorDesktopApp(0)

    

    window.show()

    sys.exit(app.exec())