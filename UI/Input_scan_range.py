import datetime
import sys, os
import time
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QGridLayout, QLabel, QToolBar, QDialog, \
    QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt, QTimer, Slot, QThread, Signal
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QPixmap, QImage,QAction
from PySide6.QtWidgets import  QStatusBar, QFileDialog, QGraphicsPixmapItem, QGraphicsView, QGraphicsScene
from UI_input_ScanRange import Ui_Dialog

"""
input any scan range by several parts based on <Min>--<Max>--<Step>\n
return the range list when confirmed 
"""


def calculate_scan_range(min_E: float = 100, max_E: float = 120, step_E: float = 0.5):
    """
    get a list of photon energies based on the input low limit and upper limit and step
    :param min_E: float=100
    :param max_E: float=120
    :param step_E: float=0.5
    :return: energy list [scan_type,[min_E,min_E+1*step_E...max_E]]
    """
    energy_list = []
    N_step = int((max_E - min_E) / step_E)
    for i in range(N_step + 1):
        energy_list.append(round((min_E + i * step_E), 4))
    if min_E + N_step * step_E < max_E:
        energy_list.append(max_E)
    print(energy_list)
    return energy_list


class InputScanRange(QDialog, Ui_Dialog):
    data_sig = Signal(list)

    def __init__(self, scan_type:str,*input_note):
        super(InputScanRange, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Input Scan Range')
        self.range_list = list()
        self.scan_range = list()
        self._row_num = self.tableWidget.rowCount()
        self._column_num = self.tableWidget.columnCount()
        self.scan_type=scan_type
        self.input_note = self.Note_text.toPlainText()
        self.Note_text.setPlainText(self.input_note + input_note[0])
        scan_head='Input Scan range'+': '+scan_type
        self.Scan_label.setText(f'{scan_head:*^60}')
        # connect data signal emit
        #self.data_sig.connect(self.get_range_list)

    # input part
    def raise_warning(self, text):
        return QMessageBox.warning(self, 'ERROR', text, QMessageBox.Yes | QMessageBox.Cancel)

    def raise_info(self, text):
        return QMessageBox.information(self, 'info', text, QMessageBox.Yes | QMessageBox.Cancel)

    @Slot()
    def on_Add_row_btn_clicked(self):
        """
        add a new row when add row button clicked
        :return:
        """
        self._row_num = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self._row_num + 1)

    @Slot()
    def on_Del_row_btn_clicked(self):
        """
        delete last row when del row button clicked
        :return:
        """
        self._row_num = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self._row_num - 1)

    def get_scan_range(self):
        """
        calculate the scan range from the input info in the table box
        :return:
        """
        self._row_num = self.tableWidget.rowCount()
        self._column_num = self.tableWidget.columnCount()
        range_list = list()  # list=[(min,max,step)]
        if self._row_num > 0:
            for i in range(self._row_num):
                if self.tableWidget.item(i, 0) and self.tableWidget.item(i, 1) and self.tableWidget.item(i, 2):
                    try:
                        min_E = float(self.tableWidget.item(i, 0).text())
                        max_E = float(self.tableWidget.item(i, 1).text())
                        step_E = float(self.tableWidget.item(i, 2).text())
                    except ValueError as e:
                        self.raise_warning('check input,should be numbers')
                    else:
                        if min_E < max_E:
                            range_list.append((min_E, max_E, step_E))
                        else:
                            self.raise_info(f'check input in row number {i + 1}')
                else:
                    # omit any row with unfilled input
                    pass
        else:
            self.raise_warning("empty input,must check!")
        # get the scan range list from the range dict info
        if range_list:
            for i in range(len(range_list)):
                if i == 0:
                    temp_list = calculate_scan_range(range_list[i][0], range_list[i][1], range_list[i][2])
                    self.range_list += temp_list
                elif i > 0:
                    if range_list[i][0] >= range_list[i - 1][1]:
                        temp_list = calculate_scan_range(range_list[i][0], range_list[i][1], range_list[i][2])
                        self.range_list += temp_list
                    else:
                        self.raise_info(f'check input range,should in order:min->max')
                        self.range_list = list()

        return self.range_list

    @Slot()
    def on_Confirm_btn_clicked(self):
        """
        check the input info to acquire the scan range list
        if OK, display the range list
        :return:
        """
        scan_range = self.get_scan_range()
        if scan_range:
            print(scan_range)
            temp = list(set(scan_range))  # delete same item by set
            self.scan_range = sorted(temp)
            # choice=QMessageBox.information(self,'scan range check',f'get scan range:{self.scan_range}'
            #                                          ,QMessageBox.Yes|QMessageBox.No)

            choice = self.raise_info(f'Get scan range: {self.scan_range},total points:{len(self.scan_range)}accept or not ?')
            if choice == QMessageBox.Yes:
                print('start emit scan range')
                # emit the scan range
                self.data_sig.emit([self.scan_type,self.scan_range])
                time.sleep(1.0)
                self.close()
        else:
            self.raise_info(f'check input range')

    @Slot(dict)
    def get_range_list(self, scan_range: dict):
        for key,value in scan_range.items():
            print(f'get range list: {key}:{value}')

    def closeEvent(self, event):
        if not self.scan_range:
            info = 'input scan range not finish, are you sure to close this dialog?'
            choice = QMessageBox.information(self, 'close dialog', info, QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputScanRange('Energy','input energy range:eV')
    window.show()
    app.exec_()
