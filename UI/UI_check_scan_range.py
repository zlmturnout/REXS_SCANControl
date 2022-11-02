# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_check_scan_range.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(888, 538)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(100, 280, 561, 51))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 290, 321, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_4.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(90, 20, 500, 251))
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.X_axis_usage = QLabel(self.groupBox)
        self.X_axis_usage.setObjectName(u"X_axis_usage")
        sizePolicy.setHeightForWidth(self.X_axis_usage.sizePolicy().hasHeightForWidth())
        self.X_axis_usage.setSizePolicy(sizePolicy)
        self.X_axis_usage.setMinimumSize(QSize(300, 40))
        palette1 = QPalette()
        brush2 = QBrush(QColor(255, 85, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush3 = QBrush(QColor(255, 85, 0, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.X_axis_usage.setPalette(palette1)
        self.X_axis_usage.setFont(font)
        self.X_axis_usage.setFrameShape(QFrame.WinPanel)

        self.verticalLayout_2.addWidget(self.X_axis_usage)

        self.X_scan_range = QLabel(self.groupBox)
        self.X_scan_range.setObjectName(u"X_scan_range")
        sizePolicy.setHeightForWidth(self.X_scan_range.sizePolicy().hasHeightForWidth())
        self.X_scan_range.setSizePolicy(sizePolicy)
        self.X_scan_range.setMinimumSize(QSize(300, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.X_scan_range.setPalette(palette2)
        self.X_scan_range.setFont(font)
        self.X_scan_range.setFrameShape(QFrame.WinPanel)

        self.verticalLayout_2.addWidget(self.X_scan_range)

        self.Y_axis_usage = QLabel(self.groupBox)
        self.Y_axis_usage.setObjectName(u"Y_axis_usage")
        sizePolicy.setHeightForWidth(self.Y_axis_usage.sizePolicy().hasHeightForWidth())
        self.Y_axis_usage.setSizePolicy(sizePolicy)
        self.Y_axis_usage.setMinimumSize(QSize(300, 40))
        palette3 = QPalette()
        brush5 = QBrush(QColor(0, 170, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Y_axis_usage.setPalette(palette3)
        self.Y_axis_usage.setFont(font)
        self.Y_axis_usage.setFrameShape(QFrame.WinPanel)

        self.verticalLayout_2.addWidget(self.Y_axis_usage)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(120, 40))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_2.setPalette(palette4)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(185, 40))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_6.setPalette(palette5)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(120, 40))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_3.setPalette(palette6)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        palette7 = QPalette()
        brush6 = QBrush(QColor(255, 0, 127, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label.setPalette(palette7)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Press OK to Start scan or Cancel", None))
        self.groupBox.setTitle("")
        self.X_axis_usage.setText("")
        self.X_scan_range.setText("")
        self.Y_axis_usage.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"X >>>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Scan range >>>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Y >>>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Check the scan info:", None))
    # retranslateUi

