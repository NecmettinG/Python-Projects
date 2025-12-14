# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arayuz_kibris_2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_QuanrumUAVArayz(object):
    def setupUi(self, QuanrumUAVArayz):
        if not QuanrumUAVArayz.objectName():
            QuanrumUAVArayz.setObjectName(u"QuanrumUAVArayz")
        QuanrumUAVArayz.resize(1282, 796)
        self.centralwidget = QWidget(QuanrumUAVArayz)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 650, 1301, 111))
        self.frame.setStyleSheet(u"background-color: #3a3a3a\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_arm = QPushButton(self.frame)
        self.pushButton_arm.setObjectName(u"pushButton_arm")
        self.pushButton_arm.setGeometry(QRect(830, 10, 111, 31))
        self.pushButton_arm.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000;\n"
"    color: white;\n"
"    border: 2px solid #5a0000;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #a00000;  /* \u00dczerine gelince hafif a\u00e7\u0131l\u0131r */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5a0000;  /* T\u0131klan\u0131nca koyula\u015f\u0131r */\n"
"}\n"
"")
        self.pushButton_disarm = QPushButton(self.frame)
        self.pushButton_disarm.setObjectName(u"pushButton_disarm")
        self.pushButton_disarm.setGeometry(QRect(980, 10, 111, 32))
        self.pushButton_disarm.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000;\n"
"    color: white;\n"
"    border: 2px solid #5a0000;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #a00000;  /* \u00dczerine gelince hafif a\u00e7\u0131l\u0131r */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5a0000;  /* T\u0131klan\u0131nca koyula\u015f\u0131r */\n"
"}\n"
"")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 151, 91))
        self.frame_2.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_otokilit = QPushButton(self.frame_2)
        self.pushButton_otokilit.setObjectName(u"pushButton_otokilit")
        self.pushButton_otokilit.setGeometry(QRect(50, 30, 41, 41))
        self.label_vakum_2 = QLabel(self.frame_2)
        self.label_vakum_2.setObjectName(u"label_vakum_2")
        self.label_vakum_2.setGeometry(QRect(20, 10, 121, 16))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 217))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(58, 58, 58, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_vakum_2.setPalette(palette)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(150, 0, 151, 91))
        self.frame_3.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_vakum = QPushButton(self.frame_3)
        self.pushButton_vakum.setObjectName(u"pushButton_vakum")
        self.pushButton_vakum.setGeometry(QRect(50, 30, 41, 41))
        self.label_otokilit = QLabel(self.frame_3)
        self.label_otokilit.setObjectName(u"label_otokilit")
        self.label_otokilit.setGeometry(QRect(20, 10, 121, 16))
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_otokilit.setPalette(palette1)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(300, 0, 151, 91))
        self.frame_4.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_otokenet = QPushButton(self.frame_4)
        self.pushButton_otokenet.setObjectName(u"pushButton_otokenet")
        self.pushButton_otokenet.setGeometry(QRect(50, 30, 41, 41))
        self.label_vakum = QLabel(self.frame_4)
        self.label_vakum.setObjectName(u"label_vakum")
        self.label_vakum.setGeometry(QRect(20, 10, 121, 16))
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_vakum.setPalette(palette2)
        self.pushButton_rtl = QPushButton(self.frame)
        self.pushButton_rtl.setObjectName(u"pushButton_rtl")
        self.pushButton_rtl.setGeometry(QRect(1120, 10, 111, 32))
        self.pushButton_rtl.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000;\n"
"    color: white;\n"
"    border: 2px solid #5a0000;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #a00000;  /* \u00dczerine gelince hafif a\u00e7\u0131l\u0131r */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5a0000;  /* T\u0131klan\u0131nca koyula\u015f\u0131r */\n"
"}\n"
"")
        self.pushButton_emergency = QPushButton(self.frame)
        self.pushButton_emergency.setObjectName(u"pushButton_emergency")
        self.pushButton_emergency.setGeometry(QRect(900, 50, 111, 32))
        self.pushButton_emergency.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000;\n"
