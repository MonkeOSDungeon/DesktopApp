import cv2

class Camera:
    def __init__(self, id: int, camera_ip_and_port: str, name: str, fps: int, resolution: tuple[int] = (1280, 720)) -> None:
        self.name = name
        self.ip = camera_ip_and_port
        self.id = id
        if type(self.ip) == int:
            self.cap = cv2.VideoCapture(camera_ip_and_port)
        else:
            self.cap = cv2.VideoCapture(camera_ip_and_port, cv2.CAP_FFMPEG)
        self.camera_fps = fps
        self.resolution = resolution

    def connect_to_camera(self):
        if type(self.ip) == int:
            self.cap = cv2.VideoCapture(self.ip)
        else:
            self.cap = cv2.VideoCapture(self.ip, cv2.CAP_FFMPEG)
        

    def read(self):
        while not self.cap.isOpened():
            self.connect_to_camera()
        _, frame = self.cap.read()
        return cv2.resize(frame, self.resolution)