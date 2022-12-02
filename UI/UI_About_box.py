# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_About_box.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(672, 440)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(500, 50))
        self.label_3.setMaximumSize(QSize(2160, 50))
        palette = QPalette()
        brush = QBrush(QColor(255, 85, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_3.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(500, 300))
        font1 = QFont()
        font1.setPointSize(12)
        self.textBrowser.setFont(font1)

        self.verticalLayout.addWidget(self.textBrowser)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"About", None))
        self.textBrowser.setMarkdown(QCoreApplication.translate("Form", u"# REXS scan control project\n"
"\n"
"## Introduction\n"
"\n"
"**This is a user interface program for data scan control at the REXS and RXES\n"
"endstation of Energy-line Beamline20U2@SSRF**\n"
"\n"
"## Developer\n"
"\n"
"**LiminZhou @SSRF20U**\n"
"\n"
"## Contact Author\n"
"\n"
"Email: zlmturnout@hotmail.com\n"
"\n"
"Github page: *https://github.com/zlmturnout*\n"
"\n"
"## Copyright\n"
"\n"
"Full code are hosted on Github repository: *https://github.com/zlmturnout/REXS_SCANControl*\n"
"\n"
"Copyright (c) 2022 LiminZhou/zlmturnout\n"
"\n"
"Please Contact the Author for Any Usage\n"
"\n"
"## Basic Strategy\n"
"\n"
"1.  python+pyepics+Qt6+matplotlib\n"
"\n"
"## Main Purpose\n"
"\n"
"1.  control motor move in X-ray diffractometer\n"
"2.  acquire the PD current to optimize the spectrometer and sample position\n"
"3.  obtain the diffraction patterns by CCD\n"
"4.  Data prepocessed\n"
"5.  save all processed data into multiple file types (xlsx,csv,txt,sqlitebase) \n"
"", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><title>Readme.md</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><a name=\"rexs-scan-control-project\"></a><span style=\" font-size:xx-large; font-weight:700;\">R</span><span style=\" font-size:xx-large; font-weight:700;\">EXS scan control project</span></h1>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"font-colorff5722introductionfont\"></a><span style=\" font-size:x-large; font-weight:700; color:#ff5722;\">I</spa"
                        "n><span style=\" font-size:x-large; font-weight:700; color:#ff5722;\">ntroduction</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">This is a user interface program for data scan control at the REXS and RXES endstation of Energy-line Beamline20U2@SSRF</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"font-colorff3d00developerfont\"></a><span style=\" font-size:x-large; font-weight:700; color:#ff3d00;\">D</span><span style=\" font-size:x-large; font-weight:700; color:#ff3d00;\">eveloper</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#00b8d4;\">LiminZhou @SSRF20U</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><a name=\"font-colorff5722contact-authorfont\"></a><span style=\" font-size:x-large; font-weight:700; color:#ff5722;\">C</span><span style=\" font-size:x-large; font-weight:700; color:#ff5722;\">ontact Author</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email: zlmturnout@hotmail.com</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Github page: <span style=\" font-style:italic;\">https://github.com/zlmturnout</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"font-colorff5722copyrightfont\"></a><span style=\" font-size:x-large; font-weight:700; color:#ff5722;\">C</span><span style=\" font-size:x-large; font-weight:700; color:#ff5722;\">opyright</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Full code are hosted on Github repository: <span style=\" font-style:italic;\">https://github.com/zlmturnout/REXS_SCANControl</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright (c) 2022 LiminZhou/zlmturnout</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00e5ff;\">Please Contact the Author for Any Usage</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"font-color2962ffbasic-strategyfont\"></a><span style=\" font-size:x-large; font-weight:700; color:#2962ff;\">B</span><span style=\" font-size:x-large; font-weight:700; color:#2962ff;\">asic Strategy</span></h2>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right:"
                        " 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">python+pyepics+Qt6+matplotlib</li></ol>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"font-color2962ffmain-purposefont\"></a><span style=\" font-size:x-large; font-weight:700; color:#2962ff;\">M</span><span style=\" font-size:x-large; font-weight:700; color:#2962ff;\">ain Purpose</span></h2>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">control motor move in X-ray diffractometer</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">acquire the PD current to optimize the spectrometer and sample position</li>\n"
""
                        "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">obtain the diffraction patterns by CCD</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Data prepocessed</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">save all processed data into multiple file types (xlsx,csv,txt,sqlitebase) </li></ol></body></html>", None))
    # retranslateUi

