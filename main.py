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
from zone_redactor import ZoneRedactorWindow
from out_of_date_video_cleaner import Cleaner
from personDetector import Detector
from email_server import Email_server
from camera import Camera
from connection import Data
import numpy as np
import socket
import struct
import sys
import cv2
import time



class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    def __init__(self, detector: Detector, is_active_detector: bool, 
                 activate_detector_every_n_frames: int, video_path: str = 'data/videos/', server_ip: str = '192.168.18.228', server_port: int = 8000):
        super().__init__()
        # socket for sending video to the client
        self.server_ip = server_ip
        self.server_port1 = server_port
        self.server_port2 = server_port + 1
        self.client_socket1 = None
        self.client_socket2 = None
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
        self.annotators = None

        self.start_detection_time = None
        self.end_detection_time = None
        self.video_writer = None

    def set_cameras(self, cameras: list[Camera]):
        self.cameras = cameras

    def set_zones(self, zones):
        self.zones = zones

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

    def send_frame(self, frame, client_socket: socket.socket):
        _, buffer = cv2.imencode('.jpg', frame)
        data = buffer.tobytes()
        size = len(data)
        try:
            client_socket.sendall(struct.pack(">L", size) + data)
        except (BrokenPipeError, ConnectionResetError):
            client_socket.close()
            self.client_connected = False
            print("Client disconnected")
            raise BrokenPipeError

    def stop(self):
        self.running = False

    def bind_server(self, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.server_ip, port))
        server_socket.listen(1)
        return server_socket

    def run(self):
        server_socket1 = self.bind_server(self.server_port1)
        server_socket2 = self.bind_server(self.server_port2)
        
        print(f"Listening for connection on {self.server_ip}:{self.server_port1}")
        print(f"Listening for connection on {self.server_ip}:{self.server_port2}")

        last_send = 0
        frame_num = 0
        NOTIFICATION_FREQ = 300
        self.running = True
        while self.running:
            if not isinstance(self.camera, Camera) or not self.camera.cap.isOpened():
                continue
            try:
                self.client_socket1, _ = server_socket1.accept()
                self.client_socket2, _ = server_socket2.accept()
                self.client_connected = True
                print("Client connected")
            except socket.timeout:
                pass
            
            while self.client_connected and self.camera is not None and self.camera.cap.isOpened():
                main_frame = self.camera.read()
                was_human_detected_in_zone = []
                oth_frames = []
                oth_box_annotators = []
                oth_annotators = []
                oth_detections = []
                for camera in self.cameras:
                    if camera is not self.camera:
                        oth_frames.append(camera.read()) 
                frame_num += 1

                if self.is_active_detector and frame_num == self.activate_detector_every_n_frames:
                    # detect every self.activate_detector_every_n_frames (default 5) frames for performance boost
                    frame_num = 0
                    self.detector.change_zone(self.zones[self.camera.id])
                    was_detected_in_zone, main_frame, self.box_annotator, self.annotators, self.detections = self.detector.detect(main_frame)
                    was_human_detected_in_zone.append(was_detected_in_zone)
                    for i,frame in enumerate(oth_frames):
                        if camera is not self.camera and self.zones[self.cameras[i].id]:
                            self.detector.change_zone(self.zones[self.cameras[i].id])
                            was_detected_in_zone, frame, temp_box_annotator, temp_annotators, temp_detections = self.detector.detect(frame)
                            was_human_detected_in_zone.append(was_detected_in_zone)
                            oth_box_annotators.append(temp_box_annotator)
                            oth_annotators.append(temp_annotators)
                            oth_detections.append(temp_detections)
                    if self.video_writer is None:
                        self.start_detection_time = time.strftime('%d.%m.%Y_%H-%M-%S', time.localtime())
                        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
                        output_filename = f'{self.video_path}{self.start_detection_time}.avi'
                        self.video_writer = cv2.VideoWriter(output_filename, fourcc, 30.0, (1280, 720))
                    self.save(main_frame)
                    
                    if any(was_human_detected_in_zone) and self.sender_server and self.reciever_to_alert and time.time() - last_send > NOTIFICATION_FREQ:
                        self.sender_server.send_email(self.reciever_to_alert, main_frame)
                        last_send = time.time()
                elif self.is_active_detector and self.annotators and self.annotators[0] and self.box_annotator:
                    # skip detection phase for performance boost

                    # annotate from previous detection annotators
                    main_frame = self.box_annotator.annotate(scene=main_frame, detections=self.detections)
                    for annotator in self.annotators:
                        main_frame = annotator.annotate(scene=main_frame)
                    for i,frame in enumerate(oth_frames):
                        if camera is not self.camera and self.zones[self.cameras[i].id]:
                            self.detector.change_zone(self.zones[self.cameras[i].id])
                            was_detected_in_zone, frame, temp_box_annotator, temp_annotators, temp_detections = self.detector.detect(frame)
                            was_human_detected_in_zone.append(was_detected_in_zone)
                            oth_box_annotators.append(temp_box_annotator)
                            oth_annotators.append(temp_annotators)
                            oth_detections.append(temp_detections)
                    self.detector.change_zone(self.zones[self.camera.id])

                    # save frame to video file
                    self.save(main_frame)
                else:
                    # realise file
                    if not self.video_writer is None:
                        self.realise()
                    else:
                        self.video_writer = None
                    frame_num = self.activate_detector_every_n_frames - 1
                self.change_pixmap_signal.emit(main_frame)
                frame1 = oth_frames[0]
                if oth_box_annotators and oth_box_annotators[0] and oth_annotators and oth_annotators[0]:
                    frame1 = oth_box_annotators[0].annotate(scene=frame1, detections=oth_detections[0])
                    for annotator in oth_annotators[0]:
                        frame1 = annotator.annotate(scene=frame1)

                if self.client_connected:
                    try:
                        self.send_frame(main_frame, self.client_socket1)    
                        self.send_frame(frame1, self.client_socket2)
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

        # path to store videos
        self.video_path = 'data/videos/'
        Cleaner(48).clean_directory(self.video_path)
        
        self.data = Data()
        self.data.create_tables()

        # TODO : подгрузка зон с БД
        # в детектор теперь идет массив зон типа [[x,y,x,y...],[x,y,x,y...]...] без решейпа
        self.zones = self.data.get_zones()
        self.detector = Detector(resolution=(1280, 720), polygons_arr=[[0,0,0,0,0,0,0,0]])
        # activate people detection every n frames, if 1 - always active 
        self.activate_detector_every_n_frames = 7

        self.cameras = self.data.get_cameras()
        #self.cameras = [Camera(first_camera_path, 30, (1280, 720))]
        if len(self.cameras) == 0:
            self.cameras.append(Camera(0, 'webcam 1', 30, (1280, 720)))
        for i in range(len(self.cameras)):
            self.ui.cb_current_camera.addItem(self.cameras[i].name)
        
        self.ui.cb_current_camera.currentIndexChanged.connect(self.cb_index_changed)

        self.email_server = None
        self.reciever_email = None

        self.ui.settings.triggered.connect(self.open_settings_window)
        self.ui.cameras_settings.triggered.connect(self.open_cameras_list_window)
        self.ui.zone_settings.triggered.connect(self.open_zone_redactor) 

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
        self.detector.change_zone(self.data.get_zones_by_camera_id(self.cameras[index].id))
        self.current_camera = self.cameras[index]
        self.thread.set_camera(self.current_camera)
        self.thread.set_cameras(self.cameras)
        self.thread.set_zones(self.zones)


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
            """index  = self.ui_cameras_list_window.tbl_cameras.selectedIndexes()[0]
            id = str(self.ui_cameras_list_window.tbl_cameras.model().data(index))
            camera_data = self.data.get_camera(id)
            self.ui_add_edit_camera.le_ip.setText(str(camera_data.ip))
            self.ui_add_edit_camera.le_fps.setText(str(camera_data.camera_fps))
            self.ui_add_edit_camera.le_name.setText(str(camera_data.name))
            self.ui_add_edit_camera.le_resolution.setText(' '.join(map(str, camera_data.resolution)))"""
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
        self.ui_settings_window.btn_save_zone.clicked.connect(self.save_new_cords)

        self.ui_settings_window.btn_save_reciever.clicked.connect(self.save_reciever)
        self.ui_settings_window.btn_save_sender.clicked.connect(self.save_sender)

        self.settings_window.show()

    def open_zone_redactor(self):
        # добавить готовые зоны из бд если есть и сунуть их туда же их в конструктор
        list_of_polygons = self.data.get_zones_by_camera_id(self.current_camera.id)
        last_frame = self.current_camera.read()
        self.zone_redactor_window = ZoneRedactorWindow(last_frame, list_of_polygons)
        self.zone_redactor_window.data_saved.connect(self.update_zone_list)
        self.zone_redactor_window.show()

    @Slot(list)
    def update_zone_list(self):
        self.list_of_zones = self.zone_redactor_window.detector_coords
        self.data.delete_zone_by_camera_id(self.current_camera.id)
        for zone in self.list_of_zones:
            zone = ' '.join(map(str, zone))
            self.data.add_zone_exec(self.current_camera.id, zone)
        self.detector.change_zone(np.array(self.list_of_zones))
        self.zones[self.current_camera.id] = self.list_of_zones
        self.thread.set_zones(self.zones)
        

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
    
    def update_video_path(self):
        self.video_path = self.ui_settings_window.le_video_path.text()

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
        print(self.ui_settings_window.le_sender_pass.text(), '\n\n')
        self.email_server = Email_server(
            self.ui_settings_window.le_sender_email.text(),
            'phfm ysxx evul awtr'
            #self.ui_settings_window.le_sender_pass.text()
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