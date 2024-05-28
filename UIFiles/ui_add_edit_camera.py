# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_camera.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddEditCamera(object):
    def setupUi(self, AddEditCamera):
        if not AddEditCamera.objectName():
            AddEditCamera.setObjectName(u"AddEditCamera")
        AddEditCamera.resize(390, 240)
        AddEditCamera.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.gridLayout = QGridLayout(AddEditCamera)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(AddEditCamera)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_name = QLabel(self.frame)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setStyleSheet(u"font-size: 14px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")
        self.lbl_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lbl_name)

        self.le_name = QLineEdit(self.frame)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.horizontalLayout_2.addWidget(self.le_name)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_ip = QLabel(self.frame)
        self.lbl_ip.setObjectName(u"lbl_ip")
        self.lbl_ip.setStyleSheet(u"font-size: 14px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")
        self.lbl_ip.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_ip)

        self.le_ip = QLineEdit(self.frame)
        self.le_ip.setObjectName(u"le_ip")
        self.le_ip.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.horizontalLayout.addWidget(self.le_ip)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_fps = QLabel(self.frame)
        self.lbl_fps.setObjectName(u"lbl_fps")
        self.lbl_fps.setStyleSheet(u"font-size: 14px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")
        self.lbl_fps.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_fps)

        self.le_fps = QLineEdit(self.frame)
        self.le_fps.setObjectName(u"le_fps")
        self.le_fps.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.horizontalLayout_3.addWidget(self.le_fps)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_resolution = QLabel(self.frame)
        self.lbl_resolution.setObjectName(u"lbl_resolution")
        self.lbl_resolution.setStyleSheet(u"font-size: 14px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")
        self.lbl_resolution.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_resolution)

        self.le_resolution = QLineEdit(self.frame)
        self.le_resolution.setObjectName(u"le_resolution")
        self.le_resolution.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.horizontalLayout_4.addWidget(self.le_resolution)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.btn_save_camera = QPushButton(self.frame)
        self.btn_save_camera.setObjectName(u"btn_save_camera")
        self.btn_save_camera.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 7px;\n"
"	width: 100px;\n"
"	height: 25px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.verticalLayout.addWidget(self.btn_save_camera)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(AddEditCamera)

        QMetaObject.connectSlotsByName(AddEditCamera)
    # setupUi

    def retranslateUi(self, AddEditCamera):
        AddEditCamera.setWindowTitle(QCoreApplication.translate("AddEditCamera", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.lbl_name.setText(QCoreApplication.translate("AddEditCamera", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.le_name.setText("")
        self.le_name.setPlaceholderText(QCoreApplication.translate("AddEditCamera", u"\u0412\u0435\u0431\u043a\u0430\u043c\u0435\u0440\u0430 1", None))
        self.lbl_ip.setText(QCoreApplication.translate("AddEditCamera", u"IP", None))
        self.le_ip.setText("")
        self.le_ip.setPlaceholderText(QCoreApplication.translate("AddEditCamera", u"http://192.168.0.183:4747/video", None))
        self.lbl_fps.setText(QCoreApplication.translate("AddEditCamera", u"FPS", None))
        self.le_fps.setText(QCoreApplication.translate("AddEditCamera", u"30", None))
        self.le_fps.setPlaceholderText(QCoreApplication.translate("AddEditCamera", u"30", None))
        self.lbl_resolution.setText(QCoreApplication.translate("AddEditCamera", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.le_resolution.setText(QCoreApplication.translate("AddEditCamera", u"1280 720", None))
        self.le_resolution.setPlaceholderText(QCoreApplication.translate("AddEditCamera", u"1280 720", None))
        self.btn_save_camera.setText(QCoreApplication.translate("AddEditCamera", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

