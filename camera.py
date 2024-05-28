import cv2

class Camera:
    def __init__(self, camera_ip_and_port: str, fps: int, resolution: tuple[int] = (1280, 720)) -> None:
        self.ip = camera_ip_and_port
        if type(camera_ip_and_port) == int:
            self.cap = cv2.VideoCapture(camera_ip_and_port)
        else:
            self.cap = cv2.VideoCapture(camera_ip_and_port, cv2.CAP_FFMPEG)
        self.camera_fps = fps
        self.resolution = resolution

    def connect_to_camera(self):
        # Waiting for video stream reception
        while not self.cap.isOpened():
            self.cap = cv2.VideoCapture(self.ip, cv2.CAP_FFMPEG)
            print("Ожидание получения видеопотока...")

        print("Видеопоток получен!")

    def read(self):
        _, frame = self.cap.read()
        return cv2.resize(frame, self.resolution)