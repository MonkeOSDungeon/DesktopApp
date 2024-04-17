from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, QThread, Signal, Slot, Qt
from ui_main_window import Ui_MainWindow
from ui_change_zone import Ui_Zone_changing
from personDetector import Detector
import numpy as np
import sys
import cv2


class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)

    def __init__(self, detector: Detector, cap, is_active_detector: bool):
        super().__init__()
        self.detector = detector
        self.cap = cap
        self.is_active_detector = is_active_detector

    def set_active_detector(self, is_active: bool) -> None:
        '''
        Set is_active_detector to is_active value
        '''
        self.is_active_detector = is_active


    def run(self):
        while True:
            _, frame = self.cap.read()
            if not self.is_active_detector:
                frame = cv2.resize(frame, (1280, 720))
            else:
                was_human_detected_in_zone, frame = self.detector.detect(frame)
                if was_human_detected_in_zone:
                    pass #add sending email and push to mobile app
            #print(self.is_active_detector)
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
        self.cap = cv2.VideoCapture(video_stream_path)
        
        self.ui.menu_change_zone.triggered.connect(self.open_zone_changing_window)

        

        self.video_stream = self.ui.video_stream
        self.is_active_detector = True
        
        self.ui.activate_people_detector.clicked.connect(self.activate_detector_button_clicked)
        
        self.thread = VideoThread(self.detector, self.cap, self.is_active_detector)
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    def open_zone_changing_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_zone_window = Ui_Zone_changing()
        self.ui_zone_window.setupUi(self.new_window)
        self.ui_zone_window.btn_save_zone.clicked.connect(self.save_new_cords)
        self.new_window.show()

    def save_new_cords(self):
        cords = list(map(int, self.ui_zone_window.le_right_top_cords.text().split()))
        cords.extend(list(map(int, self.ui_zone_window.le_left_top_cords.text().split())))
        cords.extend(list(map(int, self.ui_zone_window.le_left_bottom_cords.text().split())))
        cords.extend(list(map(int, self.ui_zone_window.le_right_bottom_cords.text().split())))
        self.detector.change_zone(np.array(cords, dtype=int).reshape((4, 2)))

    def activate_detector_button_clicked(self):
        if self.is_active_detector:
            self.is_active_detector = False
            self.ui.activate_people_detector.setText('Выключить\nраспознавание людей\nна видео')
        else:
            self.is_active_detector = True
            self.ui.activate_people_detector.setText('Включить\nраспознавание людей\nна видео')

        self.thread.set_active_detector(self.is_active_detector)

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.video_stream.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
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