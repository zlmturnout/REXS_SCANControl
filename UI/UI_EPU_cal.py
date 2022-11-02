# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_EPU_cal.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1084, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(39, 110, 550, 250))
        self.groupBox.setMinimumSize(QSize(550, 220))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Show_label_2 = QLabel(self.groupBox)
        self.Show_label_2.setObjectName(u"Show_label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Show_label_2.sizePolicy().hasHeightForWidth())
        self.Show_label_2.setSizePolicy(sizePolicy)
        self.Show_label_2.setMinimumSize(QSize(300, 100))
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.Show_label_2.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(28)
        font.setBold(True)
        self.Show_label_2.setFont(font)
        self.Show_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Show_label_2)

        self.Cal_EPU_btn = QPushButton(self.groupBox)
        self.Cal_EPU_btn.setObjectName(u"Cal_EPU_btn")
        sizePolicy.setHeightForWidth(self.Cal_EPU_btn.sizePolicy().hasHeightForWidth())
        self.Cal_EPU_btn.setSizePolicy(sizePolicy)
        self.Cal_EPU_btn.setMinimumSize(QSize(300, 100))
        self.Cal_EPU_btn.setMaximumSize(QSize(16777215, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.Cal_EPU_btn.setPalette(palette1)
        self.Cal_EPU_btn.setFont(font)
        self.Cal_EPU_btn.setStyleSheet(u"background-color:rgb(0, 170, 255)")

        self.verticalLayout.addWidget(self.Cal_EPU_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.Set_energy = QDoubleSpinBox(self.groupBox)
        self.Set_energy.setObjectName(u"Set_energy")
        sizePolicy.setHeightForWidth(self.Set_energy.sizePolicy().hasHeightForWidth())
        self.Set_energy.setSizePolicy(sizePolicy)
        self.Set_energy.setMinimumSize(QSize(200, 100))
        self.Set_energy.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.Set_energy.setFont(font1)
        self.Set_energy.setStyleSheet(u"color: rgb(255, 0, 127);")
        self.Set_energy.setInputMethodHints(Qt.ImhFormattedNumbersOnly|Qt.ImhNoAutoUppercase|Qt.ImhPreferNumbers)
        self.Set_energy.setAlignment(Qt.AlignCenter)
        self.Set_energy.setDecimals(1)
        self.Set_energy.setMinimum(100.000000000000000)
        self.Set_energy.setMaximum(2000.000000000000000)
        self.Set_energy.setSingleStep(1.000000000000000)
        self.Set_energy.setValue(450.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Set_energy)

        self.EPU_gap_text = QLineEdit(self.groupBox)
        self.EPU_gap_text.setObjectName(u"EPU_gap_text")
        sizePolicy.setHeightForWidth(self.EPU_gap_text.sizePolicy().hasHeightForWidth())
        self.EPU_gap_text.setSizePolicy(sizePolicy)
        self.EPU_gap_text.setMinimumSize(QSize(200, 100))
        self.EPU_gap_text.setMaximumSize(QSize(200, 100))
        palette2 = QPalette()
        brush3 = QBrush(QColor(255, 0, 127, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush4 = QBrush(QColor(255, 0, 127, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.EPU_gap_text.setPalette(palette2)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.EPU_gap_text.setFont(font2)
        self.EPU_gap_text.setAutoFillBackground(False)
        self.EPU_gap_text.setInputMethodHints(Qt.ImhNone)
        self.EPU_gap_text.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.EPU_gap_text)


        self.horizontalLayout.addLayout(self.formLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1084, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Show_label_2.setText(QCoreApplication.translate("MainWindow", u"Energy:", None))
        self.Cal_EPU_btn.setText(QCoreApplication.translate("MainWindow", u"EPU_GAP", None))
#if QT_CONFIG(tooltip)
        self.Set_energy.setToolTip(QCoreApplication.translate("MainWindow", u"Each Step size Z", None))
#endif // QT_CONFIG(tooltip)
        self.Set_energy.setPrefix("")
        self.Set_energy.setSuffix(QCoreApplication.translate("MainWindow", u" eV", None))
        self.EPU_gap_text.setInputMask("")
        self.EPU_gap_text.setText("")
    # retranslateUi

