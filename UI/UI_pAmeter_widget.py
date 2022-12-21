# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_pAmeter_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(359, 358)
        Form.setMinimumSize(QSize(300, 300))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_plot = QVBoxLayout()
        self.verticalLayout_plot.setObjectName(u"verticalLayout_plot")

        self.verticalLayout_3.addLayout(self.verticalLayout_plot)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Details_btn = QPushButton(Form)
        self.Details_btn.setObjectName(u"Details_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Details_btn.sizePolicy().hasHeightForWidth())
        self.Details_btn.setSizePolicy(sizePolicy)
        self.Details_btn.setMinimumSize(QSize(50, 30))
        self.Details_btn.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(True)
        self.Details_btn.setFont(font)
        self.Details_btn.setLayoutDirection(Qt.LeftToRight)
        self.Details_btn.setStyleSheet(u"QPushButton{background-color: rgb(76, 207, 255);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")
        self.Details_btn.setAutoDefault(False)
        self.Details_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.Details_btn)

        self.Device_label = QLabel(Form)
        self.Device_label.setObjectName(u"Device_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Device_label.sizePolicy().hasHeightForWidth())
        self.Device_label.setSizePolicy(sizePolicy1)
        self.Device_label.setMinimumSize(QSize(120, 20))
        self.Device_label.setMaximumSize(QSize(3160, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 85, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(255, 85, 0, 128))
        brush1.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        brush3 = QBrush(QColor(255, 85, 0, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        brush5 = QBrush(QColor(255, 85, 0, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Device_label.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.Device_label.setFont(font1)
        self.Device_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Device_label)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(100, 40))
        self.lcdNumber.setMaximumSize(QSize(16777215, 40))
        palette1 = QPalette()
        brush6 = QBrush(QColor(255, 106, 128, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush7 = QBrush(QColor(255, 255, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.lcdNumber.setPalette(palette1)
        self.lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 106, 128);")
        self.lcdNumber.setFrameShape(QFrame.Box)
        self.lcdNumber.setFrameShadow(QFrame.Raised)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setProperty("value", 0.000000000000000)

        self.horizontalLayout_3.addWidget(self.lcdNumber)

        self.Current_label = QLabel(Form)
        self.Current_label.setObjectName(u"Current_label")
        sizePolicy1.setHeightForWidth(self.Current_label.sizePolicy().hasHeightForWidth())
        self.Current_label.setSizePolicy(sizePolicy1)
        self.Current_label.setMinimumSize(QSize(40, 40))
        self.Current_label.setMaximumSize(QSize(3160, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(255, 85, 0, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        brush9 = QBrush(QColor(255, 85, 0, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        brush10 = QBrush(QColor(255, 85, 0, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Current_label.setPalette(palette2)
        self.Current_label.setFont(font1)
        self.Current_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Current_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.Details_box = QGroupBox(Form)
        self.Details_box.setObjectName(u"Details_box")
        self.verticalLayout_2 = QVBoxLayout(self.Details_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ZCHK_rbtn = QRadioButton(self.Details_box)
        self.ZCHK_rbtn.setObjectName(u"ZCHK_rbtn")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.ZCHK_rbtn.setPalette(palette3)
        self.ZCHK_rbtn.setFont(font1)

        self.horizontalLayout.addWidget(self.ZCHK_rbtn)

        self.Unit_label_2 = QLabel(self.Details_box)
        self.Unit_label_2.setObjectName(u"Unit_label_2")
        sizePolicy1.setHeightForWidth(self.Unit_label_2.sizePolicy().hasHeightForWidth())
        self.Unit_label_2.setSizePolicy(sizePolicy1)
        self.Unit_label_2.setMinimumSize(QSize(40, 40))
        self.Unit_label_2.setMaximumSize(QSize(3160, 40))
        palette4 = QPalette()
        brush11 = QBrush(QColor(0, 170, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush12 = QBrush(QColor(255, 85, 0, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        brush13 = QBrush(QColor(0, 0, 0, 128))
        brush13.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.Unit_label_2.setPalette(palette4)
        self.Unit_label_2.setFont(font1)
        self.Unit_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Unit_label_2)

        self.NPLC_cbx = QComboBox(self.Details_box)
        self.NPLC_cbx.addItem("")
        self.NPLC_cbx.addItem("")
        self.NPLC_cbx.addItem("")
        self.NPLC_cbx.addItem("")
        self.NPLC_cbx.addItem("")
        self.NPLC_cbx.setObjectName(u"NPLC_cbx")
        self.NPLC_cbx.setMinimumSize(QSize(95, 40))
        self.NPLC_cbx.setMaximumSize(QSize(120, 40))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        self.NPLC_cbx.setPalette(palette5)
        self.NPLC_cbx.setFont(font1)
        self.NPLC_cbx.setToolTipDuration(5000)
        self.NPLC_cbx.setEditable(False)

        self.horizontalLayout.addWidget(self.NPLC_cbx)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Start_monitor_btn = QPushButton(self.Details_box)
        self.Start_monitor_btn.setObjectName(u"Start_monitor_btn")
        sizePolicy.setHeightForWidth(self.Start_monitor_btn.sizePolicy().hasHeightForWidth())
        self.Start_monitor_btn.setSizePolicy(sizePolicy)
        self.Start_monitor_btn.setMinimumSize(QSize(80, 40))
        self.Start_monitor_btn.setMaximumSize(QSize(100, 40))
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.Start_monitor_btn.setFont(font2)
        self.Start_monitor_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_2.addWidget(self.Start_monitor_btn)

        self.Stop_monitor_btn = QPushButton(self.Details_box)
        self.Stop_monitor_btn.setObjectName(u"Stop_monitor_btn")
        sizePolicy.setHeightForWidth(self.Stop_monitor_btn.sizePolicy().hasHeightForWidth())
        self.Stop_monitor_btn.setSizePolicy(sizePolicy)
        self.Stop_monitor_btn.setMinimumSize(QSize(80, 40))
        self.Stop_monitor_btn.setMaximumSize(QSize(100, 40))
        self.Stop_monitor_btn.setFont(font2)
        self.Stop_monitor_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_2.addWidget(self.Stop_monitor_btn)

        self.Savedata_btn = QPushButton(self.Details_box)
        self.Savedata_btn.setObjectName(u"Savedata_btn")
        sizePolicy.setHeightForWidth(self.Savedata_btn.sizePolicy().hasHeightForWidth())
        self.Savedata_btn.setSizePolicy(sizePolicy)
        self.Savedata_btn.setMinimumSize(QSize(80, 40))
        self.Savedata_btn.setMaximumSize(QSize(100, 40))
        self.Savedata_btn.setFont(font2)
        self.Savedata_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_2.addWidget(self.Savedata_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.Details_box)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.Details_btn.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Details_btn.setText(QCoreApplication.translate("Form", u">--<", None))
        self.Device_label.setText(QCoreApplication.translate("Form", u"Device name", None))
        self.Current_label.setText(QCoreApplication.translate("Form", u"pA", None))
        self.Details_box.setTitle(QCoreApplication.translate("Form", u"ControlPannel", None))
        self.ZCHK_rbtn.setText(QCoreApplication.translate("Form", u"ZeroCheck", None))
        self.Unit_label_2.setText(QCoreApplication.translate("Form", u"Speed:", None))
        self.NPLC_cbx.setItemText(0, QCoreApplication.translate("Form", u"Fastest", None))
        self.NPLC_cbx.setItemText(1, QCoreApplication.translate("Form", u"fast", None))
        self.NPLC_cbx.setItemText(2, QCoreApplication.translate("Form", u"normal", None))
        self.NPLC_cbx.setItemText(3, QCoreApplication.translate("Form", u"slow", None))
        self.NPLC_cbx.setItemText(4, QCoreApplication.translate("Form", u"slowest", None))

#if QT_CONFIG(tooltip)
        self.NPLC_cbx.setToolTip(QCoreApplication.translate("Form", u"set ADC volts", None))
#endif // QT_CONFIG(tooltip)
        self.NPLC_cbx.setPlaceholderText("")
        self.Start_monitor_btn.setText(QCoreApplication.translate("Form", u"Start", None))
        self.Stop_monitor_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.Savedata_btn.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

