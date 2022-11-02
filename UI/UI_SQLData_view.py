# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_SQLData_view.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTableView, QWidget)

from sqltreewidget import SqlTreeWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1008, 668)
        self.gridLayout_4 = QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Update_database__btn = QPushButton(Dialog)
        self.Update_database__btn.setObjectName(u"Update_database__btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Update_database__btn.sizePolicy().hasHeightForWidth())
        self.Update_database__btn.setSizePolicy(sizePolicy)
        self.Update_database__btn.setMinimumSize(QSize(80, 40))
        self.Update_database__btn.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        font.setBold(True)
        self.Update_database__btn.setFont(font)
        self.Update_database__btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.gridLayout.addWidget(self.Update_database__btn, 0, 1, 1, 1)

        self.Open_datebase_btn = QPushButton(Dialog)
        self.Open_datebase_btn.setObjectName(u"Open_datebase_btn")
        sizePolicy.setHeightForWidth(self.Open_datebase_btn.sizePolicy().hasHeightForWidth())
        self.Open_datebase_btn.setSizePolicy(sizePolicy)
        self.Open_datebase_btn.setMinimumSize(QSize(120, 40))
        self.Open_datebase_btn.setMaximumSize(QSize(100, 40))
        self.Open_datebase_btn.setFont(font)
        self.Open_datebase_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.gridLayout.addWidget(self.Open_datebase_btn, 0, 0, 1, 1)

        self.Database_txt = QLineEdit(Dialog)
        self.Database_txt.setObjectName(u"Database_txt")
        self.Database_txt.setMinimumSize(QSize(300, 40))
        self.Database_txt.setMaximumSize(QSize(16777215, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 85, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.Database_txt.setPalette(palette)
        self.Database_txt.setFont(font)
        self.Database_txt.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Database_txt, 0, 2, 1, 1)

        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.treeView = SqlTreeWidget(self.splitter)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setMinimumSize(QSize(50, 400))
        self.treeView.setMaximumSize(QSize(300, 16777215))
        self.splitter.addWidget(self.treeView)
        self.tableView = QTableView(self.splitter)
        self.tableView.setObjectName(u"tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        self.tableView.setMinimumSize(QSize(300, 400))
        self.splitter.addWidget(self.tableView)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 3)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(400, 40))
        self.label_6.setMaximumSize(QSize(500, 40))
        palette1 = QPalette()
        brush3 = QBrush(QColor(0, 170, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_6.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setMaximumSize(QSize(40, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 255, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_7.setPalette(palette2)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_7.setFont(font2)
        self.label_7.setFrameShape(QFrame.NoFrame)
        self.label_7.setFrameShadow(QFrame.Sunken)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.X_axis_cbx = QComboBox(Dialog)
        self.X_axis_cbx.setObjectName(u"X_axis_cbx")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.X_axis_cbx.sizePolicy().hasHeightForWidth())
        self.X_axis_cbx.setSizePolicy(sizePolicy2)
        self.X_axis_cbx.setMinimumSize(QSize(60, 40))
        self.X_axis_cbx.setMaximumSize(QSize(16777215, 40))
        self.X_axis_cbx.setFont(font)

        self.horizontalLayout_6.addWidget(self.X_axis_cbx)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(40, 40))
        self.label_8.setMaximumSize(QSize(40, 40))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_8.setPalette(palette3)
        self.label_8.setFont(font2)
        self.label_8.setFrameShape(QFrame.NoFrame)
        self.label_8.setFrameShadow(QFrame.Sunken)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.Y_axis_cbx = QComboBox(Dialog)
        self.Y_axis_cbx.setObjectName(u"Y_axis_cbx")
        sizePolicy2.setHeightForWidth(self.Y_axis_cbx.sizePolicy().hasHeightForWidth())
        self.Y_axis_cbx.setSizePolicy(sizePolicy2)
        self.Y_axis_cbx.setMinimumSize(QSize(60, 40))
        self.Y_axis_cbx.setMaximumSize(QSize(16777215, 40))
        self.Y_axis_cbx.setFont(font)

        self.horizontalLayout_6.addWidget(self.Y_axis_cbx)

        self.Plot_database__btn = QPushButton(Dialog)
        self.Plot_database__btn.setObjectName(u"Plot_database__btn")
        sizePolicy.setHeightForWidth(self.Plot_database__btn.sizePolicy().hasHeightForWidth())
        self.Plot_database__btn.setSizePolicy(sizePolicy)
        self.Plot_database__btn.setMinimumSize(QSize(100, 40))
        self.Plot_database__btn.setMaximumSize(QSize(100, 40))
        self.Plot_database__btn.setFont(font1)
        self.Plot_database__btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_6.addWidget(self.Plot_database__btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Asymptom_input = QLineEdit(Dialog)
        self.Asymptom_input.setObjectName(u"Asymptom_input")
        self.Asymptom_input.setMinimumSize(QSize(100, 40))
        self.Asymptom_input.setMaximumSize(QSize(100, 40))
        font3 = QFont()
        font3.setFamilies([u"Cambria Math"])
        font3.setPointSize(14)
        self.Asymptom_input.setFont(font3)
        self.Asymptom_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Asymptom_input, 0, 2, 1, 1)

        self.Death_input = QLineEdit(Dialog)
        self.Death_input.setObjectName(u"Death_input")
        self.Death_input.setMinimumSize(QSize(100, 40))
        self.Death_input.setMaximumSize(QSize(100, 40))
        self.Death_input.setFont(font3)
        self.Death_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Death_input, 0, 3, 1, 1)

        self.Infection_input = QLineEdit(Dialog)
        self.Infection_input.setObjectName(u"Infection_input")
        self.Infection_input.setMinimumSize(QSize(100, 40))
        self.Infection_input.setMaximumSize(QSize(100, 40))
        font4 = QFont()
        font4.setFamilies([u"Cambria Math"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.Infection_input.setFont(font4)
        self.Infection_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Infection_input, 0, 1, 1, 1)

        self.Select_date_btn = QPushButton(Dialog)
        self.Select_date_btn.setObjectName(u"Select_date_btn")
        sizePolicy.setHeightForWidth(self.Select_date_btn.sizePolicy().hasHeightForWidth())
        self.Select_date_btn.setSizePolicy(sizePolicy)
        self.Select_date_btn.setMinimumSize(QSize(100, 40))
        self.Select_date_btn.setMaximumSize(QSize(100, 40))
        self.Select_date_btn.setFont(font)
        self.Select_date_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.gridLayout_2.addWidget(self.Select_date_btn, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Confirm_btn = QPushButton(Dialog)
        self.Confirm_btn.setObjectName(u"Confirm_btn")
        sizePolicy.setHeightForWidth(self.Confirm_btn.sizePolicy().hasHeightForWidth())
        self.Confirm_btn.setSizePolicy(sizePolicy)
        self.Confirm_btn.setMinimumSize(QSize(100, 40))
        self.Confirm_btn.setMaximumSize(QSize(100, 40))
        self.Confirm_btn.setFont(font1)
        self.Confirm_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout.addWidget(self.Confirm_btn)

        self.Cancel_btn = QPushButton(Dialog)
        self.Cancel_btn.setObjectName(u"Cancel_btn")
        sizePolicy.setHeightForWidth(self.Cancel_btn.sizePolicy().hasHeightForWidth())
        self.Cancel_btn.setSizePolicy(sizePolicy)
        self.Cancel_btn.setMinimumSize(QSize(100, 40))
        self.Cancel_btn.setMaximumSize(QSize(100, 40))
        self.Cancel_btn.setFont(font1)
        self.Cancel_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout.addWidget(self.Cancel_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.Plot_gridlayout = QGridLayout()
        self.Plot_gridlayout.setObjectName(u"Plot_gridlayout")

        self.gridLayout_3.addLayout(self.Plot_gridlayout, 4, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Update_database__btn.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.Open_datebase_btn.setText(QCoreApplication.translate("Dialog", u"Open database", None))
        self.Database_txt.setText("")
        self.Database_txt.setPlaceholderText(QCoreApplication.translate("Dialog", u"Sqlite database file", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Tools", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"X:", None))
#if QT_CONFIG(tooltip)
        self.X_axis_cbx.setToolTip(QCoreApplication.translate("Dialog", u"X axis", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Y:", None))
#if QT_CONFIG(tooltip)
        self.Y_axis_cbx.setToolTip(QCoreApplication.translate("Dialog", u"Y axis", None))
#endif // QT_CONFIG(tooltip)
        self.Plot_database__btn.setText(QCoreApplication.translate("Dialog", u"Plot", None))
        self.Asymptom_input.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Death_input.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Infection_input.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Select_date_btn.setText(QCoreApplication.translate("Dialog", u"Select Date", None))
        self.Confirm_btn.setText(QCoreApplication.translate("Dialog", u"add", None))
        self.Cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