"    color: white;\n"
"    border: 2px solid #5a0000;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #a00000;  /* \u00dczerine gelince hafif a\u00e7\u0131l\u0131r */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5a0000;  /* T\u0131klan\u0131nca koyula\u015f\u0131r */\n"
"}\n"
"")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(450, 0, 161, 91))
        self.frame_5.setStyleSheet(u"\n"
"\n"
"background-color: #3a3a3a")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_failsafe_2 = QLabel(self.frame_5)
        self.label_failsafe_2.setObjectName(u"label_failsafe_2")
        self.label_failsafe_2.setGeometry(QRect(50, 10, 61, 16))
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_failsafe_2.setPalette(palette3)
        self.pushButton_failsafe_2 = QPushButton(self.frame_5)
        self.pushButton_failsafe_2.setObjectName(u"pushButton_failsafe_2")
        self.pushButton_failsafe_2.setGeometry(QRect(60, 30, 41, 41))
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(610, 0, 151, 91))
        self.frame_6.setStyleSheet(u"\n"
"\n"
"background-color: #3a3a3a")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_ucusmodu_text = QLabel(self.frame_6)
        self.label_ucusmodu_text.setObjectName(u"label_ucusmodu_text")
        self.label_ucusmodu_text.setGeometry(QRect(40, 10, 81, 16))
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_ucusmodu_text.setPalette(palette4)
        self.pushButton_ucusmodu = QPushButton(self.frame_6)
        self.pushButton_ucusmodu.setObjectName(u"pushButton_ucusmodu")
        self.pushButton_ucusmodu.setGeometry(QRect(60, 30, 41, 41))
        self.pushButton_emergency_2 = QPushButton(self.frame)
        self.pushButton_emergency_2.setObjectName(u"pushButton_emergency_2")
        self.pushButton_emergency_2.setGeometry(QRect(1050, 50, 111, 32))
        self.pushButton_emergency_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000;\n"
"    color: white;\n"
"    border: 2px solid #5a0000;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #a00000;  /* \u00dczerine gelince hafif a\u00e7\u0131l\u0131r */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5a0000;  /* T\u0131klan\u0131nca koyula\u015f\u0131r */\n"
"}\n"
"")
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 180, 761, 471))
        self.frame_8.setStyleSheet(u"background-color: #4d4d4d;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.label_video = QLabel(self.frame_8)
        self.label_video.setObjectName(u"label_video")
        self.label_video.setGeometry(QRect(20, 10, 711, 431))
        self.label_video.setScaledContents(True)
        self.frame_10 = QFrame(self.centralwidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(760, 430, 521, 221))
        self.frame_10.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowser_2 = QTextBrowser(self.frame_10)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(20, 20, 481, 181))
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(760, 70, 521, 361))
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.frame_9.setPalette(palette5)
        self.frame_9.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_fotograf = QLabel(self.frame_9)
        self.label_fotograf.setObjectName(u"label_fotograf")
        self.label_fotograf.setGeometry(QRect(20, 20, 481, 321))
        self.label_fotograf.setPixmap(QPixmap(u"../\u0130HA PROJE/WhatsApp Image 2025-03-28 at 15.20.58.jpeg"))
        self.label_fotograf.setScaledContents(True)
        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 70, 621, 111))
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.frame_11.setPalette(palette6)
        self.frame_11.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.label_kalkiskord = QLabel(self.frame_11)
        self.label_kalkiskord.setObjectName(u"label_kalkiskord")
        self.label_kalkiskord.setGeometry(QRect(30, 10, 121, 16))
        palette7 = QPalette()
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_kalkiskord.setPalette(palette7)
        self.label_haryuzkoord = QLabel(self.frame_11)
        self.label_haryuzkoord.setObjectName(u"label_haryuzkoord")
        self.label_haryuzkoord.setGeometry(QRect(30, 40, 181, 16))
        palette8 = QPalette()
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_haryuzkoord.setPalette(palette8)
        self.textBrowser_4 = QTextBrowser(self.frame_11)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(220, 10, 281, 21))
        self.textBrowser_5 = QTextBrowser(self.frame_11)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(220, 40, 281, 21))
        self.label_haryuzkoord_2 = QLabel(self.frame_11)
        self.label_haryuzkoord_2.setObjectName(u"label_haryuzkoord_2")
        self.label_haryuzkoord_2.setGeometry(QRect(30, 70, 181, 16))
        palette9 = QPalette()
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_haryuzkoord_2.setPalette(palette9)
        self.textBrowser_8 = QTextBrowser(self.frame_11)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(220, 70, 281, 21))
        self.frame_14 = QFrame(self.centralwidget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, -10, 1281, 81))
        palette10 = QPalette()
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.frame_14.setPalette(palette10)
        self.frame_14.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.label_enlem_text = QLabel(self.frame_14)
        self.label_enlem_text.setObjectName(u"label_enlem_text")
        self.label_enlem_text.setGeometry(QRect(40, 20, 58, 16))
        palette11 = QPalette()
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_enlem_text.setPalette(palette11)
        self.label_boylam_text = QLabel(self.frame_14)
        self.label_boylam_text.setObjectName(u"label_boylam_text")
        self.label_boylam_text.setGeometry(QRect(190, 20, 58, 16))
        palette12 = QPalette()
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_boylam_text.setPalette(palette12)
        self.label_irtifa_text = QLabel(self.frame_14)
        self.label_irtifa_text.setObjectName(u"label_irtifa_text")
        self.label_irtifa_text.setGeometry(QRect(330, 20, 58, 16))
        palette13 = QPalette()
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_irtifa_text.setPalette(palette13)
        self.label_roll_text = QLabel(self.frame_14)
        self.label_roll_text.setObjectName(u"label_roll_text")
        self.label_roll_text.setGeometry(QRect(580, 20, 58, 16))
        palette14 = QPalette()
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_roll_text.setPalette(palette14)
        self.label_Yaw_text = QLabel(self.frame_14)
        self.label_Yaw_text.setObjectName(u"label_Yaw_text")
        self.label_Yaw_text.setGeometry(QRect(700, 20, 58, 16))
        palette15 = QPalette()
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_Yaw_text.setPalette(palette15)
        self.label_Pitch_text = QLabel(self.frame_14)
        self.label_Pitch_text.setObjectName(u"label_Pitch_text")
        self.label_Pitch_text.setGeometry(QRect(820, 20, 58, 16))
        palette16 = QPalette()
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_Pitch_text.setPalette(palette16)
        self.label_batarya_text = QLabel(self.frame_14)
        self.label_batarya_text.setObjectName(u"label_batarya_text")
        self.label_batarya_text.setGeometry(QRect(1050, 20, 58, 16))
        palette17 = QPalette()
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_batarya_text.setPalette(palette17)
        self.label_saat_text = QLabel(self.frame_14)
        self.label_saat_text.setObjectName(u"label_saat_text")
        self.label_saat_text.setGeometry(QRect(1180, 20, 58, 16))
        palette18 = QPalette()
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_saat_text.setPalette(palette18)
        self.lcdNumber_batarya = QLCDNumber(self.frame_14)
        self.lcdNumber_batarya.setObjectName(u"lcdNumber_batarya")
        self.lcdNumber_batarya.setGeometry(QRect(1040, 40, 64, 23))
        self.lcdNumber_batarya.setStyleSheet(u"QLCDNumber {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"}\n"
