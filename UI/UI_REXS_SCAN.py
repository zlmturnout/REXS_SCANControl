# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_REXS_SCAN.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMdiArea, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(934, 798)
        self.actionView_data = QAction(MainWindow)
        self.actionView_data.setObjectName(u"actionView_data")
        self.actionDatabase = QAction(MainWindow)
        self.actionDatabase.setObjectName(u"actionDatabase")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Scan_infobox = QGroupBox(self.centralwidget)
        self.Scan_infobox.setObjectName(u"Scan_infobox")
        self.Scan_infobox.setMinimumSize(QSize(900, 125))
        self.gridLayout_3 = QGridLayout(self.Scan_infobox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.Scan_infobox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 106, 60, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(85, 170, 255, 128))
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
        self.label_5.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_3 = QLabel(self.Scan_infobox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 40))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_3.setPalette(palette1)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.Scan_infobox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_4.setPalette(palette2)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_2 = QLabel(self.Scan_infobox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 40))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_2.setPalette(palette3)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Channel_cbx = QComboBox(self.Scan_infobox)
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.setObjectName(u"Channel_cbx")
        self.Channel_cbx.setMinimumSize(QSize(100, 40))
        self.Channel_cbx.setMaximumSize(QSize(220, 16777215))
        palette4 = QPalette()
        brush5 = QBrush(QColor(255, 85, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        brush6 = QBrush(QColor(180, 249, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush6)
        brush7 = QBrush(QColor(255, 0, 127, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Highlight, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        brush8 = QBrush(QColor(240, 240, 240, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        brush9 = QBrush(QColor(0, 120, 215, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Channel_cbx.setPalette(palette4)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.Channel_cbx.setFont(font1)
        self.Channel_cbx.setLayoutDirection(Qt.LeftToRight)
        self.Channel_cbx.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.gridLayout.addWidget(self.Channel_cbx, 1, 1, 1, 1)

        self.Channel_cbx_2 = QComboBox(self.Scan_infobox)
        self.Channel_cbx_2.addItem("")
        self.Channel_cbx_2.addItem("")
        self.Channel_cbx_2.addItem("")
        self.Channel_cbx_2.setObjectName(u"Channel_cbx_2")
        self.Channel_cbx_2.setMinimumSize(QSize(100, 40))
        self.Channel_cbx_2.setMaximumSize(QSize(220, 16777215))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Highlight, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Channel_cbx_2.setPalette(palette5)
        self.Channel_cbx_2.setFont(font1)
        self.Channel_cbx_2.setLayoutDirection(Qt.LeftToRight)
        self.Channel_cbx_2.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.gridLayout.addWidget(self.Channel_cbx_2, 1, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 2, 1)

        self.Connect_PVs_btn = QPushButton(self.Scan_infobox)
        self.Connect_PVs_btn.setObjectName(u"Connect_PVs_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Connect_PVs_btn.sizePolicy().hasHeightForWidth())
        self.Connect_PVs_btn.setSizePolicy(sizePolicy)
        self.Connect_PVs_btn.setMinimumSize(QSize(200, 40))
        self.Connect_PVs_btn.setMaximumSize(QSize(220, 16777215))
        self.Connect_PVs_btn.setFont(font)
        self.Connect_PVs_btn.setStyleSheet(u"QPushButton{background-color: rgb(41, 173, 255);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);border-style:inset;border-top-color: rgb(0, 170, 255);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(0, 170, 255);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(0, 170, 255);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.gridLayout_3.addWidget(self.Connect_PVs_btn, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(299, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 2, 1)

        self.Icon_label = QLabel(self.Scan_infobox)
        self.Icon_label.setObjectName(u"Icon_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Icon_label.sizePolicy().hasHeightForWidth())
        self.Icon_label.setSizePolicy(sizePolicy1)
        self.Icon_label.setMinimumSize(QSize(100, 100))

        self.gridLayout_3.addWidget(self.Icon_label, 0, 3, 2, 1)

        self.Open_PD_btn = QPushButton(self.Scan_infobox)
        self.Open_PD_btn.setObjectName(u"Open_PD_btn")
        sizePolicy1.setHeightForWidth(self.Open_PD_btn.sizePolicy().hasHeightForWidth())
        self.Open_PD_btn.setSizePolicy(sizePolicy1)
        self.Open_PD_btn.setMinimumSize(QSize(200, 40))
        self.Open_PD_btn.setFont(font1)
        self.Open_PD_btn.setStyleSheet(u"background-color: rgb(41, 173, 255);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Open_PD_btn, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.Scan_infobox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Main_fig_box = QGroupBox(self.centralwidget)
        self.Main_fig_box.setObjectName(u"Main_fig_box")
        self.Main_fig_box.setMinimumSize(QSize(600, 400))
        self.Main_fig_box.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout_2.addWidget(self.Main_fig_box)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Scan_set_Box = QGroupBox(self.centralwidget)
        self.Scan_set_Box.setObjectName(u"Scan_set_Box")
        self.Scan_set_Box.setMinimumSize(QSize(600, 120))
        self.horizontalLayout_3 = QHBoxLayout(self.Scan_set_Box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Start_scan_btn = QPushButton(self.Scan_set_Box)
        self.Start_scan_btn.setObjectName(u"Start_scan_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Start_scan_btn.sizePolicy().hasHeightForWidth())
        self.Start_scan_btn.setSizePolicy(sizePolicy2)
        self.Start_scan_btn.setMinimumSize(QSize(100, 50))
        palette6 = QPalette()
        brush10 = QBrush(QColor(255, 88, 152, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        brush11 = QBrush(QColor(49, 234, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush11)
        brush12 = QBrush(QColor(255, 255, 255, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        brush13 = QBrush(QColor(127, 127, 127, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush13)
        brush14 = QBrush(QColor(170, 170, 170, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush11)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush15)
        brush16 = QBrush(QColor(208, 113, 87, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.HighlightedText, brush16)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush15)
        palette6.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Start_scan_btn.setPalette(palette6)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.Start_scan_btn.setFont(font2)
        self.Start_scan_btn.setFocusPolicy(Qt.ClickFocus)
        self.Start_scan_btn.setStyleSheet(u"QPushButton{background-color: rgb(49, 234, 255);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 88, 152);border-style:inset;border-top-color: rgb(164, 160, 181);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(170, 255, 255);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color:rgb(167, 167, 16"
                        "7);}")
        self.Start_scan_btn.setCheckable(False)
        self.Start_scan_btn.setAutoDefault(False)
        self.Start_scan_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.Start_scan_btn)

        self.Stop_scan_btm = QPushButton(self.Scan_set_Box)
        self.Stop_scan_btm.setObjectName(u"Stop_scan_btm")
        sizePolicy2.setHeightForWidth(self.Stop_scan_btm.sizePolicy().hasHeightForWidth())
        self.Stop_scan_btm.setSizePolicy(sizePolicy2)
        self.Stop_scan_btm.setMinimumSize(QSize(120, 50))
        self.Stop_scan_btm.setFont(font2)
        self.Stop_scan_btm.setFocusPolicy(Qt.WheelFocus)
        self.Stop_scan_btm.setStyleSheet(u"QPushButton{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(164, 160, 181);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(49, 234, 255);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 91, 58) ;border-style:inset;border-top-color: rgb(134, 255, 255);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(255, 255, 255);}\n"
"QPushButton:pressed{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(134, 255, 255);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_3.addWidget(self.Stop_scan_btm)

        self.Clear_Save_btn = QPushButton(self.Scan_set_Box)
        self.Clear_Save_btn.setObjectName(u"Clear_Save_btn")
        sizePolicy2.setHeightForWidth(self.Clear_Save_btn.sizePolicy().hasHeightForWidth())
        self.Clear_Save_btn.setSizePolicy(sizePolicy2)
        self.Clear_Save_btn.setMinimumSize(QSize(120, 50))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush15)
        palette7.setBrush(QPalette.Active, QPalette.HighlightedText, brush16)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush16)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush15)
        palette7.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Clear_Save_btn.setPalette(palette7)
        self.Clear_Save_btn.setFont(font2)
        self.Clear_Save_btn.setFocusPolicy(Qt.ClickFocus)
        self.Clear_Save_btn.setStyleSheet(u"QPushButton{background-color: rgb(49, 234, 255);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 88, 152);border-style:inset;border-top-color: rgb(164, 160, 181);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(170, 255, 255);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color:rgb(167, 167, 16"
                        "7);}")
        self.Clear_Save_btn.setCheckable(False)
        self.Clear_Save_btn.setAutoDefault(False)
        self.Clear_Save_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.Clear_Save_btn)

        self.Calculate_btn = QPushButton(self.Scan_set_Box)
        self.Calculate_btn.setObjectName(u"Calculate_btn")
        sizePolicy2.setHeightForWidth(self.Calculate_btn.sizePolicy().hasHeightForWidth())
        self.Calculate_btn.setSizePolicy(sizePolicy2)
        self.Calculate_btn.setMinimumSize(QSize(120, 50))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush15)
        palette8.setBrush(QPalette.Active, QPalette.HighlightedText, brush16)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush16)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush15)
        palette8.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush16)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Calculate_btn.setPalette(palette8)
        self.Calculate_btn.setFont(font2)
        self.Calculate_btn.setFocusPolicy(Qt.ClickFocus)
        self.Calculate_btn.setStyleSheet(u"QPushButton{background-color: rgb(49, 234, 255);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 88, 152);border-style:inset;border-top-color:rgb(164, 160, 181);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(170, 255, 255);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color:rgb(167, 167, 167"
                        ");}")
        self.Calculate_btn.setCheckable(False)
        self.Calculate_btn.setAutoDefault(False)
        self.Calculate_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.Calculate_btn)


        self.verticalLayout.addWidget(self.Scan_set_Box)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(200, 0))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Now_time = QLabel(self.centralwidget)
        self.Now_time.setObjectName(u"Now_time")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Now_time.sizePolicy().hasHeightForWidth())
        self.Now_time.setSizePolicy(sizePolicy3)
        self.Now_time.setMinimumSize(QSize(190, 30))
        self.Now_time.setMaximumSize(QSize(1000, 40))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        brush17 = QBrush(QColor(44, 213, 196, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.Now_time.setPalette(palette9)
        self.Now_time.setFont(font)
        self.Now_time.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Now_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Now_time)

        self.Done_time = QLabel(self.centralwidget)
        self.Done_time.setObjectName(u"Done_time")
        sizePolicy3.setHeightForWidth(self.Done_time.sizePolicy().hasHeightForWidth())
        self.Done_time.setSizePolicy(sizePolicy3)
        self.Done_time.setMinimumSize(QSize(190, 30))
        self.Done_time.setMaximumSize(QSize(1000, 40))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.Done_time.setPalette(palette10)
        self.Done_time.setFont(font)
        self.Done_time.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Done_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Done_time)

        self.Cost_time = QLabel(self.centralwidget)
        self.Cost_time.setObjectName(u"Cost_time")
        sizePolicy3.setHeightForWidth(self.Cost_time.sizePolicy().hasHeightForWidth())
        self.Cost_time.setSizePolicy(sizePolicy3)
        self.Cost_time.setMinimumSize(QSize(190, 30))
        self.Cost_time.setMaximumSize(QSize(1000, 40))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.Cost_time.setPalette(palette11)
        self.Cost_time.setFont(font)
        self.Cost_time.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Cost_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Cost_time)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Monitor_MDI = QMdiArea(self.centralwidget)
        self.Monitor_MDI.setObjectName(u"Monitor_MDI")
        self.Monitor_MDI.setMinimumSize(QSize(300, 400))
        self.Monitor_MDI.setMaximumSize(QSize(300, 16777215))
        self.Monitor_MDI.setStyleSheet(u"")
        self.Monitor_MDI.setFrameShape(QFrame.Box)
        self.Monitor_MDI.setFrameShadow(QFrame.Sunken)
        brush18 = QBrush(QColor(76, 200, 231, 255))
        brush18.setStyle(Qt.Dense4Pattern)
        self.Monitor_MDI.setBackground(brush18)
        self.Monitor_MDI.setViewMode(QMdiArea.SubWindowView)
        self.Monitor_MDI.setDocumentMode(True)
        self.Monitor_MDI.setTabsMovable(False)
        self.Monitor_MDI.setTabShape(QTabWidget.Rounded)

        self.verticalLayout_3.addWidget(self.Monitor_MDI)

        self.info_textbox = QTextEdit(self.centralwidget)
        self.info_textbox.setObjectName(u"info_textbox")
        self.info_textbox.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.info_textbox.sizePolicy().hasHeightForWidth())
        self.info_textbox.setSizePolicy(sizePolicy4)
        self.info_textbox.setMinimumSize(QSize(100, 100))
        self.info_textbox.setMaximumSize(QSize(300, 300))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.info_textbox.setFont(font3)
        self.info_textbox.setAcceptDrops(True)
        self.info_textbox.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.info_textbox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 934, 28))
        self.menubar.setFont(font)
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setFont(font1)
        self.menuAnalysis = QMenu(self.menubar)
        self.menuAnalysis.setObjectName(u"menuAnalysis")
        self.menuAnalysis.setFont(font1)
        self.menuInstrument = QMenu(self.menubar)
        self.menuInstrument.setObjectName(u"menuInstrument")
        self.menuInstrument.setFont(font1)
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        self.menuhelp.setFont(font1)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuInstrument.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuAnalysis.addAction(self.actionView_data)
        self.menuAnalysis.addAction(self.actionDatabase)

        self.retranslateUi(MainWindow)

        self.Start_scan_btn.setDefault(False)
        self.Clear_Save_btn.setDefault(False)
        self.Calculate_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionView_data.setText(QCoreApplication.translate("MainWindow", u"View_data", None))
        self.actionDatabase.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.Scan_infobox.setTitle(QCoreApplication.translate("MainWindow", u"Scan_info", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.Channel_cbx.setItemText(0, QCoreApplication.translate("MainWindow", u"Ch3_X", None))
        self.Channel_cbx.setItemText(1, QCoreApplication.translate("MainWindow", u"Ch4_Y", None))
        self.Channel_cbx.setItemText(2, QCoreApplication.translate("MainWindow", u"Ch5_Z", None))

        self.Channel_cbx_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Ch3_X", None))
        self.Channel_cbx_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Ch4_Y", None))
        self.Channel_cbx_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Ch5_Z", None))

#if QT_CONFIG(tooltip)
        self.Connect_PVs_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect Electrometer6514", None))
#endif // QT_CONFIG(tooltip)
        self.Connect_PVs_btn.setText(QCoreApplication.translate("MainWindow", u"PMCmotor", None))
        self.Icon_label.setText("")
        self.Open_PD_btn.setText(QCoreApplication.translate("MainWindow", u"Open image", None))
        self.Main_fig_box.setTitle(QCoreApplication.translate("MainWindow", u"MainFigure", None))
        self.Scan_set_Box.setTitle(QCoreApplication.translate("MainWindow", u"Scan_Set", None))
#if QT_CONFIG(tooltip)
        self.Start_scan_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Start_scan_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"begin scan,should choose scan mode and scan range", None))
#endif // QT_CONFIG(statustip)
        self.Start_scan_btn.setText(QCoreApplication.translate("MainWindow", u"Start_Scan", None))
#if QT_CONFIG(tooltip)
        self.Stop_scan_btm.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Stop_scan_btm.setStatusTip(QCoreApplication.translate("MainWindow", u"Stop scan", None))
#endif // QT_CONFIG(statustip)
        self.Stop_scan_btm.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.Clear_Save_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Clear_Save_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"begin scan,should choose scan mode and scan range", None))
#endif // QT_CONFIG(statustip)
        self.Clear_Save_btn.setText(QCoreApplication.translate("MainWindow", u"Clear+Save", None))
#if QT_CONFIG(tooltip)
        self.Calculate_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Calculate_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"begin scan,should choose scan mode and scan range", None))
#endif // QT_CONFIG(statustip)
        self.Calculate_btn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.Now_time.setText("")
        self.Done_time.setText("")
        self.Cost_time.setText("")
        self.info_textbox.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuAnalysis.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.menuInstrument.setTitle(QCoreApplication.translate("MainWindow", u"Instrument", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

