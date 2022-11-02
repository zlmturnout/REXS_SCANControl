# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_my_msg_box.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(420, 334)
        Dialog.setMinimumSize(QSize(400, 300))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Info_box = QLabel(Dialog)
        self.Info_box.setObjectName(u"Info_box")
        self.Info_box.setMinimumSize(QSize(300, 80))
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
        self.Info_box.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(False)
        self.Info_box.setFont(font)
        self.Info_box.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Info_box, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Hide_btn = QPushButton(Dialog)
        self.Hide_btn.setObjectName(u"Hide_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hide_btn.sizePolicy().hasHeightForWidth())
        self.Hide_btn.setSizePolicy(sizePolicy)
        self.Hide_btn.setMinimumSize(QSize(120, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.Hide_btn.setFont(font1)
        self.Hide_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.Hide_btn.setAutoDefault(False)
        self.Hide_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.Hide_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Confirm_btn = QPushButton(Dialog)
        self.Confirm_btn.setObjectName(u"Confirm_btn")
        sizePolicy.setHeightForWidth(self.Confirm_btn.sizePolicy().hasHeightForWidth())
        self.Confirm_btn.setSizePolicy(sizePolicy)
        self.Confirm_btn.setMinimumSize(QSize(90, 40))
        self.Confirm_btn.setFont(font1)
        self.Confirm_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.Confirm_btn)

        self.Cancel_btn = QPushButton(Dialog)
        self.Cancel_btn.setObjectName(u"Cancel_btn")
        sizePolicy.setHeightForWidth(self.Cancel_btn.sizePolicy().hasHeightForWidth())
        self.Cancel_btn.setSizePolicy(sizePolicy)
        self.Cancel_btn.setMinimumSize(QSize(90, 40))
        self.Cancel_btn.setFont(font1)
        self.Cancel_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.Cancel_btn)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.Detail_text = QTextBrowser(Dialog)
        self.Detail_text.setObjectName(u"Detail_text")
        self.Detail_text.setMinimumSize(QSize(380, 180))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Detail_text.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.Detail_text.setFont(font2)
        self.Detail_text.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout.addWidget(self.Detail_text, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.Hide_btn.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Info_box.setText("")
        self.Hide_btn.setText(QCoreApplication.translate("Dialog", u"Show details..", None))
        self.Confirm_btn.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.Cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.Detail_text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>", None))
    # retranslateUi