"")
        self.lcdNumber_pitch = QLCDNumber(self.frame_14)
        self.lcdNumber_pitch.setObjectName(u"lcdNumber_pitch")
        self.lcdNumber_pitch.setGeometry(QRect(810, 40, 64, 23))
        self.lcdNumber_pitch.setStyleSheet(u"QLCDNumber {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"}\n"
"")
        self.lcdNumber_yaw = QLCDNumber(self.frame_14)
        self.lcdNumber_yaw.setObjectName(u"lcdNumber_yaw")
        self.lcdNumber_yaw.setGeometry(QRect(690, 40, 64, 23))
        self.lcdNumber_yaw.setStyleSheet(u"QLCDNumber {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"}\n"
"")
        self.lcdNumber_roll = QLCDNumber(self.frame_14)
        self.lcdNumber_roll.setObjectName(u"lcdNumber_roll")
        self.lcdNumber_roll.setGeometry(QRect(570, 40, 64, 23))
        self.lcdNumber_roll.setStyleSheet(u"QLCDNumber {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"}\n"
"")
        self.lcdNumber_irtifa = QLCDNumber(self.frame_14)
        self.lcdNumber_irtifa.setObjectName(u"lcdNumber_irtifa")
        self.lcdNumber_irtifa.setGeometry(QRect(320, 40, 64, 23))
        self.lcdNumber_irtifa.setStyleSheet(u"QLCDNumber {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"}\n"
"")
        self.label_lat = QLabel(self.frame_14)
        self.label_lat.setObjectName(u"label_lat")
        self.label_lat.setGeometry(QRect(40, 40, 58, 16))
        self.label_lat.setStyleSheet(u"color:#00ff00;")
        self.label_long = QLabel(self.frame_14)
        self.label_long.setObjectName(u"label_long")
        self.label_long.setGeometry(QRect(190, 40, 58, 16))
        self.label_long.setStyleSheet(u"color:#00ff00;")
        self.lcdNumber_hiz = QLCDNumber(self.frame_14)
        self.lcdNumber_hiz.setObjectName(u"lcdNumber_hiz")
        self.lcdNumber_hiz.setGeometry(QRect(450, 40, 64, 23))
        self.lcdNumber_hiz.setStyleSheet(u"QLCDNumber {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"}\n"
