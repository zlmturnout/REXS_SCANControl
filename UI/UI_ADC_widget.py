# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_ADC_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 350)
        Form.setMinimumSize(QSize(350, 350))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Device_label = QLabel(Form)
        self.Device_label.setObjectName(u"Device_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Device_label.sizePolicy().hasHeightForWidth())
        self.Device_label.setSizePolicy(sizePolicy)
        self.Device_label.setMinimumSize(QSize(251, 40))
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
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.Device_label.setFont(font)
        self.Device_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Device_label)

        self.verticalLayout_plot = QVBoxLayout()
        self.verticalLayout_plot.setObjectName(u"verticalLayout_plot")

        self.verticalLayout_2.addLayout(self.verticalLayout_plot)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Channel_cbx = QComboBox(Form)
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.setObjectName(u"Channel_cbx")
        self.Channel_cbx.setMinimumSize(QSize(120, 40))
        self.Channel_cbx.setMaximumSize(QSize(120, 40))
        palette1 = QPalette()
        brush6 = QBrush(QColor(0, 170, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        self.Channel_cbx.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.Channel_cbx.setFont(font1)
        self.Channel_cbx.setToolTipDuration(5000)

        self.horizontalLayout.addWidget(self.Channel_cbx)

        self.Range_cbx = QComboBox(Form)
        self.Range_cbx.addItem("")
        self.Range_cbx.addItem("")
        self.Range_cbx.addItem("")
        self.Range_cbx.addItem("")
        self.Range_cbx.setObjectName(u"Range_cbx")
        self.Range_cbx.setMinimumSize(QSize(120, 40))
        self.Range_cbx.setMaximumSize(QSize(120, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        self.Range_cbx.setPalette(palette2)
        self.Range_cbx.setFont(font)
        self.Range_cbx.setToolTipDuration(5000)
        self.Range_cbx.setEditable(False)

        self.horizontalLayout.addWidget(self.Range_cbx)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Start_monitor_btn = QPushButton(Form)
        self.Start_monitor_btn.setObjectName(u"Start_monitor_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Start_monitor_btn.sizePolicy().hasHeightForWidth())
        self.Start_monitor_btn.setSizePolicy(sizePolicy1)
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

        self.Stop_monitor_btn = QPushButton(Form)
        self.Stop_monitor_btn.setObjectName(u"Stop_monitor_btn")
        sizePolicy1.setHeightForWidth(self.Stop_monitor_btn.sizePolicy().hasHeightForWidth())
        self.Stop_monitor_btn.setSizePolicy(sizePolicy1)
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

        self.Savedata_btn = QPushButton(Form)
        self.Savedata_btn.setObjectName(u"Savedata_btn")
        sizePolicy1.setHeightForWidth(self.Savedata_btn.sizePolicy().hasHeightForWidth())
        self.Savedata_btn.setSizePolicy(sizePolicy1)
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


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Device_label.setText(QCoreApplication.translate("Form", u"Device name", None))
        self.Channel_cbx.setItemText(0, QCoreApplication.translate("Form", u"CH0", None))
        self.Channel_cbx.setItemText(1, QCoreApplication.translate("Form", u"CH1", None))
        self.Channel_cbx.setItemText(2, QCoreApplication.translate("Form", u"CH2", None))
        self.Channel_cbx.setItemText(3, QCoreApplication.translate("Form", u"CH3", None))

#if QT_CONFIG(tooltip)
        self.Channel_cbx.setToolTip(QCoreApplication.translate("Form", u"Set ADC Channel", None))
#endif // QT_CONFIG(tooltip)
        self.Channel_cbx.setPlaceholderText("")
        self.Range_cbx.setItemText(0, QCoreApplication.translate("Form", u"+/-  1V", None))
        self.Range_cbx.setItemText(1, QCoreApplication.translate("Form", u"+/-  2V", None))
        self.Range_cbx.setItemText(2, QCoreApplication.translate("Form", u"+/-  5V", None))
        self.Range_cbx.setItemText(3, QCoreApplication.translate("Form", u"+/-  10V", None))

#if QT_CONFIG(tooltip)
        self.Range_cbx.setToolTip(QCoreApplication.translate("Form", u"set ADC volts", None))
#endif // QT_CONFIG(tooltip)
        self.Range_cbx.setPlaceholderText("")
        self.Start_monitor_btn.setText(QCoreApplication.translate("Form", u"Start", None))
        self.Stop_monitor_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.Savedata_btn.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

