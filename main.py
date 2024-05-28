from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, QThread, Signal, Slot, Qt
from PySide6.QtSql import QSqlTableModel
from UIFiles.ui_main_window import Ui_MainWindow
from UIFiles.ui_change_email import Ui_EmailPathChanging
from UIFiles.ui_add_edit_camera import Ui_AddEditCamera
from UIFiles.ui_cameras_list import Ui_CamerasWindow
from personDetector import Detector
from email_server import Email_server
from camera import Camera
from connection import Data
import socket
import struct
import numpy as np
import sys
import cv2
import time
import supervision as sv



class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    def __init__(self, detector: Detector, is_active_detector: bool, 
                 activate_detector_every_n_frames: int, video_path: str = 'data/videos/', server_ip: str = '192.168.18.228', server_port: int = 8000):
        super().__init__()
        
        # socket for sending video to the client
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = None
        self.client_connected = False

        # path to store videos
        self.video_path = video_path

        # person detector based on YOLOv5 nano
        self.detector = detector
        # cv2 video capture
        self.camera = None
        # is it necessary to detect on the current frame or not
        self.is_active_detector = is_active_detector
        # is used to speed up performance, responsible for how many frames will be skipped between detections
        self.activate_detector_every_n_frames = activate_detector_every_n_frames

        
        # email info. wiil be changed when user input this data in settings
        self.reciever_to_alert = None
        self.sender_server = None
        
        # annotators that are used in skipped frames
        self.box_annotator = None
        self.detections = None
        self.zone_annotator = None

        self.start_detection_time = None
        self.end_detection_time = None
        self.video_writer = None

    def set_camera(self, camera: Camera):
        self.camera = camera

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

    def set_video_path(self, path):
        self.video_path = path

    def save(self, frame: np.ndarray) -> None:
        '''
        add frame to video. 
        File name is created based on the start_detection_time and end_detection_time
        args:
            frame: cv2 video capture frame
        '''
        self.video_writer.write(frame)

    def realise(self) -> None:
        '''
        end of detection, save file to file_path
        '''
        self.video_writer.release()
        #cv2.destroyAllWindows()

    def send_frame(self, frame):
        _, buffer = cv2.imencode('.jpg', frame)
        data = buffer.tobytes()
        size = len(data)
        try:
            self.client_socket.sendall(struct.pack(">L", size) + data)
        except (BrokenPipeError, ConnectionResetError):
            self.client_socket.close()
            self.client_connected = False
            print("Client disconnected")
            raise BrokenPipeError

    def stop(self):
        self.running = False

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.server_ip, self.server_port))
        server_socket.listen(1)
        
        print(f"Listening for connection on {self.server_ip}:{self.server_port}")

        last_send = 0
        frame_num = 0
        NOTIFICATION_FREQ = 300
        self.running = True
        while self.running:
            if not isinstance(self.camera, Camera) or not self.camera.cap.isOpened():
                continue
            try:
                self.client_socket, _ = server_socket.accept()
                self.client_connected = True
                print("Client connected")
            except socket.timeout:
                pass
            
            while self.client_connected and self.camera is not None and self.camera.cap.isOpened():
                frame = self.camera.read()

                frame_num += 1

                if self.is_active_detector and frame_num == self.activate_detector_every_n_frames:
                    # detect every self.activate_detector_every_n_frames (default 5) frames for performance boost
                    frame_num = 0
                    was_human_detected_in_zone, frame, self.box_annotator, self.zone_annotator, self.detections = self.detector.detect(frame)
                    if self.video_writer is None:
                        self.start_detection_time = time.strftime('%d.%m.%Y_%H-%M-%S', time.localtime())
                        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
                        output_filename = f'{self.video_path}{self.start_detection_time}.avi'
                        self.video_writer = cv2.VideoWriter(output_filename, fourcc, 30.0, (1280, 720))
                    self.save(frame)
                    
                    if was_human_detected_in_zone and self.sender_server and self.reciever and time.time() - last_send > NOTIFICATION_FREQ:
                        self.sender.send_email(self.reciever_to_alert, frame)
                        last_send = time.time()
                elif self.is_active_detector and self.zone_annotator and self.box_annotator:
                    # skip detection phase for performance boost

                    # annotate from previous detection annotators
                    frame = self.box_annotator.annotate(scene=frame, detections=self.detections)
                    frame = self.zone_annotator.annotate(scene=frame)

                    # save frame to video file
                    self.save(frame)
                else:
                    # realise file
                    if not self.video_writer is None:
                        self.realise()
                    else:
                        self.video_writer = None
                    frame_num = self.activate_detector_every_n_frames - 1
                self.change_pixmap_signal.emit(frame)

                if self.client_connected:
                    try:
                        self.send_frame(frame)
                    except (BrokenPipeError, ConnectionResetError):
                        break
                    

            if isinstance(self.camera, Camera) and not self.camera.cap.isOpened():
                self.camera.connect_to_camera()
        

