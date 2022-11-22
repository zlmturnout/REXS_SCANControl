import datetime
import math
import os
import random
import sys
import time
import traceback
from collections import namedtuple
import pandas as pd
# use PySide6
import PySide6
from PySide6 import QtCore, QtWidgets,QtSvg
from PySide6.QtCore import QSize, Qt, QThread, QTimer, Signal, Slot
from PySide6.QtGui import (QAction, QDoubleValidator, QIcon, QIntValidator,
                           QTextCursor,QPixmap,QPainter)
from PySide6.QtWidgets import (QApplication, QFileDialog, QGridLayout,
                               QMainWindow, QMessageBox, QPushButton, QStyle,
                               QWidget)

# import data form to save dict data
from resource.Dict_DataFrame_Sqlite import (dict_to_csv, dict_to_excel,
                                             dict_to_json, dict_to_SQLTable)
# import my own matplotlib InitialPlot
from resource.My_Matplotlib_PySide6 import (InitialPlot, MonitorPlot, Myplot,
                                             NavigationToolbar)
# import my tool functions for usage
from resource.Tools_functions import (createPath, deco_count_time,
                                       get_datetime, log_exception,
                                       log_exceptions, my_logger, to_log)
# import data view plot UI
from UI.Data_View_Plot import DataViewPlot
# import scan range UI
from UI.Input_scan_range import InputScanRange, calculate_scan_range
# import sub UI files
# import my message box
from UI.QtforPython_useful_tools import EmittingStr, MyMsgBox
from UI.SQLDataViewPlot import ViewSQLiteData
# import main UI function
from UI.UI_REXS_SCAN import Ui_MainWindow
# ADC monitor
from UI.ADC_Widget import ADCMonitor
# device address
from Architect.Device_address import EndStationAddress
# save path info
FILE_PATH=os.getcwd()
print(f'current path:{FILE_PATH}')
save_path = os.path.join(FILE_PATH, 'save_data')
createPath(save_path)
# sqlite database path
SQLiteDB_path=save_path
log_path = os.path.join(FILE_PATH, 'log_info')
createPath(log_path)

# logger
log_file = f'{time.strftime("%Y-%m-%d", time.localtime())}.log'
logger = my_logger(log_file=os.path.join(log_path, log_file), logger_name='Limin')

"""
notes:
This is the main python file for  plotting the < X/Z position vs I_V_PD>, and then determine the beam size 
# Data structure
full_data = {'BPM-X pos(um)': self._plot_X_list, 'BPM-Z pos(um)': self._plot_Z_list,
            'adc voltage(V)': self._plot_adc_list, 'current(pA)': self._plot_pAmeter_list,
            'time_stamp': self._time_stamp, 'scan set': self._scan_list}
"""

"""DATA structure
    namedtuple
    Returns:
        _type_: _description_
"""
ChannelDATA=namedtuple('ChannelDATA',field_names=["Name","Address","Device"])


class DATAChannel(object):
    """data structure for each channel

    DATAChannel with property of [name,address,device,data]
    """
    def __init__(self,name:str,address:tuple,device:str) -> None:
        self.__name=name
        self.__address=address
        self.__device=device
        self.data=[0]

    @property
    def name(self):
        return self.__name
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self,address:tuple):
        self.__address=address

    @property
    def device(self):
        return self.__device
    
    @device.setter
    def device(self,dev:str):
        self.__device=dev

    def add_data(self,value:float):
        """add a new data value to data list 

        Args:
            value (float): _description_
        """
        self.data.append(value)
        # maximal 1000 values
        if len(self.data)>1000:
            self.data=self.data[-1000:]

    def __repr__(self) -> str:
        return f'name:{self.__name}\naddress:{self.__address}\ndevice:{self.__device}\ndata:{self.data}'
    
