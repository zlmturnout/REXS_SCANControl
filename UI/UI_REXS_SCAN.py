# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_REXS_SCAN.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMdiArea, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(928, 831)
        self.actionView_data = QAction(MainWindow)
        self.actionView_data.setObjectName(u"actionView_data")
        self.actionDatabase = QAction(MainWindow)
        self.actionDatabase.setObjectName(u"actionDatabase")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Scan_infobox = QGroupBox(self.centralwidget)
        self.Scan_infobox.setObjectName(u"Scan_infobox")
        self.Scan_infobox.setMinimumSize(QSize(600, 125))
        self.gridLayout_3 = QGridLayout(self.Scan_infobox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Open_PD_btn = QPushButton(self.Scan_infobox)
        self.Open_PD_btn.setObjectName(u"Open_PD_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Open_PD_btn.sizePolicy().hasHeightForWidth())
        self.Open_PD_btn.setSizePolicy(sizePolicy)
        self.Open_PD_btn.setMinimumSize(QSize(200, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.Open_PD_btn.setFont(font)
        self.Open_PD_btn.setStyleSheet(u"QPushButton{background-color: rgb(41, 173, 255);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);border-style:inset;border-top-color: rgb(0, 170, 255);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(0, 170, 255);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(0, 170, 255);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.gridLayout_3.addWidget(self.Open_PD_btn, 2, 1, 1, 1)

        self.Channel_cbx = QComboBox(self.Scan_infobox)
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.setObjectName(u"Channel_cbx")
        self.Channel_cbx.setMinimumSize(QSize(100, 40))
        self.Channel_cbx.setMaximumSize(QSize(220, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 85, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(180, 249, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 0, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(240, 240, 240, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 120, 215, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.Channel_cbx.setPalette(palette)
        self.Channel_cbx.setFont(font)
        self.Channel_cbx.setLayoutDirection(Qt.LeftToRight)
        self.Channel_cbx.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.gridLayout_3.addWidget(self.Channel_cbx, 2, 0, 1, 1)

        self.Start_Acqusition_btn = QPushButton(self.Scan_infobox)
        self.Start_Acqusition_btn.setObjectName(u"Start_Acqusition_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Start_Acqusition_btn.sizePolicy().hasHeightForWidth())
        self.Start_Acqusition_btn.setSizePolicy(sizePolicy1)
        self.Start_Acqusition_btn.setMinimumSize(QSize(200, 40))
        self.Start_Acqusition_btn.setMaximumSize(QSize(220, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.Start_Acqusition_btn.setFont(font1)
        self.Start_Acqusition_btn.setStyleSheet(u"QPushButton{background-color: rgb(41, 173, 255);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);border-style:inset;border-top-color: rgb(0, 170, 255);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(0, 170, 255);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(0, 170, 255);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.gridLayout_3.addWidget(self.Start_Acqusition_btn, 0, 1, 1, 1)

        self.Channel_cbx_2 = QComboBox(self.Scan_infobox)
        self.Channel_cbx_2.addItem("")
        self.Channel_cbx_2.addItem("")
        self.Channel_cbx_2.addItem("")
        self.Channel_cbx_2.setObjectName(u"Channel_cbx_2")
        self.Channel_cbx_2.setMinimumSize(QSize(100, 40))
        self.Channel_cbx_2.setMaximumSize(QSize(220, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.Channel_cbx_2.setPalette(palette1)
        self.Channel_cbx_2.setFont(font)
        self.Channel_cbx_2.setLayoutDirection(Qt.LeftToRight)
        self.Channel_cbx_2.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.gridLayout_3.addWidget(self.Channel_cbx_2, 0, 0, 1, 1)

        self.Icon_label = QLabel(self.Scan_infobox)
        self.Icon_label.setObjectName(u"Icon_label")
        sizePolicy.setHeightForWidth(self.Icon_label.sizePolicy().hasHeightForWidth())
        self.Icon_label.setSizePolicy(sizePolicy)
        self.Icon_label.setMinimumSize(QSize(100, 100))

        self.gridLayout_3.addWidget(self.Icon_label, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.Scan_infobox, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(300, 125))
        self.tabWidget.setMaximumSize(QSize(400, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        brush5 = QBrush(QColor(0, 170, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        brush7 = QBrush(QColor(120, 120, 120, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        self.tabWidget.setPalette(palette2)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ADC_TEY_checkBox = QCheckBox(self.tab)
        self.ADC_TEY_checkBox.setObjectName(u"ADC_TEY_checkBox")

        self.horizontalLayout_2.addWidget(self.ADC_TEY_checkBox)

        self.ADC_Au_checkBox = QCheckBox(self.tab)
        self.ADC_Au_checkBox.setObjectName(u"ADC_Au_checkBox")

        self.horizontalLayout_2.addWidget(self.ADC_Au_checkBox)

        self.ADC_PD_checkBox = QCheckBox(self.tab)
        self.ADC_PD_checkBox.setObjectName(u"ADC_PD_checkBox")

        self.horizontalLayout_2.addWidget(self.ADC_PD_checkBox)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pA_TEY_checkBox = QCheckBox(self.tab_2)
        self.pA_TEY_checkBox.setObjectName(u"pA_TEY_checkBox")

        self.horizontalLayout_3.addWidget(self.pA_TEY_checkBox)

        self.pA_Au_checkBox = QCheckBox(self.tab_2)
        self.pA_Au_checkBox.setObjectName(u"pA_Au_checkBox")

        self.horizontalLayout_3.addWidget(self.pA_Au_checkBox)

        self.pA_PD_checkBox = QCheckBox(self.tab_2)
        self.pA_PD_checkBox.setObjectName(u"pA_PD_checkBox")

        self.horizontalLayout_3.addWidget(self.pA_PD_checkBox)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.Main_fig_box = QGroupBox(self.centralwidget)
        self.Main_fig_box.setObjectName(u"Main_fig_box")
        self.Main_fig_box.setMinimumSize(QSize(600, 400))
        self.Main_fig_box.setCursor(QCursor(Qt.CrossCursor))

        self.gridLayout_5.addWidget(self.Main_fig_box, 1, 0, 1, 1)

        self.Monitor_MDI = QMdiArea(self.centralwidget)
        self.Monitor_MDI.setObjectName(u"Monitor_MDI")
        self.Monitor_MDI.setMinimumSize(QSize(300, 400))
        self.Monitor_MDI.setMaximumSize(QSize(400, 16777215))
        self.Monitor_MDI.setStyleSheet(u"")
        self.Monitor_MDI.setFrameShape(QFrame.Box)
        self.Monitor_MDI.setFrameShadow(QFrame.Sunken)
        brush8 = QBrush(QColor(76, 200, 231, 255))
        brush8.setStyle(Qt.Dense4Pattern)
        self.Monitor_MDI.setBackground(brush8)
        self.Monitor_MDI.setViewMode(QMdiArea.SubWindowView)
        self.Monitor_MDI.setDocumentMode(True)
        self.Monitor_MDI.setTabsMovable(False)
        self.Monitor_MDI.setTabShape(QTabWidget.Rounded)

        self.gridLayout_5.addWidget(self.Monitor_MDI, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Scan_set_Box = QGroupBox(self.centralwidget)
        self.Scan_set_Box.setObjectName(u"Scan_set_Box")
        self.Scan_set_Box.setMinimumSize(QSize(600, 120))
        self.gridLayout_4 = QGridLayout(self.Scan_set_Box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Start_scan_btn = QPushButton(self.Scan_set_Box)
        self.Start_scan_btn.setObjectName(u"Start_scan_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Start_scan_btn.sizePolicy().hasHeightForWidth())
        self.Start_scan_btn.setSizePolicy(sizePolicy2)
        self.Start_scan_btn.setMinimumSize(QSize(120, 50))
        palette3 = QPalette()
        brush9 = QBrush(QColor(255, 88, 152, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        brush10 = QBrush(QColor(49, 234, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush10)
        brush11 = QBrush(QColor(255, 255, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        brush12 = QBrush(QColor(127, 127, 127, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush12)
        brush13 = QBrush(QColor(170, 170, 170, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush14 = QBrush(QColor(208, 113, 87, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush14)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush15 = QBrush(QColor(85, 170, 255, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.Start_scan_btn.setPalette(palette3)
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

        self.gridLayout_4.addWidget(self.Start_scan_btn, 0, 0, 1, 1)

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

        self.gridLayout_4.addWidget(self.Stop_scan_btm, 0, 1, 1, 1)

        self.Clear_Save_btn = QPushButton(self.Scan_set_Box)
        self.Clear_Save_btn.setObjectName(u"Clear_Save_btn")
        sizePolicy2.setHeightForWidth(self.Clear_Save_btn.sizePolicy().hasHeightForWidth())
        self.Clear_Save_btn.setSizePolicy(sizePolicy2)
        self.Clear_Save_btn.setMinimumSize(QSize(120, 50))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Active, QPalette.HighlightedText, brush14)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.Clear_Save_btn.setPalette(palette4)
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

        self.gridLayout_4.addWidget(self.Clear_Save_btn, 0, 2, 1, 1)

        self.Calculate_btn = QPushButton(self.Scan_set_Box)
        self.Calculate_btn.setObjectName(u"Calculate_btn")
        sizePolicy2.setHeightForWidth(self.Calculate_btn.sizePolicy().hasHeightForWidth())
        self.Calculate_btn.setSizePolicy(sizePolicy2)
        self.Calculate_btn.setMinimumSize(QSize(120, 50))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Active, QPalette.HighlightedText, brush14)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.Calculate_btn.setPalette(palette5)
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

        self.gridLayout_4.addWidget(self.Calculate_btn, 0, 3, 1, 1)


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
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        brush16 = QBrush(QColor(44, 213, 196, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.Now_time.setPalette(palette6)
        self.Now_time.setFont(font1)
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
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.Done_time.setPalette(palette7)
        self.Done_time.setFont(font1)
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
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.Cost_time.setPalette(palette8)
        self.Cost_time.setFont(font1)
        self.Cost_time.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Cost_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Cost_time)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_5.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.info_textbox = QTextEdit(self.centralwidget)
        self.info_textbox.setObjectName(u"info_textbox")
        self.info_textbox.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.info_textbox.sizePolicy().hasHeightForWidth())
        self.info_textbox.setSizePolicy(sizePolicy4)
        self.info_textbox.setMinimumSize(QSize(100, 100))
        self.info_textbox.setMaximumSize(QSize(400, 300))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        self.info_textbox.setPalette(palette9)
        font3 = QFont()
        font3.setFamilies([u"Cambria Math"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.info_textbox.setFont(font3)
        self.info_textbox.setAcceptDrops(True)
        self.info_textbox.setReadOnly(True)

        self.gridLayout_5.addWidget(self.info_textbox, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 928, 28))
        self.menubar.setFont(font1)
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setFont(font)
        self.menuAnalysis = QMenu(self.menubar)
        self.menuAnalysis.setObjectName(u"menuAnalysis")
        self.menuAnalysis.setFont(font)
        self.menuInstrument = QMenu(self.menubar)
        self.menuInstrument.setObjectName(u"menuInstrument")
        self.menuInstrument.setFont(font)
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        self.menuhelp.setFont(font)
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

        self.tabWidget.setCurrentIndex(0)
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
        self.Open_PD_btn.setText(QCoreApplication.translate("MainWindow", u"Set Range", None))
        self.Channel_cbx.setItemText(0, QCoreApplication.translate("MainWindow", u"Ch3_X", None))
        self.Channel_cbx.setItemText(1, QCoreApplication.translate("MainWindow", u"Ch4_Y", None))
        self.Channel_cbx.setItemText(2, QCoreApplication.translate("MainWindow", u"Ch5_Z", None))

#if QT_CONFIG(tooltip)
        self.Start_Acqusition_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect Electrometer6514", None))
#endif // QT_CONFIG(tooltip)
        self.Start_Acqusition_btn.setText(QCoreApplication.translate("MainWindow", u"Start Acqusition", None))
        self.Channel_cbx_2.setItemText(0, QCoreApplication.translate("MainWindow", u"REXS_\u6563\u5c04\u7ad9", None))
        self.Channel_cbx_2.setItemText(1, QCoreApplication.translate("MainWindow", u"RXES_\u53d1\u5c04\u8c31\u7ad9", None))
        self.Channel_cbx_2.setItemText(2, QCoreApplication.translate("MainWindow", u"O-REXS_\u6709\u673a\u6563\u5c04", None))

        self.Icon_label.setText("")
        self.ADC_TEY_checkBox.setText(QCoreApplication.translate("MainWindow", u"TEY_V", None))
        self.ADC_Au_checkBox.setText(QCoreApplication.translate("MainWindow", u"Au_V", None))
        self.ADC_PD_checkBox.setText(QCoreApplication.translate("MainWindow", u"PD_V", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"ADC_DAQ", None))
        self.pA_TEY_checkBox.setText(QCoreApplication.translate("MainWindow", u"TEY_I", None))
        self.pA_Au_checkBox.setText(QCoreApplication.translate("MainWindow", u"Au_I", None))
        self.pA_PD_checkBox.setText(QCoreApplication.translate("MainWindow", u"PD_I", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"pAmeter", None))
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
"</style></head><body style=\" font-family:'Cambria Math'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; font-size:16pt; font-weight:700;\"><br /></p></body></html>", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuAnalysis.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.menuInstrument.setTitle(QCoreApplication.translate("MainWindow", u"Instrument", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

