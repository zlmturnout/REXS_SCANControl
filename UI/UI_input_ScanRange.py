# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_input_ScanRange.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 600)
        Dialog.setMinimumSize(QSize(900, 600))
        Dialog.setMaximumSize(QSize(2160, 16777215))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Scan_label = QLabel(Dialog)
        self.Scan_label.setObjectName(u"Scan_label")
        self.Scan_label.setMinimumSize(QSize(300, 50))
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
        self.Scan_label.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(True)
        self.Scan_label.setFont(font)
        self.Scan_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Scan_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(330, 200))
        self.tableWidget.setMaximumSize(QSize(1000, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.tableWidget.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.tableWidget.setFont(font1)
        self.tableWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setInputMethodHints(Qt.ImhNone)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setLineWidth(20)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setCornerButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Add_row_btn = QPushButton(Dialog)
        self.Add_row_btn.setObjectName(u"Add_row_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Add_row_btn.sizePolicy().hasHeightForWidth())
        self.Add_row_btn.setSizePolicy(sizePolicy)
        self.Add_row_btn.setMinimumSize(QSize(120, 60))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.Add_row_btn.setFont(font2)
        self.Add_row_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Add_row_btn)

        self.Del_row_btn = QPushButton(Dialog)
        self.Del_row_btn.setObjectName(u"Del_row_btn")
        sizePolicy.setHeightForWidth(self.Del_row_btn.sizePolicy().hasHeightForWidth())
        self.Del_row_btn.setSizePolicy(sizePolicy)
        self.Del_row_btn.setMinimumSize(QSize(120, 60))
        self.Del_row_btn.setFont(font2)
        self.Del_row_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Del_row_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(150, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_2.setPalette(palette2)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.Note_text = QPlainTextEdit(Dialog)
        self.Note_text.setObjectName(u"Note_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Note_text.sizePolicy().hasHeightForWidth())
        self.Note_text.setSizePolicy(sizePolicy2)
        self.Note_text.setMinimumSize(QSize(100, 200))
        self.Note_text.setMaximumSize(QSize(1000, 16777215))
        palette3 = QPalette()
        brush5 = QBrush(QColor(224, 70, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush5)
        brush6 = QBrush(QColor(224, 70, 255, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Note_text.setPalette(palette3)
        self.Note_text.setFont(font3)
        self.Note_text.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.Note_text)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Confirm_btn = QPushButton(Dialog)
        self.Confirm_btn.setObjectName(u"Confirm_btn")
        sizePolicy.setHeightForWidth(self.Confirm_btn.sizePolicy().hasHeightForWidth())
        self.Confirm_btn.setSizePolicy(sizePolicy)
        self.Confirm_btn.setMinimumSize(QSize(90, 40))
        self.Confirm_btn.setFont(font2)
        self.Confirm_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.Confirm_btn)

        self.Cancel_btn = QPushButton(Dialog)
        self.Cancel_btn.setObjectName(u"Cancel_btn")
        sizePolicy.setHeightForWidth(self.Cancel_btn.sizePolicy().hasHeightForWidth())
        self.Cancel_btn.setSizePolicy(sizePolicy)
        self.Cancel_btn.setMinimumSize(QSize(90, 40))
        self.Cancel_btn.setFont(font2)
        self.Cancel_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.Cancel_btn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Scan_label.setText(QCoreApplication.translate("Dialog", u">>>>>>>>>>Input scan range info<<<<<<<<<<", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Min", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Max", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Step", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"1", None));
        self.Add_row_btn.setText(QCoreApplication.translate("Dialog", u"Add row", None))
        self.Del_row_btn.setText(QCoreApplication.translate("Dialog", u"Delete row", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Input Note", None))
        self.Note_text.setPlainText(QCoreApplication.translate("Dialog", u"Example:\n"
"      Min  Max  Step\n"
"1    1.0   2.0    0.2\n"
"2    2.5   5.0    0.5\n"
"3    5.3   8.3    0.3\n"
"....\n"
"\n"
"", None))
        self.Confirm_btn.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.Cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