class REXSScanPlot(QMainWindow, Ui_MainWindow):
    # signal used
    scan_info_sig = Signal(dict)
    scan_start_sig = Signal(list)

    @log_exceptions(log_func=logger.error)
    def __init__(self, parent=None):
        super(REXSScanPlot, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('REXS_Scan_plot')
        print('REXS_Scan_plot')
        self.__ini_output()
        self._ini_menu()
        self.__ini_DAQ()

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    MenuBar part
    """
    @log_exceptions(log_func=logger.error)
    def _ini_menu(self):
        """
        for menuBar
        :return:
        """
        style = QApplication.style()
        # open data file
        OpenDATA = QAction('open data(&O)...', self)
        OpenDATA.setIcon(style.standardIcon(QStyle.SP_DialogOpenButton))
        OpenDATA.setShortcut(Qt.CTRL | Qt.Key_O)
        OpenDATA.triggered.connect(self.open_datafile)
        self.menuMenu.addAction(OpenDATA)
        # save data
        SaveDATA = QAction('save data(&S)...', self)
        SaveDATA.setIcon(style.standardIcon(QStyle.SP_DialogSaveButton))
        SaveDATA.setShortcut(Qt.CTRL | Qt.Key_S)
        SaveDATA.triggered.connect(self.save_all_data)
        self.menuMenu.addAction(SaveDATA)
        # show View data in analysis menuBar
        self.actionView_data.triggered.connect(self.show_full_data)
        self.actionDatabase.triggered.connect(self.view_sql_data)
        self.__init__Icons()

    @log_exceptions(log_func=logger.error)
    def __init__Icons(self):
        """Initial all icons in the menuBar"""
        #icon_path=os.path.join(FILE_PATH,'/resource/icons')
        icon_path=os.path.realpath('icons')
        print(f'icon_path: %s' % icon_path)
        data_icon=QIcon(os.path.join(icon_path, 'databricks.svg'))
        database_icon=QIcon(os.path.join(icon_path, 'datacamp.svg'))
        PMC_motor_icon=QIcon(os.path.join(icon_path, 'pkgsrc.svg'))
        pAmeter_icon=QIcon(os.path.join(icon_path, 'avast.svg'))
        self.actionView_data.setIcon(data_icon)
        self.actionDatabase.setIcon(database_icon)
        #Eline_icon=QIcon(os.path.join(icon_path, 'databricks.svg')) #databricks
        Eline_icon=QIcon(os.path.join(icon_path, 'Eline20U_icons.svg'))
        self.Icon_label.setPixmap(QPixmap(os.path.join(icon_path, 'Eline20U_icons.svg')))
        self.Icon_label.setScaledContents(True)
        self.setWindowIcon(Eline_icon)
        self.setIconSize(QSize(80,80))
    
    @log_exceptions(log_func=logger.error)
    def open_datafile(self):
        """
        open data file,file format should be excel(.xlsx)
        :return:
        """
        pd_data = pd.DataFrame()
        filename, filetype = QFileDialog.getOpenFileName(self, "read data file(supported filetype:xlsx/csv/json)",
                                                         './', '*.xlsx;;*.csv;;*.json')
        print(filename, filetype)
        if filename.endswith('.xlsx'):
            # add dtype={'time stamp': 'datetime64[ns]'} if have 'time stamp'
            pd_data = pd.read_excel(filename, index_col=0, na_values=["NA"], engine='openpyxl')
            # print(pd_data)
        if filename.endswith('.csv'):
            pd_data = pd.read_csv(filename, index_col=0)
        if filename.endswith('.json'):
            pd_data = pd.read_json(filename)
        # drop the row with NaN and return
        valid_pd_data = pd_data
        self.ViewopenData = DataViewPlot(valid_pd_data)
        self.ViewopenData.show_data_table(valid_pd_data)
        self.ViewopenData.show()
    
    @log_exceptions(log_func=logger.error)
    def save_all_data(self):
        """
        save all data to usr defined location and name,
        file format should be excel(.xlsx)
        :return:
        """
        print('save data')
        scan_data = self.get_full_data()
        self.usr_save_full_data(scan_data, save_path, usr_define=1)

    @log_exceptions(log_func=logger.error)
    @Slot()
    def view_sql_data(self):
        self.ViewSqlData = ViewSQLiteData()
        self.ViewSqlData.show()


    @log_exceptions(log_func=logger.error)
    def show_full_data(self):
        self.ViewData = DataViewPlot()
        full_dict_data = self.get_full_data()
        full_pd_data = self.ViewData.dict_to_pd(full_dict_data)
        self.ViewData.show_data_table(full_pd_data)
        self.ViewData.show()

    """
    end of MenuBar part
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of info output part
    """

    @log_exceptions(log_func=logger.error)
    def __ini_output(self):
        # set a timer to show current time
        self.cur_timer = QTimer()
        self.cur_timer.timeout.connect(self.set_cur_time)
        self.cur_timer.start(100)
        # out put all to status_box
        sys.stdout = EmittingStr()
        sys.stderr = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)
        sys.stderr.textWritten.connect(self.outputWritten)
        # program start info
        start_info = f'REXS@20U Scan&Plot program \n\tby Limin Zhou @SSRF_20U' \
                     f'\n\t{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}'
        print(start_info)

    # out put info into the status msg box
    def outputWritten(self, text):
        cursor = self.info_textbox.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.info_textbox.setTextCursor(cursor)
        self.info_textbox.ensureCursorVisible()

    def set_cur_time(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.Now_time.setText(f'Now: {timestamp}')

    # raise info part
    def raise_warning(self, text):
        return QMessageBox.warning(self, 'ERROR', text, QMessageBox.Yes | QMessageBox.Cancel)

    def raise_info(self, text):
        return QMessageBox.information(self, 'info', text, QMessageBox.Yes | QMessageBox.Cancel)

    def set_progress_Bar(self,status:int):
        self.progressBar.setValue(status)

    """
    end of info output part

    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of data channel selection part
    """
    def __ini_DAQ(self):
        """
        initial data acquisition
        """
        self.endStation_num=0
        self.endStation_Address=EndStationAddress[self.endStation_num]
        # data acqusition channel
        self.Full_DataChannnels=dict()
        self.all_channels={"TEY_V":self.ADC_TEY_checkBox,"Au_V":self.ADC_Au_checkBox,"PD_V":self.ADC_PD_checkBox,
            "TEY_I":self.pA_TEY_checkBox,"Au_I":self.pA_Au_checkBox,"PD_I":self.pA_PD_checkBox}
        self.active_data_dict={}
        #for adc monitors
        self.All_monitors_dict={}
        self.All_monitor_count=0
        self.Select_endstation_cbx_currentIndexChanged['int'].connect(self.set_endstation)


    @log_exceptions(log_func=logger.error)
    @Slot(int)
    def set_endstation(self,num:int):
        # choose another station
        self.endStation_num=num
        self.endStation_Address=EndStationAddress[num]
    
    @Slot()
    def on_Start_Acqusition_btn_clicked(self):
        """check data channel and start acquiring data
        """
        self.set_channels()
        print(self.Full_DataChannnels)
        for ch_name,daq_ch in self.Full_DataChannnels.items():
            self.add_channel_monitor(daq_ch)
    
    def set_channels(self):
        for name,checkbox in self.all_channels.items():
            if checkbox.isChecked():
                if name not in self.active_data_dict:
                    self.active_data_dict[name]=[]
                    self.Full_DataChannnels[name]=DATAChannel(name=name,address=self.endStation_Address[name],device="ADC")

    def add_channel_monitor(self,daq_ch:DATAChannel):
        """add one channel monitor 

        Args:
            daq_ch (DATAChannel): provide a DATAChannel 
        """             
        if daq_ch.device=="ADC" and daq_ch.name not in self.All_monitors_dict:
            # adc address=(host,port,channel,ul_range_n)
            print(daq_ch.address,daq_ch.name)
            self.All_monitor_count+=1
            self.All_monitors_dict[daq_ch.name]=ADCMonitor(ADCname=daq_ch.name,host=daq_ch.address[0],port=daq_ch.address[1],
            board_num=self.endStation_num,channel=daq_ch.address[2],ul_range_n=daq_ch.address[-1])
            self.Monitor_MDI.addSubWindow(self.All_monitors_dict[daq_ch.name])
            self.All_monitors_dict[daq_ch.name].show()
            self.All_monitors_dict[daq_ch.name].emit_data_sig.connect(self.get_channel_data)
            self.All_monitors_dict[daq_ch.name].close_sig.connect(self.close_channel_monitor)
    
    @Slot(str,float)
    def get_channel_data(self,ch_name:str,value:float):
        print(f'channel: {ch_name} get a new value: {value}')
        #update data list in DATAChannel with ch_name
        self.Full_DataChannnels[ch_name].add_data(value)
    
    @Slot(str)
    def close_channel_monitor(self,ch_name:str):
        """remove data channel monitor

        Args:
            ch_name (str): _description_
        """
        print(f'now close channel monitor:{ch_name}')
        self.All_monitors_dict[ch_name].close()
        self.All_monitors_dict.pop(ch_name,0)
        self.All_monitor_count-=1


    
    """
    end of data channel selection part
    """   
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    def closeEvent(self, event):
        if self._start_plot_flag == 1:
            self.raise_info('Stop the scan process before exit!')
            event.ignore()
        elif self._start_plot_flag == 0:
            close = QMessageBox.question(self,
                                                   "QUIT",
                                                   "Are you sure to exit?",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if close == QMessageBox.Yes:
                # save data
                # self.usr_save_full_data(usr_define=0)
                self.clear_all_data()
                event.accept()
            else:
                event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = REXSScanPlot()
    win.show()
    sys.exit(app.exec())
    # ch1=DATAChannel('Au_REXS',address="10.30.95.167:54211",device="ADC")
    # ch1.data.append(1)
    # ch1.data.append(2)
    # print(ch1.__repr__())
