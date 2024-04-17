# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_zone.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Zone_changing(object):
    def setupUi(self, Zone_changing):
        if not Zone_changing.objectName():
            Zone_changing.setObjectName(u"Zone_changing")
        Zone_changing.resize(402, 311)
        Zone_changing.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame = QFrame(Zone_changing)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 381, 291))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_description = QLabel(self.frame)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setStyleSheet(u"font-size: 14px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")

        self.verticalLayout.addWidget(self.lbl_description)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_left_top_cords = QLineEdit(self.frame)
        self.le_left_top_cords.setObjectName(u"le_left_top_cords")
        self.le_left_top_cords.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.gridLayout.addWidget(self.le_left_top_cords, 1, 0, 1, 1)

        self.le_right_top_cords = QLineEdit(self.frame)
        self.le_right_top_cords.setObjectName(u"le_right_top_cords")
        self.le_right_top_cords.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.gridLayout.addWidget(self.le_right_top_cords, 1, 1, 1, 1)

        self.le_left_bottom_cords = QLineEdit(self.frame)
        self.le_left_bottom_cords.setObjectName(u"le_left_bottom_cords")
        self.le_left_bottom_cords.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.gridLayout.addWidget(self.le_left_bottom_cords, 3, 0, 1, 1)

        self.le_right_bottom_cords = QLineEdit(self.frame)
        self.le_right_bottom_cords.setObjectName(u"le_right_bottom_cords")
        self.le_right_bottom_cords.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.gridLayout.addWidget(self.le_right_bottom_cords, 3, 1, 1, 1)

        self.lbl_right_top = QLabel(self.frame)
        self.lbl_right_top.setObjectName(u"lbl_right_top")
        self.lbl_right_top.setStyleSheet(u"font-size: 12px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")

        self.gridLayout.addWidget(self.lbl_right_top, 0, 1, 1, 1)

        self.lbl_left_top = QLabel(self.frame)
        self.lbl_left_top.setObjectName(u"lbl_left_top")
        self.lbl_left_top.setStyleSheet(u"font-size: 12px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")

        self.gridLayout.addWidget(self.lbl_left_top, 0, 0, 1, 1)

        self.lbl_left_bottom = QLabel(self.frame)
        self.lbl_left_bottom.setObjectName(u"lbl_left_bottom")
        self.lbl_left_bottom.setStyleSheet(u"font-size: 12px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")

        self.gridLayout.addWidget(self.lbl_left_bottom, 2, 0, 1, 1)

        self.lbl_right_bottom = QLabel(self.frame)
        self.lbl_right_bottom.setObjectName(u"lbl_right_bottom")
        self.lbl_right_bottom.setStyleSheet(u"font-size: 12px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")

        self.gridLayout.addWidget(self.lbl_right_bottom, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.btn_save_zone = QPushButton(self.frame)
        self.btn_save_zone.setObjectName(u"btn_save_zone")
        self.btn_save_zone.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.btn_save_zone)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Zone_changing)

        QMetaObject.connectSlotsByName(Zone_changing)
    # setupUi

    def retranslateUi(self, Zone_changing):
        Zone_changing.setWindowTitle(QCoreApplication.translate("Zone_changing", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0437\u043e\u043d\u044b", None))
        self.lbl_description.setText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442 \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u0443\u0433\u043b\u0430 \u0437\u043e\u043d\u044b\n"
"\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0446\u0435\u043b\u044b\u043c\u0438 \u0447\u0438\u0441\u043b\u0430\u043c\u0438 \n"
"                     0 < x < 1280   0 < y < 720 ", None))
        self.le_left_top_cords.setText("")
        self.le_left_top_cords.setPlaceholderText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b", None))
        self.le_right_top_cords.setText("")
        self.le_right_top_cords.setPlaceholderText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b", None))
        self.le_left_bottom_cords.setText("")
        self.le_left_bottom_cords.setPlaceholderText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b", None))
        self.le_right_bottom_cords.setText("")
        self.le_right_bottom_cords.setPlaceholderText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b", None))
        self.lbl_right_top.setText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\n"
"\u043f\u0440\u0430\u0432\u043e\u0433\u043e \u0432\u0435\u0440\u0445\u043d\u0435\u0433\u043e \u0443\u0433\u043b\u0430 \u0437\u043e\u043d\u044b", None))
        self.lbl_left_top.setText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\n"
"\u043b\u0435\u0432\u043e\u0433\u043e \u0432\u0435\u0440\u0445\u043d\u0435\u0433\u043e \u0443\u0433\u043b\u0430 \u0437\u043e\u043d\u044b", None))
        self.lbl_left_bottom.setText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\n"
"\u043b\u0435\u0432\u043e\u0433\u043e \u043d\u0438\u0436\u043d\u0435\u0433\u043e \u0443\u0433\u043b\u0430 \u0437\u043e\u043d\u044b", None))
        self.lbl_right_bottom.setText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\n"
"\u043f\u0440\u0430\u0432\u043e\u0433\u043e \u043d\u0438\u0436\u043d\u0435\u0433\u043e \u0443\u0433\u043b\u0430 \u0437\u043e\u043d\u044b", None))
        self.btn_save_zone.setText(QCoreApplication.translate("Zone_changing", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
    # retranslateUi

