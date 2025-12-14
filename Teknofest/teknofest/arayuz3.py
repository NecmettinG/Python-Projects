# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arayuz_serbestg.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_QuanrumUAVArayz(object):
    def setupUi(self, QuanrumUAVArayz):
        if not QuanrumUAVArayz.objectName():
            QuanrumUAVArayz.setObjectName(u"QuanrumUAVArayz")
        QuanrumUAVArayz.resize(1282, 786)
        self.centralwidget = QWidget(QuanrumUAVArayz)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 650, 1281, 91))
        self.frame.setStyleSheet(u"background-color: #3a3a3a\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_arm = QPushButton(self.frame)
        self.pushButton_arm.setObjectName(u"pushButton_arm")
        self.pushButton_arm.setGeometry(QRect(370, 30, 100, 32))
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
        self.pushButton_disarm.setGeometry(QRect(520, 30, 100, 32))
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
        self.pushButton_rtl = QPushButton(self.frame)
        self.pushButton_rtl.setObjectName(u"pushButton_rtl")
        self.pushButton_rtl.setGeometry(QRect(670, 30, 100, 32))
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
        self.pushButton_emergency.setGeometry(QRect(820, 30, 100, 32))
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
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 570, 221, 81))
        self.frame_2.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_otokilit = QLabel(self.frame_2)
        self.label_otokilit.setObjectName(u"label_otokilit")
        self.label_otokilit.setGeometry(QRect(50, 10, 121, 16))
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
        self.label_otokilit.setPalette(palette)
        self.indicator_otokilit = QLabel(self.frame_2)
        self.indicator_otokilit.setObjectName(u"indicator_otokilit")
        self.indicator_otokilit.setGeometry(QRect(80, 30, 41, 41))
        self.indicator_otokilit.setStyleSheet("background-color: red; border: 1px solid black;")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(430, 570, 221, 80))
        self.frame_4.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_otokenet = QLabel(self.frame_4)
        self.label_otokenet.setObjectName(u"label_otokenet")
        self.label_otokenet.setGeometry(QRect(50, 10, 131, 16))
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
        self.label_otokenet.setPalette(palette1)
        self.indicator_otokenet = QLabel(self.frame_4)
        self.indicator_otokenet.setObjectName(u"indicator_otokenet")
        self.indicator_otokenet.setGeometry(QRect(90, 30, 41, 41))
        self.indicator_otokenet.setStyleSheet("background-color: red; border: 1px solid black;")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(650, 570, 211, 80))
        self.frame_5.setStyleSheet(u"\n"
"\n"
"background-color: #3a3a3a")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_ucusmodu = QLabel(self.frame_5)
        self.label_ucusmodu.setObjectName(u"label_ucusmodu")
        self.label_ucusmodu.setGeometry(QRect(70, 10, 71, 16))
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
        self.label_ucusmodu.setPalette(palette2)
        self.label_modelabel = QLabel(self.frame_5)
        self.label_modelabel.setObjectName(u"label_modelabel")
        self.label_modelabel.setGeometry(QRect(70, 40, 91, 16))
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
        self.label_modelabel.setPalette(palette3)
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(860, 570, 211, 81))
        self.frame_6.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_mobilbaglanti = QLabel(self.frame_6)
        self.label_mobilbaglanti.setObjectName(u"label_mobilbaglanti")
        self.label_mobilbaglanti.setGeometry(QRect(70, 10, 91, 16))
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
        self.label_mobilbaglanti.setPalette(palette4)
        self.indicator_mobilbaglanti = QLabel(self.frame_6)
        self.indicator_mobilbaglanti.setObjectName(u"indicator_mobilbaglanti")
        self.indicator_mobilbaglanti.setGeometry(QRect(90, 30, 41, 41))
        self.indicator_mobilbaglanti.setStyleSheet("background-color: red; border: 1px solid black;")
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(1070, 570, 211, 81))
        self.frame_7.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_failsafe = QLabel(self.frame_7)
        self.label_failsafe.setObjectName(u"label_failsafe")
        self.label_failsafe.setGeometry(QRect(80, 10, 58, 16))
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
        self.label_failsafe.setPalette(palette5)
        self.indicator_failsafe = QLabel(self.frame_7)
        self.indicator_failsafe.setObjectName(u"indicator_failsafe")
        self.indicator_failsafe.setGeometry(QRect(90, 30, 41, 41))
        self.indicator_failsafe.setStyleSheet("background-color: red; border: 1px solid black;")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(220, 570, 211, 80))
        self.frame_3.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_vakum = QLabel(self.frame_3)
        self.label_vakum.setObjectName(u"label_vakum")
        self.label_vakum.setGeometry(QRect(50, 10, 121, 16))
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_vakum.setPalette(palette6)
        self.indicator_vakum = QLabel(self.frame_3)
        self.indicator_vakum.setObjectName(u"indicator_vakum")
        self.indicator_vakum.setGeometry(QRect(90, 30, 41, 41))
        self.indicator_vakum.setStyleSheet("background-color: red; border: 1px solid black;")
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 170, 761, 401))
        self.frame_8.setStyleSheet(u"background-color: #4d4d4d;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowser_6 = QTextBrowser(self.frame_8)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(20, 30, 711, 351))
        palette7 = QPalette()
        brush2 = QBrush(QColor(246, 246, 246, 216))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        brush4 = QBrush(QColor(251, 254, 254, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush4)
        brush5 = QBrush(QColor(255, 255, 255, 216))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush5)
        brush6 = QBrush(QColor(252, 252, 252, 216))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush6)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
        brush7 = QBrush(QColor(252, 252, 252, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush7)
        brush8 = QBrush(QColor(253, 253, 253, 216))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush8)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush4)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush5)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush6)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush7)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush8)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush4)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush7)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush8)
        self.textBrowser_6.setPalette(palette7)

        self.textBrowser_6.setParent(None)
        
        # Create a QLabel for video display with the same geometry
        self.video_label = QLabel(self.frame_8)
        self.video_label.setObjectName("video_label")
        self.video_label.setGeometry(20, 30, 711, 351)  # Same as textBrowser_6
        
        # Set styling to match the original design
        self.video_label.setStyleSheet("""
            QLabel {
                background-color: #4d4d4d;
                border: 1px solid #666666;
                color: white;
            }
        """)
        
        # Set alignment and initial text
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setText("RTSP Stream Loading...")
        self.video_label.setScaledContents(True)

        self.frame_10 = QFrame(self.centralwidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(760, 390, 521, 181))
        self.frame_10.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowser_2 = QTextBrowser(self.frame_10)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(20, 20, 481, 141))
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(760, 170, 521, 221))
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
        self.frame_9.setPalette(palette8)
        self.frame_9.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowserPhoto = QLabel(self.frame_9)
        self.textBrowserPhoto.setObjectName(u"textBrowserPhoto")
        self.textBrowserPhoto.setGeometry(QRect(20, 20, 240, 171))
        self.textBrowserDB = QTextBrowser(self.frame_9)
        self.textBrowserDB.setObjectName(u"textBrowserDB")
        self.textBrowserDB.setGeometry(QRect(260, 20, 240, 171))
        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 70, 571, 101))
        palette9 = QPalette()
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.frame_11.setPalette(palette9)
        self.frame_11.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.label_kalkiskord = QLabel(self.frame_11)
        self.label_kalkiskord.setObjectName(u"label_kalkiskord")
        self.label_kalkiskord.setGeometry(QRect(30, 30, 121, 16))
        palette10 = QPalette()
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_kalkiskord.setPalette(palette10)
        self.label_haryuzkoord = QLabel(self.frame_11)
        self.label_haryuzkoord.setObjectName(u"label_haryuzkoord")
        self.label_haryuzkoord.setGeometry(QRect(30, 60, 181, 16))
        palette11 = QPalette()
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_haryuzkoord.setPalette(palette11)
        self.textBrowser_4 = QTextBrowser(self.frame_11)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(220, 30, 281, 21))
        self.textBrowser_5 = QTextBrowser(self.frame_11)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(220, 60, 281, 21))
        self.frame_12 = QFrame(self.centralwidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(710, 70, 571, 101))
        palette12 = QPalette()
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.frame_12.setPalette(palette12)
        self.frame_12.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        #self.label_yabnesne1 = QLabel(self.frame_12)
        #self.label_yabnesne1.setObjectName(u"label_yabnesne1")
        #self.label_yabnesne1.setGeometry(QRect(30, 30, 171, 16))
        palette13 = QPalette()
        brush9 = QBrush(QColor(254, 254, 254, 216))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush9)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush9)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        #self.label_yabnesne1.setPalette(palette13)
        #self.label_yabnesne2 = QLabel(self.frame_12)
        #self.label_yabnesne2.setObjectName(u"label_yabnesne2")
        #self.label_yabnesne2.setGeometry(QRect(30, 60, 171, 16))
        self.label_yabnesne = QLabel(self.frame_12)
        self.label_yabnesne.setObjectName(u"label_yabnesne")
        self.label_yabnesne.setGeometry(QRect(30, 45, 171, 16))
        self.label_yabnesne.setPalette(palette13)
        #palette14 = QPalette()
        #palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush9)
        #palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        #palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        #palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        #palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush9)
        #palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        #palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        #palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        #palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        #palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        #palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        #self.label_yabnesne2.setPalette(palette14)
        #self.textBrowser = QTextBrowser(self.frame_12)
        #self.textBrowser.setObjectName(u"textBrowser")
        #self.textBrowser.setGeometry(QRect(200, 30, 281, 21))
        #self.textBrowser_3 = QTextBrowser(self.frame_12)
        #self.textBrowser_3.setObjectName(u"textBrowser_3")
        #self.textBrowser_3.setGeometry(QRect(200, 60, 281, 21))
        self.dangerZoneTextBrowser = QTextBrowser(self.frame_12)
        self.dangerZoneTextBrowser.setObjectName(u"dangerZoneTextBrowser")
        self.dangerZoneTextBrowser.setGeometry(QRect(200, 38, 281, 42))
        self.frame_14 = QFrame(self.centralwidget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, -10, 1281, 81))
        palette15 = QPalette()
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.frame_14.setPalette(palette15)
        self.frame_14.setStyleSheet(u"background-color: #3a3a3a")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.label_enlem = QLabel(self.frame_14)
        self.label_enlem.setObjectName(u"label_enlem")
        self.label_enlem.setGeometry(QRect(40, 20, 58, 16))
        palette16 = QPalette()
        brush10 = QBrush(QColor(255, 255, 255, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_enlem.setPalette(palette16)
        self.label_boylam = QLabel(self.frame_14)
        self.label_boylam.setObjectName(u"label_boylam")
        self.label_boylam.setGeometry(QRect(190, 20, 58, 16))
        palette17 = QPalette()
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_boylam.setPalette(palette17)
        self.label_irtifa = QLabel(self.frame_14)
        self.label_irtifa.setObjectName(u"label_irtifa")
        self.label_irtifa.setGeometry(QRect(350, 20, 58, 16))
        palette18 = QPalette()
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_irtifa.setPalette(palette18)
        self.label_roll = QLabel(self.frame_14)
        self.label_roll.setObjectName(u"label_roll")
        self.label_roll.setGeometry(QRect(650, 20, 58, 16))
        palette19 = QPalette()
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_roll.setPalette(palette19)
        self.label_Yaw = QLabel(self.frame_14)
        self.label_Yaw.setObjectName(u"label_Yaw")
        self.label_Yaw.setGeometry(QRect(790, 20, 58, 16))
        palette20 = QPalette()
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_Yaw.setPalette(palette20)
        self.label_Pitch = QLabel(self.frame_14)
        self.label_Pitch.setObjectName(u"label_Pitch")
        self.label_Pitch.setGeometry(QRect(930, 20, 58, 16))
        palette21 = QPalette()
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_Pitch.setPalette(palette21)
        self.label_batarya = QLabel(self.frame_14)
        self.label_batarya.setObjectName(u"label_batarya")
        self.label_batarya.setGeometry(QRect(1060, 20, 58, 16))
        palette22 = QPalette()
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_batarya.setPalette(palette22)
        self.label_saat = QLabel(self.frame_14)
        self.label_saat.setObjectName(u"label_saat")
        self.label_saat.setGeometry(QRect(1180, 20, 58, 16))
        palette23 = QPalette()
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_saat.setPalette(palette23)
        self.label_saat_display = QLabel(self.frame_14)
        self.label_saat_display.setObjectName(u"label_saat_display")
        self.label_saat_display.setGeometry(QRect(1150, 40, 100, 23))
        self.label_saat_display.setStyleSheet(u"QLabel {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"    font-family: 'OCR A Std', 'Courier New', monospace;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #333;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.label_saat_display.setAlignment(Qt.AlignCenter)
        self.label_batarya_display = QLabel(self.frame_14)
        self.label_batarya_display.setObjectName(u"label_batarya_display")
        self.label_batarya_display.setGeometry(QRect(1030, 40, 100, 23))
        self.label_batarya_display.setStyleSheet(u"QLabel {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"    font-family: 'OCR A Std', 'Courier New', monospace;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #333;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.label_batarya_display.setAlignment(Qt.AlignCenter)
        self.label_pitch_display = QLabel(self.frame_14)
        self.label_pitch_display.setObjectName(u"label_pitch_display")
        self.label_pitch_display.setGeometry(QRect(900, 40, 100, 23))
        self.label_pitch_display.setStyleSheet(u"QLabel {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"    font-family: 'OCR A Std', 'Courier New', monospace;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #333;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.label_pitch_display.setAlignment(Qt.AlignCenter)
        self.label_yaw_display = QLabel(self.frame_14)
        self.label_yaw_display.setObjectName(u"label_yaw_display")
        self.label_yaw_display.setGeometry(QRect(760, 40, 100, 23))
        self.label_yaw_display.setStyleSheet(u"QLabel {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"    font-family: 'OCR A Std', 'Courier New', monospace;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #333;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.label_yaw_display.setAlignment(Qt.AlignCenter)
        self.label_roll_display = QLabel(self.frame_14)
        self.label_roll_display.setObjectName(u"label_roll_display")
        self.label_roll_display.setGeometry(QRect(620, 40, 100, 23))
        self.label_roll_display.setStyleSheet(u"QLabel {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"    font-family: 'OCR A Std', 'Courier New', monospace;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #333;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.label_roll_display.setAlignment(Qt.AlignCenter)
        self.label_altitude_display = QLabel(self.frame_14)
        self.label_altitude_display.setObjectName(u"label_altitude_display")
        self.label_altitude_display.setGeometry(QRect(320, 40, 100, 23))
        self.label_altitude_display.setStyleSheet(u"QLabel {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"    font-family: 'OCR A Std', 'Courier New', monospace;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #333;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.label_altitude_display.setAlignment(Qt.AlignCenter)
        self.label_enlem_2 = QLabel(self.frame_14)
        self.label_enlem_2.setObjectName(u"label_enlem_2")
        self.label_enlem_2.setGeometry(QRect(40, 40, 58, 16))
        self.label_enlem_2.setStyleSheet(u"color:#00ff00;")
        self.label_boylam_2 = QLabel(self.frame_14)
        self.label_boylam_2.setObjectName(u"label_boylam_2")
        self.label_boylam_2.setGeometry(QRect(190, 40, 58, 16))
        self.label_boylam_2.setStyleSheet(u"color:#00ff00;")
        self.label_hiz_display = QLabel(self.frame_14)
        self.label_hiz_display.setObjectName(u"label_hiz_display")
        self.label_hiz_display.setGeometry(QRect(470, 40, 100, 23))
        self.label_hiz_display.setStyleSheet(u"QLabel {\n"
"    background-color: black;\n"
"    color: #00ff00;\n"
"    font-family: 'OCR A Std', 'Courier New', monospace;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #333;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"")
        self.label_hiz_display.setAlignment(Qt.AlignCenter)
        self.label_hiz = QLabel(self.frame_14)
        self.label_hiz.setObjectName(u"label_hiz")
        self.label_hiz.setGeometry(QRect(500, 20, 58, 16))
        palette24 = QPalette()
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.label_hiz.setPalette(palette24)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(570, 70, 141, 100))
        self.label.setPixmap(QPixmap(u"C:/Users/Asus/Desktop/quantum_photo.jpg"))
        self.label.setScaledContents(True)
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
        self.pushButton_rtl.setText(QCoreApplication.translate("QuanrumUAVArayz", u"RTL", None))
        self.pushButton_emergency.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Acil \u0130ni\u015f", None))
        self.label_otokilit.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Otonom Kilitlenme", None))
        self.indicator_otokilit.setText("")
        self.label_otokenet.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Otonom Kenetlenme", None))
        self.indicator_otokenet.setText("")
        self.label_ucusmodu.setText(QCoreApplication.translate("QuanrumUAVArayz", u"U\u00e7u\u015f Modu", None))
        self.label_modelabel.setText(QCoreApplication.translate("QuanrumUAVArayz", u"otonom", None))
        self.label_mobilbaglanti.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Mobil Ba\u011flant\u0131", None))
        self.indicator_mobilbaglanti.setText("")
        self.label_failsafe.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Fail Safe", None))
        self.indicator_failsafe.setText("")
        self.label_vakum.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Vakumlama Durumu", None))
        self.indicator_vakum.setText("")
        self.textBrowser_6.setHtml(QCoreApplication.translate("QuanrumUAVArayz", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_kalkiskord.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Kalk\u0131\u015f Koordinatlar\u0131:", None))
        self.label_haryuzkoord.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Hareketli Y\u00fczey Koordinatlar\u0131:", None))
        #self.label_yabnesne1.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Yabanc\u0131 Nesne Koordinat 1:", None))
        #self.label_yabnesne2.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Yabanc\u0131 Nesne Koordinat 2:", None))
        self.label_yabnesne.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Yabanc\u0131 Nesne Koordinat:", None))
        self.label_enlem.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Enlem", None))
        self.label_boylam.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Boylam", None))
        self.label_irtifa.setText(QCoreApplication.translate("QuanrumUAVArayz", u"\u0130rtifa", None))
        self.label_roll.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Roll", None))
        self.label_Yaw.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Yaw", None))
        self.label_Pitch.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Pitch", None))
        self.label_batarya.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Batarya", None))
        self.label_saat.setText(QCoreApplication.translate("QuanrumUAVArayz", u"Saat", None))
        self.label_enlem_2.setText(QCoreApplication.translate("QuanrumUAVArayz", u"enlem", None))
        self.label_boylam_2.setText(QCoreApplication.translate("QuanrumUAVArayz", u"boylam", None))
        self.label_hiz.setText(QCoreApplication.translate("QuanrumUAVArayz", u"H\u0131z", None))
        self.label.setText("")
    # retranslateUi

