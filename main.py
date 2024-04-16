from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, QThread, Signal, Slot, Qt
from ui_main_window import Ui_MainWindow
from personDetector import Detector
import numpy as np
import sys
import cv2


class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)

    def __init__(self, detector: Detector, cap):
        super().__init__()
        self.detector = detector
        self.cap = cap

    def run(self):
        while True:
            _, frame = self.cap.read()
            _, frame = self.detector.detect(frame)
            self.change_pixmap_signal.emit(frame)

class HumanDetectorDesktopApp(QMainWindow):
    def __init__(self, video_path: str = 0) -> None:
        '''
        args:
                video_path: path to video, default = 0 (video stream from web camera)
        '''
        super(HumanDetectorDesktopApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.detector = Detector(resolution=(1280, 720), zone=np.array([1000, 0, 500, 0, 500, 720, 1000, 720], dtype=int).reshape((4, 2)))
        self.cap = cv2.VideoCapture(video_path)
        
        self.video_stream = self.ui.video_stream
        self.thread = VideoThread(self.detector, self.cap)
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

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