import datetime
import math
import os
import random
import sys
import time,re
import traceback
from collections import namedtuple
import pandas as pd
import numpy as np
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
from Architect.PVsetMoveControl import PVsetThread,SSRFBeamLine
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
        self.__ini_plot()
        self.__ini_beamline()

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
    start of operator and beamline info part
    """
    def __ini_beamline(self):
        self.SSRF_timer=QTimer()
        self.SSRF_timer_runFlag=False
        self.SSRF_timer.timeout.connect(self.get_SSRF_BeamStatus)
        self.SSRF_beamline=SSRFBeamLine()
        today = time.strftime('%Y-%m-%d', time.localtime())
        self.Today_label.setText(today+"@E-line20U2")
        self.SSRF_timer.start(1000)
        self.username="User"
        self.UserName_input.returnPressed.connect(self.set_username)
    
    def get_SSRF_BeamStatus(self):
        beam_current=self.SSRF_beamline.beamcurrent
        self.BeamCurrent_lcd.display(beam_current)
        if "TEY_V" in self.Full_DataChannnels:
            pass
            #print(f'get TEY_V: {self.Full_DataChannnels["TEY_V"].data[-1]} V')    
    
    @Slot()
    def set_username(self):
        username=self.UserName_input.text()
        self.username=username+"@E-line20U2"
        print(f'current-user:{self.username}')
        self.UserName_input.setStyleSheet("QLineEdit{background-color: rgb(99, 239, 255);color: rgb(255, 124, 133);}")
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
        self.active_data_dict={} # all channel data will store in the active data dict
        #for adc monitors
        self.All_monitors_dict={}
        self.All_monitor_count=0
        self.Select_endstation_cbx.currentIndexChanged['int'].connect(self.set_endstation)
        self.set_endstation(0)
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
        if not self.channel_monitor_on_flag:
            try:
                self.Full_DataChannnels={}
                self.set_channels()
                print(self.Full_DataChannnels)
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
        #print(f'channel: {ch_name} get a new value: {value}')
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
    
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of Scan range set part
    """
    def __ini_scan_set(self):
        #for PV monitor
        self.pvmonitors_dict={}
        self.pvmonitors_count=0
        self.scan_range_set_flag=0
        # scan data 
        self.total_scan_num=0
        self.curr_scan_num=0
        self.scan_X_set_list=[]
        self.scan_X_data_set=[]
        self.scan_X_data_rbv=[]
        self.scan_timestamp_list=[]
        self.scan_started_flag=False
        self._save_N=0
        # timer for scan process
        self.scan_start_time = time.time()
        self.scan_cost_timer = QTimer()
        self.scan_cost_timer.timeout.connect(self.update_cost_time)
        # set scan X type
        self.Scan_Channel_cbx.currentIndexChanged['int'].connect(self.set_scan_X)
        self.set_scan_X(0)

    @staticmethod
    def expect_time_cost(scan_mode:str,scan_num: int, t_interval: int):
        """
        calculate the expected time cost of this scan
        :param scan_mode: 'ADC' or 'pAmeter'
        :param scan_num: total scan numbers
        :param t_interval: set dt/ms
        :return: time cost by seconds
        """
        if scan_mode == 'ADC':
            return float(scan_num * (t_interval / 1000 + 1.5))
        elif scan_mode == 'pAmeter':
            return float(scan_num * (t_interval / 1000 + 1.0))
        else:
            return float(scan_num * (t_interval / 1000 + 2.0))

    @Slot()
    def update_cost_time(self):
        time_past = time.time() - self.scan_start_time
        self.Cost_time.setText('Time Cost :' + str(datetime.timedelta(seconds=time_past)))

    @log_exceptions(log_func=logger.error)
    @Slot(int)
    def set_scan_X(self,index:int):
        """set the PV name for scan X axis
        """
        self.scanX_name=self.Scan_Channel_cbx.currentText()
        self.scan_PVset=self.scanX_channel_dict[self.scanX_name]["SET"]
        self.scan_PVrbv=self.scanX_channel_dict[self.scanX_name]["RBV"]
        self.scan_PVmovn=self.scanX_channel_dict[self.scanX_name].get('MOVN',None)
        scan_msg=f'Now will scan:{self.scanX_name} PV={self.scan_PVset} with readback: PV={self.scan_PVrbv} '
        f'and movn: {self.scan_PVmovn}'
        print(scan_msg)
        logger.info(scan_msg)
        # set range flag before further scan
        self.scan_range_set_flag=0

    @Slot()
    def on_Set_range_btn_clicked(self):
        """set scan range
        """
        self.pv_current_value=self.Add_pv_monitor(pvname=self.scan_PVrbv,tag="SCAN X axis")
        if self.pv_current_value:
            input_info = f'scan channel: {self.scanX_name}\nCurrent value:\n{self.scanX_name}:{self.pv_current_value}'
            self.inputRange_dialog = InputScanRange(f'{self.scanX_name}', input_info)
            self.inputRange_dialog.data_sig.connect(self.get_scan_range)
            self.inputRange_dialog.show()
        else:
            self.raise_warning(f'access to {self.scanX_name} failed with None value get')

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

    """
    end of the scan range set part
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of the scan process part
    """

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Start_scan_btn_clicked(self):
        """
        start the scan run process
        # main process:
        1. set X PV
        2. acquire channel data
        3. plot the X-ch data
        4. check should start next round[1,2,3] again
        5. end scan process and save data

        """
        # check all status (channel set,range set) are OK
        if self.scan_range_set_flag==1 and self.channel_monitor_on_flag and not self.scan_started_flag:
            detailed_info = f'Scan set: will scan {self.scanX_name}\n Current value: {self.pv_current_value}\n' \
                                f'Scan range: from {self.Min_input.text()} to {self.Max_input.text()}ms with totally {self.Num_input.text()} points\n' \
                                f'You should confirm to start scan process.'
            logger.info(detailed_info)
            # clean the active_data_dict
            self.curr_scan_num=0
            self.clear_all_data()
            for ch,ch_datalist in self.active_data_dict.items():
                ch_datalist=[]
            self.msg_box = MyMsgBox('Channel Scan', f'Scan on {self.scanX_name}', details=detailed_info, signal=1)
            self.msg_box.close_sig.connect(self.pv_channel_scan)
            self.msg_box.exec()

    @log_exceptions(log_func=logger.error)
    @Slot(str)
    def pv_channel_scan(self, start_info: str):
        """PV channel scan start
        Note on scan_info=[scanX_name,[set_value_list]]
        
        Args:
            start_info (str): Yes|Cancel
        
        """
        if start_info=='Yes':
            print(f'Now begin scan on{self._scan_info[0]} ')
            self.scan_X_set_list=self._scan_info[1]
            self.total_scan_num=len(self.scan_X_set_list)
            # start emit signal for PV sets
            self.scan_start_sig.connect(self.set_X_PV)
            self.scan_start_sig.emit([self.curr_scan_num,"Set_X"])
            logger.info(f'begin set PV value')
            # calculate time cost
            time_cost = self.expect_time_cost(scan_mode='ADC',scan_num=len(self.scan_X_set_list), t_interval=500)
            t_done = time.time() + time_cost
            tdone_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_done))
            self.Done_time.setText(f'Finish at:{tdone_stamp}')
            self.scan_start_time = time.time()
            self.scan_cost_timer.start(1000)
        elif start_info == 'Cancel':
            pass
    
    @Slot(list)
    def set_X_PV(self,Xset_info:list):
        """
        set the PV value of X scan
        Args:
            Xset_info (list): [cur_scan_num,"Set_X"]
        """
        if Xset_info[-1]=="Set_X":
            self.scan_started_flag=True
            X_setValue=self.scan_X_set_list[Xset_info[0]]
            self.XsetThread=PVsetThread(set_pv=self.scan_PVset,set_value=X_setValue,rbv_pv=self.scan_PVrbv,
                                            movn_pv=self.scan_PVmovn,check_num=0,resolution=0.02)
            self.XsetThread.done_signal.connect(self.Xset_done)
            self.XsetThread.start()
    
    @Slot(list)
    def Xset_done(self,done_info:list):
        """X PV value set done,append data and acquire data from all active channels

        Args:
            done_info (list): [read_back,set_value,check_n,set_info]
        """
        print(done_info)
        if done_info[-1]=="done" or 'done with time out':
            # set X done
            self.scan_X_data_rbv.append(done_info[0])
            self.scan_X_data_set.append(done_info[1])
            logger.info(f'{self.scanX_name} set done: {done_info}')
            # start channel data acquire from active_data_dict
            try:
                for ch_name,ch_data_list in self.active_data_dict.items():
                    if isinstance(ch_data_list,list):
                        # add latest data from DATAChannel of this ch_name to active_data_dict 
                        ch_data_list.append(self.Full_DataChannnels[ch_name].data[-1])
            except Exception as e:
                print(e)
                logger.error(traceback.format_exc() + str(e))
            else:
                # now start new run
                self.ch_dataAcquire_done()

    def ch_dataAcquire_done(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.scan_timestamp_list.append(timestamp)
        # plot the all scan channel data acording to plot set 
        full_X_data={f'{self.scanX_name}_set':self.scan_X_data_set,f'{self.scanX_name}_rbv':self.scan_X_data_rbv,
                            "timestamp":self.scan_timestamp_list}
        Norm_Y_data=self.normalize_Y_data(self.active_data_dict)
        # plot scan data
        self.plot_scan_data(x_data=full_X_data, y_data=Norm_Y_data)
            
        # check if should start next scan round again
        self.curr_scan_num += 1
        if self.curr_scan_num<self.total_scan_num:
            # start next scan round
            self.scan_start_sig.emit([self.curr_scan_num,"Set_X"])
            self.set_progress_Bar(int(100*self.curr_scan_num/self.total_scan_num))
        elif self.curr_scan_num==self.total_scan_num:
            # scan done
            self.set_progress_Bar(100)
            done_msg=f'{self.scanX_name} scan process done'
            print(done_msg)
            logger.info(done_msg)
            self.scan_cost_timer.stop()
            self.scan_start_sig.disconnect(self.set_X_PV)
            self.scan_started_flag=False
            # save all scan data automatically
            full_data=self.get_full_data()
            t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
            self._save_N += 1
            filename = f'GR_counts_data_{t_stamp}_{self._save_N}'
            folder = time.strftime('%Y-%m-%d', time.localtime())
            save_folder = createPath(os.path.join(save_path, folder))
            self.save_scan_data(full_data, save_folder, filename)
            # show on msg box
            time_cost=time.time()-self.scan_start_time
            done_info=f'scan {self.scanX_name} finished successfully!\n Total scan num:{self.curr_scan_num}\n\
            Time cost:{time_cost:.2f}~{str(datetime.timedelta(seconds=time_cost))}\n\
            save to path:{save_path}'
            self.done_msgbox=MyMsgBox('Channel Scan done', f'Scan on {self.scanX_name} finished', details=done_info, signal=0)
            self.done_msgbox.show()

    def normalize_Y_data(self,data_dict:dict):
        """normalize the active_data_dict into accessable data:
        normized_dict_form= {"TEY":[datalist],"PD":[datalist],"Au":[datalist],"Normalized":[datalist]}

        Args:
            data_dict (dict): active_data_dict={ch_name:[datalist]}

        Returns:
            _type_: _description_
        """
        Normailed_Y_data={}
        label_list=["TEY","Au","PD"]
        for ch_name,ch_datalist in data_dict.items():
            for label in label_list:
                if re.search(label,ch_name):
                    Normailed_Y_data[label]=ch_datalist
        # normalized data by normalized_data=-log(TEY/Au)
        Norm_data=np.log(np.array(Normailed_Y_data["Au"])/np.array(Normailed_Y_data["TEY"]))
        Normailed_Y_data["Normalized"]=Norm_data.tolist()
        return Normailed_Y_data


    """
    end of the scan process part
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************


    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    plot and save scan data
    """
    def __ini_plot(self):
        self.figure = Myplot()
        # add NavigationToolbar in the figure (widgets)
        self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.Main_fig_box)
        self.gridlayout.addWidget(self.figure)
        self.gridlayout.addWidget(self.fig_ntb)
        self.X_axis_set_cbx.currentIndexChanged.connect(self.update_figure)
        self.Y_axis_set_cbx.currentIndexChanged.connect(self.update_figure)

    @Slot()
    def update_figure(self):
        """update the scan plot set and plot new figure 
        """
        #print(f'now update figure with {self.active_data_dict.items()}')
        if self.scan_range_set_flag==1 or self.scan_started_flag:
            full_X_data={f'{self.scanX_name}_set':self.scan_X_data_set,f'{self.scanX_name}_rbv':self.scan_X_data_rbv,
                            "timestamp":self.scan_timestamp_list}
            Norm_Y_data=self.normalize_Y_data(self.active_data_dict)
            # plot scan data
            self.plot_scan_data(x_data=full_X_data, y_data=Norm_Y_data)
        else:
            print(f'Current Axis:\nX-axis:{self.X_axis_set_cbx.currentText()} Y-axis:{self.Y_axis_set_cbx.currentText()}')

    def plot_scan_data(self,x_data:dict, y_data:dict):
        """plot the scan data according the plot set

        Args:
            x_data (dict): X_datadict={"ch_name_set":[datalist],"ch_name_rbv":[datalist],"timestamp":[datalist]}
            y_data (dict): Y_datadict={"TEY":[datalist],"PD":[datalist],"Au":[datalist],"Normalized":[datalist]}
        """
        self.figure.axes.cla()
        #  x_list ["ReadBack","SetPoint","timestamp"]
        x_list=x_data[f'{self.scanX_name}_set'] # default is the set value list
        if self.X_axis_set_cbx.currentText()=="ReadBack":
            x_list=x_data[f'{self.scanX_name}_rbv']
        elif self.X_axis_set_cbx.currentText()=="Timestamp":
            x_list=x_data['timestamp']
        else:
            pass
        # for Y list
        y_axis=self.Y_axis_set_cbx.currentText() # ["TEY","Au","PD","Normalized"]
        y_list=y_data[y_axis]
        self.figure.axes.plot(x_list, y_list, marker='o', markersize=4, markerfacecolor='orchid',
                               markeredgecolor='orchid', linestyle='-', color='c',label=y_axis)
        if y_axis=="Normalized":
            self.figure.axes.plot(x_list, y_data["TEY"], marker='*', markersize=4, markerfacecolor='limegreen',
                                markeredgecolor='limegreen', linestyle=':', color='m',label="TEY")
            self.figure.axes.plot(x_list, y_data["Au"], marker='s', markersize=4, markerfacecolor='lightsalmon',
                                markeredgecolor='lightsalmon', linestyle='--', color='C1',label="Au")
        self.figure.axes.legend()
        # draw and plot
        self.figure.axes.set_xlabel(self.scanX_name, fontsize=16, color='m')
        self.figure.axes.set_ylabel(y_axis, fontsize=16, color='m')
        self.figure.draw()


    def get_full_data(self):
        """
        get the full scan data and return
        data structure:
        full_data_dict={"name":[datalist]}

        :return: full valid scan data(not empty) in dict form
        """
        valid_full_data = dict()
        active_full_data={f'{self.scanX_name}_set':self.scan_X_data_set,f'{self.scanX_name}_rbv':self.scan_X_data_rbv,
                            "timestamp":self.scan_timestamp_list}
        #add channel data
        active_full_data.update(self.active_data_dict)
        # get the valid scan data (not empty)
        for key, value in active_full_data.items():
            if value:
                valid_full_data[key] = value
        return valid_full_data

    # clear all scan data
    def clear_all_data(self):
        """
        clear all previous data
        :return:
        """
        self.scan_X_data_set=[]
        self.scan_X_data_rbv=[]
        self.scan_timestamp_list=[]
        for ch_name,ch_data in self.active_data_dict.items():
            print(f'clear all data in {ch_name}')
            self.active_data_dict[ch_name]=[]
        

    # save scan data
    def save_scan_data(self, full_data: dict, path, filename):
        """
        save the full data into several file form [dict] form
        :param filename: filename without extension
        :param path: filepath
        :param full_data: {'counts':[list],'Energy':[list]....}
        :return:
        """
        if full_data and os.path.isdir(path):
            dict_to_csv(full_data, path, filename + '.csv')
            dict_to_excel(full_data, path, filename + '.xlsx')
            # dict_to_json(full_data, path, filename + '.json')
            dict_to_SQLTable(full_data,filename, SQLiteDB_path, 'ALLScanData.db')
            QMessageBox.information(self, 'save file', f'full data have been saved to {path}', QMessageBox.Yes)

    def usr_save_full_data(self, full_data: dict, path: str, usrname='usr_test', usr_define: int = 1):
        """
        check all the data acquired now,save all valid data
        :param usrname: usr defined filename
        :param path: filepath
        :param filename: filename without extension
        :param usr_define: usr define save path and filename->1=yes,0=no
        :return:
        """
        t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
        self._save_N += 1
        filename = usrname + t_stamp + str(self._save_N)
        usr_path = path if os.path.isdir(path) else save_path
        print(filename, usr_path)
        file_in_path = None
        filetype = None
        # save scan data
        if full_data:
            if usr_define == 1:
                file_in_path, filetype = QFileDialog.getSaveFileName(self, 'save file', usr_path, 'xlsx(*.xlsx)')
                usr_path = os.path.dirname(file_in_path)
                usr_file = os.path.basename(file_in_path)
                filename = usr_file.split('.')[0]
            self.save_scan_data(full_data, usr_path, filename)
        else:
            if usr_define == 1:
                self.raise_info(f'No data to save')
            else:
                pass

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************



            






    """
    end of Scan process part
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
