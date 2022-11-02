from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QGridLayout, QLabel, QToolBar, QDialog
from PySide6.QtCore import Qt, QTimer, Slot, QThread, Signal
from UI.UI_check_scan_range import Ui_Dialog

"""
pop a window with info to check the input scan information
"""


class ScanCheck(QDialog, Ui_Dialog):
    scan_sig = Signal(dict)

    def __init__(self,X_axis,X_scan_range,Y_axis):
        super(ScanCheck, self).__init__()
        self.setupUi(self)
        self._X_axis = X_axis
        self._Y_axis = Y_axis
        self._X_scan_range=X_scan_range
        self._X_range_list = []
        self._get_info_flag = 1

        self.buttonBox.accepted.connect(self.emit_scan_info)
        self.X_axis_usage.setText(self._X_axis)
        self.X_scan_range.setText(str(self._X_scan_range))
        self.Y_axis_usage.setText(self._Y_axis)

    @staticmethod
    def get_pos_list(min_p: float = 100, max_p: float = 120, step_p: float = 0.5):
        """
        get a position list based on the input low limit and upper limit and step
        :param max_p:
        :param step_p:
        :return:
        """
        pos_list = []
        N_step = int((max_p - min_p) / step_p)
        for i in range(N_step + 1):
            pos_list.append(min_p + i * step_p)
        if min_p + N_step * step_p < max_p:
            pos_list.append(max_p)
        print(pos_list)
        return pos_list


    def show_scan_info(self):
        """
        info={'X scan':Grating pos or mirror pos,'X scan range':[min:max:step],'Y scan':  adc voltage or pAmeter current}
        :param info:
        :return:
        """
        self.X_axis_usage.setText(self._X_axis)
        self.X_scan_range.setText(self._X_scan_range)
        self.Y_axis_usage.setText(self._Y_axis)

    def emit_scan_info(self):
        self._X_range_list = self.get_pos_list(self._X_scan_range[0],self._X_scan_range[1],self._X_scan_range[-1])
        scan_info = {'X scan': self._X_axis, 'X range list': self._X_range_list, 'Y scan': self._Y_axis}
        self.scan_sig.emit(scan_info)