"\n"
"")
        self.label_hiz_text = QLabel(self.frame_14)
        self.label_hiz_text.setObjectName(u"label_hiz_text")
        self.label_hiz_text.setGeometry(QRect(460, 20, 58, 16))
        palette19 = QPalette()
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_hiz_text.setPalette(palette19)
        self.label_heading_text = QLabel(self.frame_14)
        self.label_heading_text.setObjectName(u"label_heading_text")
        self.label_heading_text.setGeometry(QRect(930, 20, 58, 16))
        palette20 = QPalette()
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_heading_text.setPalette(palette20)
        self.lcdNumber_heading = QLCDNumber(self.frame_14)
        self.lcdNumber_heading.setObjectName(u"lcdNumber_heading")
        self.lcdNumber_heading.setGeometry(QRect(920, 40, 64, 23))
        self.lcdNumber_heading.setStyleSheet(u"QLCDNumber {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"}\n"
"")
        self.label_saat = QLabel(self.frame_14)
        self.label_saat.setObjectName(u"label_saat")
        self.label_saat.setGeometry(QRect(1170, 40, 58, 16))
        self.label_saat.setStyleSheet(u"color:#00ff00;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(620, 70, 141, 111))
        self.label.setPixmap(QPixmap(u"../../Downloads/WhatsApp Image 2025-02-24 at 11.41.50.jpeg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(620, 70, 141, 111))
        self.label_2.setPixmap(QPixmap(u"../\u0130HA PROJE/WhatsApp Image 2025-02-24 at 11.41.50.jpeg"))
        self.label_2.setScaledContents(True)
        QuanrumUAVArayz.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QuanrumUAVArayz)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1282, 24))
        QuanrumUAVArayz.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(QuanrumUAVArayz)
        self.statusbar.setObjectName(u"statusbar")
        QuanrumUAVArayz.setStatusBar(self.statusbar)

        self.retranslateUi(QuanrumUAVArayz)

        QMetaObject.connectSlotsByName(QuanrumUAVArayz)
    # setupUi

    def retranslateUi(self, QuanrumUAVArayz):
        QuanrumUAVArayz.setWindowTitle(QCoreApplication.translate("QuanrumUAVArayz", u"Quantum UAV Aray\u00fcz", None))
        self.pushButton_arm.setText(QCoreApplication.translate("QuanrumUAVArayz", u"ARM", None))
        self.pushButton_disarm.setText(QCoreApplication.translate("QuanrumUAVArayz", u"D\u0130SARM", None))
        self.pushButton_otokilit.setText("")
        self.label_vakum_2.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Kimyasal Kar\u0131\u015f\u0131m", None))
        self.pushButton_vakum.setText("")
        self.label_otokilit.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Otonom Kilitlenme", None))
        self.pushButton_otokenet.setText("")
        self.label_vakum.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Vakumlama Durumu", None))
        self.pushButton_rtl.setText(QCoreApplication.translate("QuanrumUAVArayz", u"RTL", None))
        self.pushButton_emergency.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Acil \u0130ni\u015f", None))
        self.label_failsafe_2.setText(QCoreApplication.translate("QuanrumUAVArayz", u" Fail Safe", None))
        self.pushButton_failsafe_2.setText("")
        self.label_ucusmodu_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u" U\u00e7u\u015f Modu", None))
        self.pushButton_ucusmodu.setText("")
        self.pushButton_emergency_2.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Yetkililere Bildir", None))
        self.label_video.setText(QCoreApplication.translate("QuanrumUAVArayz", u"TextLabel", None))
        self.label_fotograf.setText("")
        self.label_kalkiskord.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Kalk\u0131\u015f Koordinatlar\u0131:", None))
        self.label_haryuzkoord.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Kimyasal Kar\u0131\u015f\u0131m konumu:", None))
        self.label_haryuzkoord_2.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Yang\u0131n Koordinatlaar\u0131:", None))
        self.label_enlem_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Enlem", None))
        self.label_boylam_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Boylam", None))
        self.label_irtifa_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"\u0130rtifa", None))
        self.label_roll_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Roll", None))
        self.label_Yaw_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Yaw", None))
        self.label_Pitch_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Pitch", None))
        self.label_batarya_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Batarya", None))
        self.label_saat_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Saat", None))
        self.label_lat.setText(QCoreApplication.translate("QuanrumUAVArayz", u"enlem", None))
        self.label_long.setText(QCoreApplication.translate("QuanrumUAVArayz", u"boylam", None))
        self.label_hiz_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"H\u0131z", None))
        self.label_heading_text.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Heading", None))
        self.label_saat.setText(QCoreApplication.translate("QuanrumUAVArayz", u"saat", None))
        self.label.setText("")
        self.label_2.setText("")
    # retranslateUi