class HumanDetectorDesktopApp(QMainWindow):
    def __init__(self, first_camera_path: str = 0) -> None:
        '''
        args: 
                video_stream_path: path to video stream, default = 0 (video stream from web camera)
        '''
        super(HumanDetectorDesktopApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = Data()
        self.data.create_tables()

        # TODO : подгрузка зон с БД
        self.detector = Detector(resolution=(1280, 720), zone=np.array([1000, 0, 500, 0, 500, 720, 1000, 720], dtype=int).reshape((4, 2)))
        # activate people detection every n frames, if 1 - always active 
        self.activate_detector_every_n_frames = 5

        self.cameras = self.data.get_cameras()
        #self.cameras = [Camera(first_camera_path, 30, (1280, 720))]
        if len(self.cameras) == 0:
            self.cameras.append(Camera(0, 'webcam 1', 30, (1280, 720)))
        for i in range(len(self.cameras)):
            self.ui.cb_current_camera.addItem(self.cameras[i].name)
        
        self.ui.cb_current_camera.currentIndexChanged.connect(self.cb_index_changed)

        self.email_server = None
        self.reciever_email = None
        # path to store videos
        self.video_path = 'data/videos/'

        self.ui.settings.triggered.connect(self.open_settings_window)
        self.ui.cameras_settings.triggered.connect(self.open_cameras_list_window)

        self.video_stream = self.ui.video_stream
        self.is_active_detector = False
        
        self.ui.activate_people_detector.clicked.connect(self.activate_detector_button_clicked)

        self.thread = VideoThread(self.detector, self.is_active_detector, self.activate_detector_every_n_frames)
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    def cb_update(self):
        self.ui.cb_current_camera.clear()
        for i in range(len(self.cameras)):
            self.ui.cb_current_camera.addItem(self.cameras[i].name)

    def cb_index_changed(self, index):
        self.thread.set_camera(self.cameras[index])

    def add_new_camera(self):
        ip = self.ui_add_edit_camera.le_ip.text()
        fps = int(self.ui_add_edit_camera.le_fps.text())
        resolution = self.ui_add_edit_camera.le_resolution.text()
        name = self.ui_add_edit_camera.le_name.text()

        if name == '':
            name = None

        # Somehow this methods does not work
        #self.data.add_camera(ip, fps, resolution, name)
        #self.data.add_cam_list(ip, fps, resolution, name)
        self.data.add_cam_exec(ip, fps, resolution, name)
        self.cameras = self.data.get_cameras()
        self.cb_update()
        self.view_data()
        self.add_edit_camera_window.close()

    def edit_curr_camera(self):
        index  = self.ui_cameras_list_window.tbl_cameras.selectedIndexes()[0]
        id = str(self.ui_cameras_list_window.tbl_cameras.model().data(index))

        ip = self.ui_add_edit_camera.le_ip.text()
        fps = int(self.ui_add_edit_camera.le_fps.text())
        resolution = self.ui_add_edit_camera.le_resolution.text()
        name = self.ui_add_edit_camera.le_name.text()

        if name == '':
            name = None

        self.data.update_camera(id, ip, fps, resolution, name)
        self.cameras = self.data.get_cameras()
        self.cb_update()

        self.view_data()
        self.add_edit_camera_window.close()

    def delete_curr_camera(self):
        index  = self.ui_cameras_list_window.tbl_cameras.selectedIndexes()[0]
        id = str(self.ui_cameras_list_window.tbl_cameras.model().data(index))

        self.data.delete_camera(id)
        self.view_data()

    def open_add_edit_camera_window(self):
        self.add_edit_camera_window = QtWidgets.QDialog()
        self.ui_add_edit_camera = Ui_AddEditCamera()
        self.ui_add_edit_camera.setupUi(self.add_edit_camera_window)

        sender = self.sender()
        if sender.text() == 'Добавить камеру':
            self.ui_add_edit_camera.btn_save_camera.clicked.connect(self.add_new_camera)
        else:
            index  = self.ui_cameras_list_window.tbl_cameras.selectedIndexes()[0]
            id = str(self.ui_cameras_list_window.tbl_cameras.model().data(index))
            camera_data = self.data.get_camera(id)
            self.ui_add_edit_camera.le_ip.setText(str(camera_data.ip))
            self.ui_add_edit_camera.le_fps.setText(str(camera_data.camera_fps))
            self.ui_add_edit_camera.le_name.setText(camera_data.name)
            self.ui_add_edit_camera.le_resolution.setText(' '.join(map(str, camera_data.resolution)))
            self.ui_add_edit_camera.btn_save_camera.clicked.connect(self.edit_curr_camera)

        self.add_edit_camera_window.show()

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('cameras')
        self.model.select()
        self.ui_cameras_list_window.tbl_cameras.setModel(self.model)

    def open_cameras_list_window(self):
        self.cameras_list_window = QtWidgets.QDialog()
        self.ui_cameras_list_window = Ui_CamerasWindow()
        self.ui_cameras_list_window.setupUi(self.cameras_list_window)
        self.ui_cameras_list_window.tbl_cameras.resizeColumnsToContents()

        self.ui_cameras_list_window.btn_add_camera.clicked.connect(self.open_add_edit_camera_window)
        self.ui_cameras_list_window.btn_edit_camera.clicked.connect(self.open_add_edit_camera_window)
        self.ui_cameras_list_window.btn_delete_camera.clicked.connect(self.delete_curr_camera)

        self.view_data()

        self.cameras_list_window.show()

    def update_video_path(self):
        self.video_path = self.ui_settings_window.le_video_path.text()

    # connected to click on settings
    def open_settings_window(self):
        '''
        Create new window where you can 
            change zone, 
            sender and reciever emails 
        and some more things will be added)
        '''
        self.settings_window = QtWidgets.QDialog()
        self.ui_settings_window = Ui_EmailPathChanging()
        self.ui_settings_window.setupUi(self.settings_window)
        self.ui_settings_window.btn_save_video_path.clicked.connect(self.update_video_path)

        self.ui_settings_window.btn_save_reciever.clicked.connect(self.save_reciever)
        self.ui_settings_window.btn_save_sender.clicked.connect(self.save_sender)

        self.settings_window.show()
    
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