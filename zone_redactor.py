import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QDialog, QGraphicsScene, QGraphicsPolygonItem, QGraphicsEllipseItem, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QPen, QColor, QMouseEvent, QImage, QPolygonF
from PySide6.QtCore import Qt, QRectF, QPoint, QPointF, Signal
from UIFiles.ui_zone_redactor import Ui_ZoneRedactor


class PolygonZone(QGraphicsPolygonItem):
    dragging_point_index = None
    point_size = 10
    grab_radius = 20 
    def __init__(self,bounding_rect, last_changed, zone_arr, arr_from_db:list, parent=None):
        super().__init__(parent)
        self.bounding_rect = bounding_rect
        self.last_changed = last_changed
        self.zone_arr = zone_arr
        if not len(arr_from_db):
            self.polygon_points = [
                QPointF(50, 50),
                QPointF(200, 50),
                QPointF(200, 150),
                QPointF(50, 150)
            ]
        else:
            self.polygon_points = [QPointF(arr_from_db[i], arr_from_db[i + 1]) for i in range(0, len(arr_from_db), 2)]
        
        self.setPolygon(QPolygonF(self.polygon_points))
        self.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        
        # corner circles for each vertex of the polygon
        self.corner_circles = []
        if len(self.zone_arr)>0:
            for circle in self.zone_arr[self.last_changed[0]].corner_circles:
                circle.setBrush(QColor(Qt.red))
        for point in self.polygon_points:
            circle = QGraphicsEllipseItem(-self.point_size/2, -self.point_size/2, self.point_size, self.point_size, self)
            circle.setBrush(QColor(Qt.green))
            circle.setPos(point)
            self.corner_circles.append(circle)
     
        
    def mousePressEvent(self, event):
        if self.last_changed[0]!=None:
            for circle in self.zone_arr[self.last_changed[0]].corner_circles:
                circle.setBrush(QColor(Qt.red))
        # Change color of corner circles to green
        for circle in self.corner_circles:
            circle.setBrush(QColor(Qt.green))
        
        # Update last_changed with the index of this polygon in the zone array
        if self in self.zone_arr:
            self.last_changed[0] = self.zone_arr.index(self)
        
        pos = event.pos()
        for i, point in enumerate(self.polygon_points):
            if (point - pos).manhattanLength() < self.grab_radius:
                self.dragging_point_index = i
                break
            
        event.accept()

    def mouseMoveEvent(self, event):
        if self.dragging_point_index is not None:
            pos = event.pos() # gets the current position of the mouse cursor
            scene_pos = self.mapToScene(pos) # converts the position to the coordinate system of the QGraphicsScene
            # the point must be within the zone boundary
            scene_pos.setX(max(self.bounding_rect.left(), min(self.bounding_rect.right(), scene_pos.x())))
            scene_pos.setY(max(self.bounding_rect.top(), min(self.bounding_rect.bottom(), scene_pos.y())))

            self.polygon_points[self.dragging_point_index] = scene_pos
            self.setPolygon(QPolygonF(self.polygon_points))
            self.update_corner_circles()

        event.accept()

    def mouseReleaseEvent(self, event):
        self.dragging_point_index = None
        event.accept()
        
    def delete_point(self):
        self.polygon_points.pop()
        self.corner_circles.pop()
        self.setPolygon(QPolygonF(self.polygon_points))

    def add_point(self, point: QPointF):
        self.polygon_points.append(point)
        self.setPolygon(QPolygonF(self.polygon_points))
        self.update_corner_circles()

    def get_polygon_coordinates(self):
        return [(point.x(), point.y()) for point in self.polygon_points]

    def update_corner_circles(self):
        for i, point in enumerate(self.polygon_points):
            if i>=len(self.corner_circles):
                circle = QGraphicsEllipseItem(-self.point_size/2, -self.point_size/2, self.point_size, self.point_size, self)
                circle.setBrush(QColor(Qt.green))
                circle.setPos(point)
                self.corner_circles.append(circle)
            else:
                self.corner_circles[i].setPos(point)
            


