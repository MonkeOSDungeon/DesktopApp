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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 825)
        MainWindow.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.activate_people_detector = QPushButton(self.centralwidget)
        self.activate_people_detector.setObjectName(u"activate_people_detector")
        self.activate_people_detector.setGeometry(QRect(573, 735, 155, 65))
        self.activate_people_detector.setStyleSheet(u"background-color: rgb(110, 110, 110);")
        self.video_stream = QLabel(self.centralwidget)
        self.video_stream.setObjectName(u"video_stream")
        self.video_stream.setGeometry(QRect(10, 10, 1280, 720))
        self.video_stream.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1300, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MonkeOS-team", None))
        self.activate_people_detector.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \n"
"\u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435 \u043b\u044e\u0434\u0435\u0439 \n"
"\u043d\u0430 \u0432\u0438\u0434\u0435\u043e", None))
        self.video_stream.setText("")
    # retranslateUi

