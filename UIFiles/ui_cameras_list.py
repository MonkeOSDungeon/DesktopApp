# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameras.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_CamerasWindow(object):
    def setupUi(self, CamerasWindow):
        if not CamerasWindow.objectName():
            CamerasWindow.setObjectName(u"CamerasWindow")
        CamerasWindow.resize(400, 300)
        CamerasWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(CamerasWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add_camera = QPushButton(CamerasWindow)
        self.btn_add_camera.setObjectName(u"btn_add_camera")
        self.btn_add_camera.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_add_camera)

        self.btn_edit_camera = QPushButton(CamerasWindow)
        self.btn_edit_camera.setObjectName(u"btn_edit_camera")
        self.btn_edit_camera.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_edit_camera)

        self.btn_delete_camera = QPushButton(CamerasWindow)
        self.btn_delete_camera.setObjectName(u"btn_delete_camera")
        self.btn_delete_camera.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_delete_camera)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tbl_cameras = QTableView(CamerasWindow)
        self.tbl_cameras.setObjectName(u"tbl_cameras")
        self.tbl_cameras.setStyleSheet(u"QTableView {\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-bottom-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section{\n"
"	background-color: rgb(53, 53, 53);\n"
"	color: white;\n"
"	border: none;\n"
"	height: 50px;\n"
"	font-size: 14px\n"
"}\n"
"\n"
"QTableView::item {\n"
"	border-style: none;\n"
"	border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableView::item::selected{\n"
"	border: none;\n"
"	color: rgba(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tbl_cameras.setShowGrid(False)

        self.verticalLayout.addWidget(self.tbl_cameras)


        self.retranslateUi(CamerasWindow)

        QMetaObject.connectSlotsByName(CamerasWindow)
    # setupUi

    def retranslateUi(self, CamerasWindow):
        CamerasWindow.setWindowTitle(QCoreApplication.translate("CamerasWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u0430\u043c\u0435\u0440", None))
        self.btn_add_camera.setText(QCoreApplication.translate("CamerasWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u043c\u0435\u0440\u0443", None))
        self.btn_edit_camera.setText(QCoreApplication.translate("CamerasWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043a\u0430\u043c\u0435\u0440\u0443", None))
        self.btn_delete_camera.setText(QCoreApplication.translate("CamerasWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u0430\u043c\u0435\u0440\u0443", None))
    # retranslateUi