class ZoneRedactorWindow(QDialog):
    data_saved = Signal(list)
    def __init__(self, frame, list_of_polygons):
        super().__init__()
        self.ui = Ui_ZoneRedactor()
        self.ui.setupUi(self)
        self.list_from_db = list_of_polygons
        # - это если будет загрузка зон с бд
        self.zone_arr = []
        self.last_changed = [None]
        # image from cv2 
        image = frame
        height, width, ch = image.shape
        cv_image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        bytes_per_line = ch * width
        q_image = QImage(cv_image_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)
        self.image_item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.image_item)
        # area where zone can move
        self.bounding_rect = QRectF(0, 0, width, height)
        if len(self.list_from_db)>0:
            for zone in self.list_from_db:
                polygon_zone = PolygonZone(self.bounding_rect, self.last_changed, self.zone_arr, arr_from_db=zone)
                self.scene.addItem(polygon_zone)
                polygon_zone.setZValue(1)
                self.zone_arr.append(polygon_zone)
                self.last_changed[0] = len(self.zone_arr)-1
            self.list_from_db = []
        # buttons 
        # примеры использования, подвязать к кнопкам
        self.ui.addButton.clicked.connect(self.add_polygon_point)
        self.ui.deleteButton.clicked.connect(self.delete_polygon_point)
        self.ui.addZoneButton.clicked.connect(self.add_zone)
        self.ui.saveZone.clicked.connect(self.save_zone)
        self.ui.deleteZoneButton.clicked.connect(self.delete_polygon)
        

    
    def save_zone(self):
        zone_cords = self.get_polygon_coordinates()
        self.detector_coords = []
        # coordinares which wil be used to make zone in detector
        for i, zone in enumerate(zone_cords):
            if len(self.zone_arr[i].polygon_points) > 1:
                points = [p for point in zone for p in point]
                points = list(map(int, points))
                self.detector_coords.append(points) 
                
                # print(f"zone_{i} coordinates:")
                # for c in points:
                #     print(c)
        self.data_saved.emit(self.detector_coords)
        

    def add_zone(self):
        polygon_zone = PolygonZone(self.bounding_rect, self.last_changed, self.zone_arr, arr_from_db=[])
        self.scene.addItem(polygon_zone)
        polygon_zone.setZValue(1) 
        self.zone_arr.append(polygon_zone)
        self.last_changed[0] = len(self.zone_arr)-1
        

    def get_polygon_coordinates(self):
        zone_cords=[]
        for zone in self.zone_arr:
            zone_cords.append(zone.get_polygon_coordinates())
        return zone_cords


    def add_polygon_point(self):
        if self.last_changed[0] != None:
            p1 = self.zone_arr[self.last_changed[0]].polygon_points[0]
            p2 = self.zone_arr[self.last_changed[0]].polygon_points[-1]
            new_p = ((p1.x()+p2.x())/2, (p1.y()+p2.y())/2)
            self.zone_arr[self.last_changed[0]].add_point(QPointF(*new_p))
    
    def delete_polygon(self):
        if self.last_changed[0] != None:
            for _ in range(len(self.zone_arr[self.last_changed[0]].polygon_points)):
                self.delete_polygon_point()            

    def delete_polygon_point(self):
        # deletes point fron polygon
        if self.last_changed[0] != None:
            if len(self.zone_arr[self.last_changed[0]].polygon_points)>2:
                self.scene.removeItem(self.zone_arr[self.last_changed[0]].corner_circles[-1])
                self.zone_arr[self.last_changed[0]].delete_point()
            elif len(self.zone_arr[self.last_changed[0]].polygon_points) == 2:
                for _ in range(2):
                    self.scene.removeItem(self.zone_arr[self.last_changed[0]].corner_circles[-1])
                    self.zone_arr[self.last_changed[0]].delete_point()
                         
                self.zone_arr.pop(self.last_changed[0])             
                self.last_changed[0] = None
            
             

def main():
    app = QApplication(sys.argv)
    window = ZoneRedactorWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

# куда деть кадры которые передвются из основного окна?
# что делать с камерами
# куда деть массив с координатами зон?
# что делать с координатами приходящими из бд при включении (еще один конструктор?)