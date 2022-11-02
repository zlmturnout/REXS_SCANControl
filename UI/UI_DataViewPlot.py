# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_DataViewPlot.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1400, 800)
        Dialog.setMinimumSize(QSize(1200, 800))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.View_label = QLabel(Dialog)
        self.View_label.setObjectName(u"View_label")
        self.View_label.setMinimumSize(QSize(300, 50))
        palette = QPalette()
        brush = QBrush(QColor(227, 76, 114, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(0, 170, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.View_label.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(True)
        self.View_label.setFont(font)
        self.View_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.View_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Import_btn = QPushButton(Dialog)
        self.Import_btn.setObjectName(u"Import_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Import_btn.sizePolicy().hasHeightForWidth())
        self.Import_btn.setSizePolicy(sizePolicy)
        self.Import_btn.setMinimumSize(QSize(120, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.Import_btn.setFont(font1)
        self.Import_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.Import_btn)

        self.Export_btn = QPushButton(Dialog)
        self.Export_btn.setObjectName(u"Export_btn")
        sizePolicy.setHeightForWidth(self.Export_btn.sizePolicy().hasHeightForWidth())
        self.Export_btn.setSizePolicy(sizePolicy)
        self.Export_btn.setMinimumSize(QSize(120, 40))
        self.Export_btn.setFont(font1)
        self.Export_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.Export_btn)

        self.horizontalSpacer = QSpacerItem(338, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 40))
        palette1 = QPalette()
        brush5 = QBrush(QColor(255, 85, 127, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush5)
        brush6 = QBrush(QColor(255, 85, 127, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_2.setPalette(palette1)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.Select_X_axis = QComboBox(Dialog)
        self.Select_X_axis.setObjectName(u"Select_X_axis")
        self.Select_X_axis.setMinimumSize(QSize(150, 40))
        self.Select_X_axis.setFont(font1)
        self.Select_X_axis.setLayoutDirection(Qt.LeftToRight)
        self.Select_X_axis.setStyleSheet(u"background-color:  rgb(33, 190, 193);\n"
"color: rgb(255, 85, 127);\n"
"selection-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(28, 255, 247);\n"
"border-color: rgb(255, 0, 127);")
        self.Select_X_axis.setInsertPolicy(QComboBox.InsertAtBottom)

        self.horizontalLayout.addWidget(self.Select_X_axis)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label.setPalette(palette2)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.Select_Y_axis = QComboBox(Dialog)
        self.Select_Y_axis.setObjectName(u"Select_Y_axis")
        self.Select_Y_axis.setMinimumSize(QSize(150, 40))
        self.Select_Y_axis.setFont(font1)
        self.Select_Y_axis.setStyleSheet(u"background-color:  rgb(33, 190, 193);\n"
"color: rgb(255, 85, 127);\n"
"selection-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(7, 197, 255);\n"
"border-color: rgb(255, 0, 127);")

        self.horizontalLayout.addWidget(self.Select_Y_axis)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableView = QTableView(Dialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(400, 300))

        self.horizontalLayout_3.addWidget(self.tableView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Plot_data_btn = QPushButton(Dialog)
        self.Plot_data_btn.setObjectName(u"Plot_data_btn")
        sizePolicy.setHeightForWidth(self.Plot_data_btn.sizePolicy().hasHeightForWidth())
        self.Plot_data_btn.setSizePolicy(sizePolicy)
        self.Plot_data_btn.setMinimumSize(QSize(125, 60))
        self.Plot_data_btn.setFont(font1)
        self.Plot_data_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Plot_data_btn)

        self.Update_data_btn = QPushButton(Dialog)
        self.Update_data_btn.setObjectName(u"Update_data_btn")
        sizePolicy.setHeightForWidth(self.Update_data_btn.sizePolicy().hasHeightForWidth())
        self.Update_data_btn.setSizePolicy(sizePolicy)
        self.Update_data_btn.setMinimumSize(QSize(125, 60))
        self.Update_data_btn.setFont(font1)
        self.Update_data_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Update_data_btn)

        self.verticalSpacer = QSpacerItem(20, 238, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Derivative_btn = QPushButton(Dialog)
        self.Derivative_btn.setObjectName(u"Derivative_btn")
        sizePolicy.setHeightForWidth(self.Derivative_btn.sizePolicy().hasHeightForWidth())
        self.Derivative_btn.setSizePolicy(sizePolicy)
        self.Derivative_btn.setMinimumSize(QSize(125, 60))
        self.Derivative_btn.setFont(font1)
        self.Derivative_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Derivative_btn)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.Plot_box = QGroupBox(Dialog)
        self.Plot_box.setObjectName(u"Plot_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Plot_box.sizePolicy().hasHeightForWidth())
        self.Plot_box.setSizePolicy(sizePolicy1)
        self.Plot_box.setMinimumSize(QSize(450, 420))

        self.horizontalLayout_3.addWidget(self.Plot_box)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(448, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.Close_btn = QPushButton(Dialog)
        self.Close_btn.setObjectName(u"Close_btn")
        sizePolicy.setHeightForWidth(self.Close_btn.sizePolicy().hasHeightForWidth())
        self.Close_btn.setSizePolicy(sizePolicy)
        self.Close_btn.setMinimumSize(QSize(90, 40))
        self.Close_btn.setFont(font1)
        self.Close_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.Close_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.View_label.setText(QCoreApplication.translate("Dialog", u">>>>>>>>>>View scan data<<<<<<<<<<", None))
        self.Import_btn.setText(QCoreApplication.translate("Dialog", u"import data", None))
        self.Export_btn.setText(QCoreApplication.translate("Dialog", u"Export data", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"X axis", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Y axis", None))
        self.Plot_data_btn.setText(QCoreApplication.translate("Dialog", u"Plot data", None))
        self.Update_data_btn.setText(QCoreApplication.translate("Dialog", u"Update data", None))
        self.Derivative_btn.setText(QCoreApplication.translate("Dialog", u" Derivative", None))
        self.Plot_box.setTitle(QCoreApplication.translate("Dialog", u"Plot", None))
        self.Close_btn.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

