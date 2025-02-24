# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1318, 849)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.settings = QAction(MainWindow)
        self.settings.setObjectName(u"settings")
        self.actionst = QAction(MainWindow)
        self.actionst.setObjectName(u"actionst")
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.cameras_settings = QAction(MainWindow)
        self.cameras_settings.setObjectName(u"cameras_settings")
        self.zone_settings = QAction(MainWindow)
        self.zone_settings.setObjectName(u"zone_settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.activate_people_detector = QPushButton(self.frame)
        self.activate_people_detector.setObjectName(u"activate_people_detector")
        self.activate_people_detector.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.gridLayout_2.addWidget(self.activate_people_detector, 1, 2, 1, 1)

        self.cb_current_camera = QComboBox(self.frame)
        self.cb_current_camera.setObjectName(u"cb_current_camera")
        self.cb_current_camera.setStyleSheet(u"QComboBox{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 7px;\n"
"	width: 200px;\n"
"	height: 40px\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}\n"
"\n"
"/*\n"
"\n"
"QComboBox {\n"
"font-size: 16px;\n"
"color: white;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    color: black;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);\n"
"}\n"
"QComboBox:item {                              \n"
"	margin:3px; \n"
"	color: black;\n"
"}  \n"
"\n"
"QComboBox:item:selected\n"
"{\n"
"     border: 0px solid #999900;\n"
"     background: transparent;\n"
"}\n"
"QComboBox:item:checked\n"
"{\n"
"     font-weight: bold;\n"
"}*/")

        self.gridLayout_2.addWidget(self.cb_current_camera, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.video_stream = QLabel(self.frame)
        self.video_stream.setObjectName(u"video_stream")
        self.video_stream.setMinimumSize(QSize(0, 0))
        self.video_stream.setMaximumSize(QSize(1920, 1080))

        self.gridLayout_2.addWidget(self.video_stream, 0, 0, 1, 4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1318, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.settings)
        self.menu.addAction(self.cameras_settings)
        self.menu.addAction(self.zone_settings)

        self.retranslateUi(MainWindow)

        self.cb_current_camera.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MonkeOS-team", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"&\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0447\u0442\u044b", None))
        self.actionst.setText(QCoreApplication.translate("MainWindow", u"st", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.cameras_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u0430\u043c\u0435\u0440", None))
        self.zone_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0437\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.activate_people_detector.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \n"
"\u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435 \u043b\u044e\u0434\u0435\u0439 \n"
"\u043d\u0430 \u0432\u0438\u0434\u0435\u043e", None))
        self.cb_current_camera.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose camera", None))
        self.video_stream.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"&\u041c\u0435\u043d\u044e", None))
    # retranslateUi

