# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_email.ui'
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

class Ui_EmailChanging(object):
    def setupUi(self, EmailChanging):
        if not EmailChanging.objectName():
            EmailChanging.setObjectName(u"EmailChanging")
        EmailChanging.resize(614, 348)
        EmailChanging.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.gridLayout = QGridLayout(EmailChanging)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(EmailChanging)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
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
        self.le_sender_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.le_sender_pass.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

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


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(EmailChanging)

        QMetaObject.connectSlotsByName(EmailChanging)
    # setupUi

    def retranslateUi(self, EmailChanging):
        EmailChanging.setWindowTitle(QCoreApplication.translate("EmailChanging", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0437\u043e\u043d\u044b", None))
        self.lbl_sender.setText(QCoreApplication.translate("EmailChanging", u"\u041f\u043e\u0447\u0442\u0430, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439\n"
"\u0431\u0443\u0434\u0443\u0442 \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u0442\u044c\n"
"\u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f:", None))
        self.le_sender_email.setText(QCoreApplication.translate("EmailChanging", u"zone.monitor.alert@gmail.com", None))
        self.le_sender_email.setPlaceholderText(QCoreApplication.translate("EmailChanging", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u0447\u0442\u044b", None))
        self.le_sender_pass.setText(QCoreApplication.translate("EmailChanging", u"G7rB!x2#VpQ8^yM0", None))
        self.le_sender_pass.setPlaceholderText(QCoreApplication.translate("EmailChanging", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_save_sender.setText(QCoreApplication.translate("EmailChanging", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.lbl_reciever.setText(QCoreApplication.translate("EmailChanging", u"\u041f\u043e\u0447\u0442\u0430, \u043a\u0443\u0434\u0430\n"
"\u0431\u0443\u0434\u0443\u0442 \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u0442\u044c\n"
"\u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f:", None))
        self.le_email_reciever.setPlaceholderText(QCoreApplication.translate("EmailChanging", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u0447\u0442\u044b", None))
        self.btn_save_reciever.setText(QCoreApplication.translate("EmailChanging", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

