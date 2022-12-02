# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_PV_monitor.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 588)
        Form.setMinimumSize(QSize(500, 300))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PV_name_label = QLabel(Form)
        self.PV_name_label.setObjectName(u"PV_name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PV_name_label.sizePolicy().hasHeightForWidth())
        self.PV_name_label.setSizePolicy(sizePolicy)
        self.PV_name_label.setMinimumSize(QSize(100, 40))
        self.PV_name_label.setMaximumSize(QSize(3160, 40))
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
        self.PV_name_label.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.PV_name_label.setFont(font)
        self.PV_name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.PV_name_label)

        self.verticalLayout_plot = QVBoxLayout()
        self.verticalLayout_plot.setObjectName(u"verticalLayout_plot")

        self.verticalLayout.addLayout(self.verticalLayout_plot)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PV_name_label_2 = QLabel(Form)
        self.PV_name_label_2.setObjectName(u"PV_name_label_2")
        sizePolicy.setHeightForWidth(self.PV_name_label_2.sizePolicy().hasHeightForWidth())
        self.PV_name_label_2.setSizePolicy(sizePolicy)
        self.PV_name_label_2.setMinimumSize(QSize(100, 25))
        self.PV_name_label_2.setMaximumSize(QSize(100, 40))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(255, 85, 0, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        brush7 = QBrush(QColor(255, 85, 0, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        brush8 = QBrush(QColor(255, 85, 0, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.PV_name_label_2.setPalette(palette1)
        self.PV_name_label_2.setFont(font)
        self.PV_name_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.PV_name_label_2)

        self.PV_name_label_3 = QLabel(Form)
        self.PV_name_label_3.setObjectName(u"PV_name_label_3")
        sizePolicy.setHeightForWidth(self.PV_name_label_3.sizePolicy().hasHeightForWidth())
        self.PV_name_label_3.setSizePolicy(sizePolicy)
        self.PV_name_label_3.setMinimumSize(QSize(100, 25))
        self.PV_name_label_3.setMaximumSize(QSize(100, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(255, 85, 0, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        brush10 = QBrush(QColor(255, 85, 0, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        brush11 = QBrush(QColor(255, 85, 0, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.PV_name_label_3.setPalette(palette2)
        self.PV_name_label_3.setFont(font)
        self.PV_name_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.PV_name_label_3)

        self.Time_stamp_label = QLabel(Form)
        self.Time_stamp_label.setObjectName(u"Time_stamp_label")
        sizePolicy.setHeightForWidth(self.Time_stamp_label.sizePolicy().hasHeightForWidth())
        self.Time_stamp_label.setSizePolicy(sizePolicy)
        self.Time_stamp_label.setMinimumSize(QSize(200, 25))
        self.Time_stamp_label.setMaximumSize(QSize(3160, 20))
        palette3 = QPalette()
        brush12 = QBrush(QColor(0, 170, 255, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush13 = QBrush(QColor(255, 85, 0, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        brush14 = QBrush(QColor(255, 85, 0, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        brush15 = QBrush(QColor(255, 85, 0, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.Time_stamp_label.setPalette(palette3)
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.Time_stamp_label.setFont(font1)
        self.Time_stamp_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.Time_stamp_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PV_value_input = QLineEdit(Form)
        self.PV_value_input.setObjectName(u"PV_value_input")
        self.PV_value_input.setMinimumSize(QSize(100, 30))
        self.PV_value_input.setMaximumSize(QSize(100, 30))
        palette4 = QPalette()
        brush16 = QBrush(QColor(255, 100, 11, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush16)
        brush17 = QBrush(QColor(255, 100, 11, 128))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        brush18 = QBrush(QColor(0, 0, 0, 128))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.PV_value_input.setPalette(palette4)
        self.PV_value_input.setFont(font)
        self.PV_value_input.setAlignment(Qt.AlignCenter)
        self.PV_value_input.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.PV_value_input)

        self.Y_change_cbx = QComboBox(Form)
        self.Y_change_cbx.addItem("")
        self.Y_change_cbx.addItem("")
        self.Y_change_cbx.setObjectName(u"Y_change_cbx")
        self.Y_change_cbx.setMinimumSize(QSize(100, 30))
        self.Y_change_cbx.setMaximumSize(QSize(16777215, 25))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        self.Y_change_cbx.setPalette(palette5)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.Y_change_cbx.setFont(font2)

        self.horizontalLayout_2.addWidget(self.Y_change_cbx)

        self.Start_monitor_btn = QPushButton(Form)
        self.Start_monitor_btn.setObjectName(u"Start_monitor_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Start_monitor_btn.sizePolicy().hasHeightForWidth())
        self.Start_monitor_btn.setSizePolicy(sizePolicy1)
        self.Start_monitor_btn.setMinimumSize(QSize(80, 40))
        self.Start_monitor_btn.setMaximumSize(QSize(100, 40))
        self.Start_monitor_btn.setFont(font1)
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
        self.Stop_monitor_btn.setFont(font1)
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
        self.Savedata_btn.setFont(font1)
        self.Savedata_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_2.addWidget(self.Savedata_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PV_name_label.setText(QCoreApplication.translate("Form", u"PV name", None))
        self.PV_name_label_2.setText(QCoreApplication.translate("Form", u"Value", None))
        self.PV_name_label_3.setText(QCoreApplication.translate("Form", u"Change", None))
        self.Time_stamp_label.setText(QCoreApplication.translate("Form", u"Timestamp", None))
        self.PV_value_input.setText(QCoreApplication.translate("Form", u"0", None))
        self.Y_change_cbx.setItemText(0, QCoreApplication.translate("Form", u"Num", None))
        self.Y_change_cbx.setItemText(1, QCoreApplication.translate("Form", u"Timestamp", None))

        self.Start_monitor_btn.setText(QCoreApplication.translate("Form", u"Start", None))
        self.Stop_monitor_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.Savedata_btn.setText(QCoreApplication.translate("Form", u"SaveData", None))
    # retranslateUi

