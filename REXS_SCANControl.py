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
# pyepics for PV access
from epics import ca, caget, cainfo, camonitor, caput, PV, get_pv
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
# import YAML load funcs
from Architect.YAML_Read_load import read_yaml_data
# import PV set QThread
from Architect.PVsetMoveControl import PVsetThread
# import data view plot UI
from UI.Data_View_Plot import DataViewPlot
# import scan range UI
from UI.Input_scan_range import InputScanRange, calculate_scan_range
# import PV monitor UI files
from UI.PV_Monitor_Widget import PVMonitor
# import scan range UI
from UI.Input_scan_range import InputScanRange
# import my message box
from UI.QtforPython_useful_tools import EmittingStr, MyMsgBox,AboutInfo
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
        self.data=[-1]

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
        self.__ini_scan_set()

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
        self.actionAbout.triggered.connect(self.show_about_info)
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
        About_icon=QIcon(os.path.join(icon_path, 'avast.svg'))
        self.actionView_data.setIcon(data_icon)
        self.actionDatabase.setIcon(database_icon)
        self.actionAbout.setIcon(About_icon)
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

    @Slot()
    def show_about_info(self):
        self.about_info=AboutInfo()
        self.about_info.show()
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
        self.adc_channels={"TEY_V":self.ADC_TEY_checkBox,"Au_V":self.ADC_Au_checkBox,"PD_V":self.ADC_PD_checkBox}
        self.pA_channels={"TEY_I":self.pA_TEY_checkBox,"Au_I":self.pA_Au_checkBox,"PD_I":self.pA_PD_checkBox}
        self.active_data_dict={}
        #for adc monitors
        self.All_monitors_dict={}
        self.All_monitor_count=0
        self.Select_endstation_cbx.currentIndexChanged['int'].connect(self.set_endstation)
        self.set_endstation(0)
        self.Scan_Channel_cbx.currentIndexChanged['int'].connect(self.set_scan_X)
        self.set_scan_X(0)
        # flag for monitoring on
        self.channel_monitor_on_flag=False

    @log_exceptions(log_func=logger.error)
    @Slot(int)
    def set_endstation(self,num:int):
        # choose another station
        self.endStation_num=num
        self.endStation_Address=EndStationAddress[num]
        yaml_file=os.path.abspath('.\\Architect\\PV_names_E20U2.yaml')
        self.load_station_PVs(yaml_file)

    @log_exceptions(log_func=logger.error)
    def load_station_PVs(self,yaml_file:str):
        """
        load station PV names according to the station selection
        """
        # remove all items in Scan_Channel_cbx
        while self.Scan_Channel_cbx.count()>0:
            self.Scan_Channel_cbx.removeItem(0)
        self.scanX_channel_dict={} # scan X channels{"name":{key:PVname}...} with keys=["SET","RBV","MOVN"(optional)]
        yaml_data=read_yaml_data(yaml_file)
        REXS_PVs=yaml_data['REXS_Station']
        RXES_PVs=yaml_data['RXES_Station']
        Beamline_PVs=yaml_data['BeamLine']
        # add beamline PVs
        self.scanX_channel_dict['Energy']=Beamline_PVs['PGM1_E']
        if self.Select_endstation_cbx.currentIndex()==0:
            # for REXS station
            for name,PVs in REXS_PVs.items():
                self.scanX_channel_dict[name]=PVs
            # for RXES station add BPM scan
        elif self.Select_endstation_cbx.currentIndex()==1:
            self.scanX_channel_dict["BPM_X"]=RXES_PVs["BPM_X"]
            self.scanX_channel_dict["BPM_Z"]=RXES_PVs["BPM_Z"]
        elif self.Select_endstation_cbx.currentIndex()==2:
            #for O-REXS station 
            pass
        # add scan channel to cbx
        for ch_name,pv_dict in self.scanX_channel_dict.items():
            self.Scan_Channel_cbx.addItem(ch_name)


    @Slot()
    def on_Start_Acqusition_btn_clicked(self):
        """check data channel and start acquiring data
        """
        self.Full_DataChannnels={}
        self.set_channels()
        print(self.Full_DataChannnels)
        try:
            for ch_name,daq_ch in self.Full_DataChannnels.items():
                self.add_channel_monitor(daq_ch)
        except Exception as e:
            print(e)
            logger.error(traceback.format_exc() + str(e))
        else:
            self.channel_monitor_on_flag=True
    
    def set_channels(self):
        # ADC channels
        for name,checkbox in self.adc_channels.items():
            if checkbox.isChecked():
                if name not in self.active_data_dict:
                    self.active_data_dict[name]=[]
                    self.Full_DataChannnels[name]=DATAChannel(name=name,address=self.endStation_Address[name],device="ADC")
        # pAmeter channels
        for name,checkbox in self.pA_channels.items():
            if checkbox.isChecked():
                if name not in self.active_data_dict:
                    self.active_data_dict[name]=[]
                    self.Full_DataChannnels[name]=DATAChannel(name=name,address=self.endStation_Address[name],device="pAmeter")

    def add_channel_monitor(self,daq_ch:DATAChannel):
        """add one channel monitor 

        Args:
            daq_ch (DATAChannel): provide a DATAChannel 
        """             
        if daq_ch.device=="ADC" and daq_ch.name not in self.All_monitors_dict:
            # adc address=(host,port,channel,ul_range_n)
            print(daq_ch.address[2],daq_ch.name)
            self.All_monitor_count+=1
            self.All_monitors_dict[daq_ch.name]=ADCMonitor(ADCname=daq_ch.name,host=daq_ch.address[0],port=daq_ch.address[1],
            board_num=self.endStation_num,channel=daq_ch.address[2],ul_range_n=daq_ch.address[-1])
            self.Monitor_MDI.addSubWindow(self.All_monitors_dict[daq_ch.name])
            self.All_monitors_dict[daq_ch.name].show()
            self.All_monitors_dict[daq_ch.name].emit_data_sig.connect(self.get_channel_data)
            self.All_monitors_dict[daq_ch.name].close_sig.connect(self.close_channel_monitor)
            #start the monitor
            self.All_monitors_dict[daq_ch.name].start_monitor()
    
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

    @log_exceptions(log_func=logger.error)
    @Slot(int)
    def set_scan_X(self,index:int):
        """set the PV name for scan X axis
        """
        scanX_name=self.Scan_Channel_cbx.currentText()
        self.scan_PVset=self.scanX_channel_dict[scanX_name]["SET"]
        self.scan_PVrbv=self.scanX_channel_dict[scanX_name]["RBV"]
        self.scan_PVmovn=self.scanX_channel_dict[scanX_name].get('MOVN',None)
        print(f'Now scan:{scanX_name} PV={self.scan_PVset} with readback: PV={self.scan_PVrbv} '
        f'and movn: {self.scan_PVmovn}')
        # set range flag before further scan
        self.scan_range_set_flag=0
    
    """
    end of data channel selection part
    """   
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of Scan set  part
    """
    def __ini_scan_set(self):
        #for PV monitor

        self.pvmonitors_dict={}
        self.pvmonitors_count=0
        self.scan_range_set_flag=0

    @Slot()
    def on_Set_range_btn_clicked(self):
        """set scan range
        """
        scanX_name=self.Scan_Channel_cbx.currentText()
        self.pv_current_value=self.Add_pv_monitor(pvname=self.scan_PVrbv,tag="SCAN X axis")
        if self.pv_current_value:
            input_info = f'scan channel: {scanX_name}\nCurrent value:\n{scanX_name}:{self.pv_current_value}'
            self.inputRange_dialog = InputScanRange(f'{scanX_name}', input_info)
            self.inputRange_dialog.data_sig.connect(self.get_scan_range)
            self.inputRange_dialog.show()
        else:
            self.raise_warning(f'access to {scanX_name} failed with None value get')

    @Slot(list)
    def get_scan_range(self, scan_range_list: list):
        """
        get the scan range,\n
        scan range list: [scan_type,[min_E,min_E+1*step_E...max_E]] \n
        :return:
        """
        if scan_range_list[-1]:
            self._scan_info = scan_range_list
            self.raise_info(f'Next will scan {scan_range_list[0]}, scan range:\n{scan_range_list[-1]},'
                            f' total points: {len(scan_range_list[-1])}, you can start now')
            self.scan_range_set_flag = 1
            #print(self._scan_info)
            min_value=scan_range_list[-1][0]
            max_value=scan_range_list[-1][-1]
            num=len(scan_range_list[-1])
            self.Min_input.setText(f'{min_value}')
            self.Max_input.setText(f'{max_value}')
            self.Num_input.setText(f'{num}')
            logger.info(f'get scan info: {self._scan_info}')

    def Add_pv_monitor(self,pvname,tag=None):
        print(f'get pvname: {pvname}')
        if pvname not in self.pvmonitors_dict:
            # add one monitor
            self.pvmonitors_count+=1
            self.pvmonitors_dict[pvname]=PVMonitor(PVname=pvname,TagName=tag)
            self.Monitor_MDI.addSubWindow(self.pvmonitors_dict[pvname])
            self.pvmonitors_dict[pvname].show()
            self.pvmonitors_dict[pvname].close_sig.connect(self.close_pvmonitor)
        else:
            print(f'already have monitor: {pvname}')
            self.statusLabel.setText(f'already have monitor: {pvname}')
            self.pvmonitors_dict[pvname].showMaximized()
        return self.pvmonitors_dict[pvname].get_pv_value()

    @Slot(str)
    def close_pvmonitor(self,pvname):
        print(f'will close pvmonitor: {pvname}')
        self.pvmonitors_dict[pvname].close()
        self.pvmonitors_dict.pop(pvname,0)
        self.pvmonitors_count-=1

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Start_scan_btn_clicked(self):
        """
        start the scan process
        """
        # check all status (channel set,range set) are OK
        if self.scan_range_set_flag==1 and self.channel_monitor_on_flag:
            scanX_name=self.Scan_Channel_cbx.currentText()
            detailed_info = f'Scan set: will scan {scanX_name}\n Current value: {self.pv_current_value}\n' \
                                f'Scan range: from {self.Min_input.text()} to {self.Max_input.text()}ms with totally {self.Num_input.text()} points\n' \
                                f'You should confirm to start scan process.'
            logger.info(detailed_info)
            self.msg_box = MyMsgBox('Channel Scan', f'Scan on {scanX_name}', details=detailed_info, signal=1)
            self.msg_box.close_sig.connect(self.pv_channel_scan)
            self.msg_box.exec()

    @log_exceptions(log_func=logger.error)
    @Slot(str)
    def pv_channel_scan(self, start_info: str):
        if start_info=='Yes':
            print(f'Now begin scan on{self._scan_info[0]} ')
            self._scan_info



    """
    end of Scan  part
    """   
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of close event
    """
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
