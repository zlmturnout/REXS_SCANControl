import numpy as np
import math
from math import pow
import sys,os,time,datetime
sys.path.append('.')
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QGridLayout, QLabel, QToolBar, QDialog
from PySide6.QtCore import Qt, QTimer, Slot, QThread, Signal
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QPixmap, QImage,QAction
from PySide6.QtGui import QRegularExpressionValidator , QIntValidator, QDoubleValidator
from PySide6.QtWidgets import  QStatusBar, QFileDialog, QGraphicsPixmapItem, QGraphicsView, QGraphicsScene
from UI.UI_EPU_cal import Ui_MainWindow
E=450.0
# -3.22603+0.21154*H3-8.14607*10^(-4)*H3^2+2.22227*10^(-6)*H3^3-3.97447*10^(-9)*H3^4+4.67901*10^(-12)*H3^5-3.58878*10^(-15)*H3^6+1.72643*10^(-18)*H3^7-4.73077*10^(-22)*H3^8+5.6383*10^(-26)*H3^9
EPU_gap=-3.22603+0.21154*E-8.14607*pow(10,-4)*E**2+2.22227*pow(10,-6)*E**3-3.97447*pow(10,-9)*E**4+4.67901*pow(10,-12)*E**5-3.58878*pow(10,-15)*E**6+1.72643*pow(10,-18)*E**7-4.73077*pow(10,-22)*E**8+5.6383*pow(10,-26)*E**9
print(f'Epu_gap at Energy:{E}eV={EPU_gap}')


class ParameterSet(QMainWindow, Ui_MainWindow):
    sig = Signal(list)

    def __init__(self):
        super(ParameterSet, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("EPU calculate")
        # connection to change
        self.Energy=450
        self.Set_energy.valueChanged.connect(self.get_input_energy)

    def get_input_energy(self):
        self.Energy=float(self.Set_energy.text().strip('eV'))
        print(f'get energy:{self.Energy:.2f}')

    @staticmethod
    def cal_EPU_gap(Energy:float=450.0):
        """
        calculate EPU gap at each energy
        :param Energy:
        :return:
        """
        E=Energy
        return -3.22603+0.21154*E-8.14607*pow(10,-4)*E**2+2.22227*pow(10,-6)*E**3-3.97447*pow(10,-9)*E**4+4.67901*pow(10,-12)*E**5-3.58878*pow(10,-15)*E**6+1.72643*pow(10,-18)*E**7-4.73077*pow(10,-22)*E**8+5.6383*pow(10,-26)*E**9

    @Slot()
    def on_Cal_EPU_btn_clicked(self):
        """
        show the calculated EPU gap
        :return:
        """
        EPU_gap=self.cal_EPU_gap(self.Energy)
        self.EPU_gap_text.setText(f'{EPU_gap:.4f}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParameterSet()
    window.show()
    app.exec_()
