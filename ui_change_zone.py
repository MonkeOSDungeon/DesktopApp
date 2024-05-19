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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_Zone_changing(object):
    def setupUi(self, Zone_changing):
        if not Zone_changing.objectName():
            Zone_changing.setObjectName(u"Zone_changing")
        Zone_changing.resize(614, 348)
        Zone_changing.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.gridLayout_3 = QGridLayout(Zone_changing)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(Zone_changing)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"  background-color: rgda(0, 0, 0, 0);\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  color: white;\n"
"  background-color: rgba(255, 255, 255, 30);\n"
"  border: 1px solid rgba(255, 255, 255, 40);\n"
"  width: 150px;\n"
"  height: 25px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.zone_tab = QWidget()
        self.zone_tab.setObjectName(u"zone_tab")
        self.gridLayout_2 = QGridLayout(self.zone_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.zone_tab)
        self.frame.setObjectName(u"frame")
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
        self.lbl_description.setTextFormat(Qt.AutoText)
        self.lbl_description.setScaledContents(False)
        self.lbl_description.setAlignment(Qt.AlignCenter)

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


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.zone_tab, "")
        self.oth_settings_tab = QWidget()
        self.oth_settings_tab.setObjectName(u"oth_settings_tab")
        self.gridLayout_4 = QGridLayout(self.oth_settings_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_2 = QFrame(self.oth_settings_tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_sender = QLabel(self.frame_2)
        self.lbl_sender.setObjectName(u"lbl_sender")
        self.lbl_sender.setStyleSheet(u"font-size: 14px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")

        self.horizontalLayout_3.addWidget(self.lbl_sender)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.le_sender_email = QLineEdit(self.frame_2)
        self.le_sender_email.setObjectName(u"le_sender_email")
        self.le_sender_email.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.verticalLayout_4.addWidget(self.le_sender_email)

        self.le_sender_pass = QLineEdit(self.frame_2)
        self.le_sender_pass.setObjectName(u"le_sender_pass")
        self.le_sender_pass.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")
        self.le_sender_pass.setFrame(True)
        self.le_sender_pass.setEchoMode(QLineEdit.Password)
        self.le_sender_pass.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.le_sender_pass)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.btn_save_sender = QPushButton(self.frame_2)
        self.btn_save_sender.setObjectName(u"btn_save_sender")
        self.btn_save_sender.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btn_save_sender)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_reciever = QLabel(self.frame_2)
        self.lbl_reciever.setObjectName(u"lbl_reciever")
        self.lbl_reciever.setStyleSheet(u"font-size: 14px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")

        self.horizontalLayout.addWidget(self.lbl_reciever)

        self.le_email_reciever = QLineEdit(self.frame_2)
        self.le_email_reciever.setObjectName(u"le_email_reciever")
        self.le_email_reciever.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.horizontalLayout.addWidget(self.le_email_reciever)

        self.btn_save_reciever = QPushButton(self.frame_2)
        self.btn_save_reciever.setObjectName(u"btn_save_reciever")
        self.btn_save_reciever.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_save_reciever)


        self.gridLayout_5.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_resolution = QLabel(self.frame_2)
        self.lbl_resolution.setObjectName(u"lbl_resolution")
        self.lbl_resolution.setStyleSheet(u"font-size: 14px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-color: none;\n"
"border: none")

        self.horizontalLayout_2.addWidget(self.lbl_resolution)

        self.le_resolution = QLineEdit(self.frame_2)
        self.le_resolution.setObjectName(u"le_resolution")
        self.le_resolution.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 5px;")

        self.horizontalLayout_2.addWidget(self.le_resolution)

        self.btn_save_resolution = QPushButton(self.frame_2)
        self.btn_save_resolution.setObjectName(u"btn_save_resolution")
        self.btn_save_resolution.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_save_resolution)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.oth_settings_tab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Zone_changing)

        self.tabWidget.setCurrentIndex(1)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zone_tab), QCoreApplication.translate("Zone_changing", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0437\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.lbl_sender.setText(QCoreApplication.translate("Zone_changing", u"\u041f\u043e\u0447\u0442\u0430, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439\n"
"\u0431\u0443\u0434\u0443\u0442 \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u0442\u044c\n"
"\u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f:", None))
        self.le_sender_email.setText(QCoreApplication.translate("Zone_changing", u"zone.monitor.alert@gmail.com", None))
        self.le_sender_email.setPlaceholderText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u0447\u0442\u044b", None))
        self.le_sender_pass.setText(QCoreApplication.translate("Zone_changing", u"G7rB!x2#VpQ8^yM0", None))
        self.le_sender_pass.setPlaceholderText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_save_sender.setText(QCoreApplication.translate("Zone_changing", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.lbl_reciever.setText(QCoreApplication.translate("Zone_changing", u"\u041f\u043e\u0447\u0442\u0430, \u043a\u0443\u0434\u0430\n"
"\u0431\u0443\u0434\u0443\u0442 \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u0442\u044c\n"
"\u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f:", None))
        self.le_email_reciever.setPlaceholderText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u0447\u0442\u044b", None))
        self.btn_save_reciever.setText(QCoreApplication.translate("Zone_changing", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.lbl_resolution.setText(QCoreApplication.translate("Zone_changing", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u0432\u0438\u0434\u0435\u043e:", None))
        self.le_resolution.setPlaceholderText(QCoreApplication.translate("Zone_changing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u0430 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b", None))
        self.btn_save_resolution.setText(QCoreApplication.translate("Zone_changing", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.oth_settings_tab), QCoreApplication.translate("Zone_changing", u"\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

