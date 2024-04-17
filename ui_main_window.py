# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1262, 825)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.menu_change_zone = QAction(MainWindow)
        self.menu_change_zone.setObjectName(u"menu_change_zone")
        self.actionst = QAction(MainWindow)
        self.actionst.setObjectName(u"actionst")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.activate_people_detector = QPushButton(self.centralwidget)
        self.activate_people_detector.setObjectName(u"activate_people_detector")
        self.activate_people_detector.setGeometry(QRect(573, 735, 155, 65))
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
        self.video_stream = QLabel(self.centralwidget)
        self.video_stream.setObjectName(u"video_stream")
        self.video_stream.setGeometry(QRect(10, 10, 1280, 720))
        self.video_stream.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1262, 22))
        self.settings = QMenu(self.menubar)
        self.settings.setObjectName(u"settings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.settings.menuAction())
        self.settings.addAction(self.menu_change_zone)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MonkeOS-team", None))
        self.menu_change_zone.setText(QCoreApplication.translate("MainWindow", u"&\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.actionst.setText(QCoreApplication.translate("MainWindow", u"st", None))
        self.activate_people_detector.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \n"
"\u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435 \u043b\u044e\u0434\u0435\u0439 \n"
"\u043d\u0430 \u0432\u0438\u0434\u0435\u043e", None))
        self.video_stream.setText("")
        self.settings.setTitle(QCoreApplication.translate("MainWindow", u"&\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

