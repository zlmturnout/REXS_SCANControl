import time, random, sys, os, math, datetime, traceback
import pandas as pd
from PySide6.QtCore import Qt,Signal,Slot,QTimer,QThread
from PySide6.QtWidgets import QTreeView,QTreeWidget,QTreeWidgetItem,QHBoxLayout,QHeaderView,QWidget
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox
from socket import *
sys.path.append('.')
# SCIP cmd for pA6517B
from Architect.SCIP_CMD_6517B import *
# data save part
from resource.Dict_DataFrame_Sqlite import dict_to_csv,dict_to_excel,dict_to_json,dict_to_SQLTable
from resource.Tools_functions import createPath,get_datetime
# matplotlib
from matplotlib.backends.backend_qtagg import(FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

# save path
DATA_PATH = os.getcwd()
save_path = os.path.join(DATA_PATH, 'save_data')
createPath(save_path)
# data base
SQLiteDB_path=createPath(os.path.join(save_path,'database'))
#today_folder=createPath(os.path.join(save_path,time.strftime('%Y-%m-%d', time.localtime())))

# UI import
from UI_pAmeter_widget import Ui_Form

HOST = '10.30.95.170'
Port_list = [23, 26, 29, 32]  # port in USR_N540,26 is for keithley 6517B
BUFSIZ = 1024
NPLC_list=[0.01,0.1,1,5,10] # nplc for pAmeter read speed

"""
worker Qthread for reading current[aA~mA] from Keithley 6517B electrometer
"""
# basic logic to measure current by Keithley 6517b
# *CLS (clear status)
cmd_cls = '*CLS'
# reset 6517B
cmd_RST = '*RST'
# zero check status
cmd_zch = ':SYSTem:ZCHeck?'  # 0 is OFF , 1 is ON
# configure measure current
cmd_config_CURR = ':CONFigure:CURR:DC'
# set filter type=advance mode=average  counts=5  noise=1% and median OFF
cmd_curr_aver = ':SENS:CURR:AVERage:TCONtrol?'
# initiate continues on
cmd_initiate = ':INITiate'  # take the Model 6517B out of the idle state wait 1s
# return a new value
cmd_get_newval = ':SENS:DATA:FRESh?'
# data type [re.fullmatch(r'([+\-0-9E.]+)[A-Z]{4}', result[0])]
test_data = '+198.4891E-12NADC,+0007633.858813secs,+58454RDNG#\r\n'


class Keithley6517BCom(QThread):
    """
        worker Qthread for communicating with Keithley 6517B electrometer,using serial port
        emit signal current data when complete:[average,all currents,info]
        function:read currents implemented
        """
    data_sig = Signal(list)

    def __init__(self, address: tuple, func: str, points: int = 5, delay: float = 0.1, full_time: float = 1000,
                 keep_on: int = 0, nplc: int = 1,
                 parent=None):
        #QThread.__init__(self, parent)
        super(Keithley6517BCom, self).__init__(parent)
        self.address = address
        self.func = func
        self.points = points
        self.delay = delay
        self.nplc = nplc
        self.monitor_time = full_time  # monitor for 1000s
        self.run_flag = True
        self._keep_on = keep_on
        print(f'keep on =={keep_on}')
        self.response_msg = ''
        self.initiate_state_flag=False # pAmeter has initiate(True) or not(False)
        self.current_nplc(nplc=self.nplc)

    def __del__(self):
        self.run_flag = False

    def cmd_send(self, cmd: str, wait: int = 100, receive_flag=True):
        """
        send cmd to the keithley address, get the response and return
        start tcp client,set up connection to the sever USR_N540,
        send msg and return when get response message
        :param receive_flag: if true receive and return, else wait and return NONE
        :param wait: wait [100]ms before the cmd is write
        :param cmd:
        :return:
        """
        self.send_msg = (cmd + '\r\n').encode('utf-8')
        self.socket_TCP = socket(AF_INET, SOCK_STREAM)
        self.socket_TCP.settimeout(2.0)  # set timeout
        try:
            self.socket_TCP.connect(self.address)
        except Exception as e:
            error_info = traceback.format_exc()
            print(error_info)
        else:
            self.connect_flag = True
            self.socket_TCP.send(self.send_msg)
            self.msleep(wait)
            t_start = time.time()
            while self.connect_flag and receive_flag and time.time() - t_start < 10:
                resp = self.socket_TCP.recv(BUFSIZ)
                if resp:
                    self.response_msg = resp.decode('utf-8')
                    # print(f'response:{self.response_msg} from address:{self.address}')
                    break
        finally:
            # self.connect_flag = True
            self.socket_TCP.close()
            return self.response_msg

    @property
    def deviceID(self):
        deviceID = self.cmd_send(cmd_ID)
        return deviceID

    @property
    def version(self):
        return self.cmd_send(cmd_version)

    def reset(self):
        self.cmd_send(cmd_RST, wait=1000, receive_flag=False)

    def clear_status(self):
        self.cmd_send(cmd_cls, wait=1000, receive_flag=False)

    def zero_check(self, status: str = 'ON'):
        """
        set zero check mode, OFF is off, ON is on
        :param status:
        :return:
        """
        if status == 'ON':
            self.cmd_send(cmd_zch_on, receive_flag=False)
        elif status == 'OFF':
            self.cmd_send(cmd_zch_off, receive_flag=False)

    def configure_current(self, AutoRange: int = 1, Range: float = 0.01, nplc: float = 1, Digits: int = 7):
        """
        :SENS:FUNC 'CURR'
        configure measure current
        :param AutoRange: auto range 0 is off,1 is on
        :param Range: 0-21e-3 A
        :param nplc: 0.01,1,10, fast,median,low
        :param Digits: add [val]:4=3.5,5=4.5, 6=5.5, 7=6.5,
        :return:
        """
        cmd_setRange = ''
        if AutoRange == 1:
            cmd_setRange = cmd_curr_AutoRange + str(AutoRange)
        elif AutoRange == 0:
            cmd_setRange = cmd_curr_AutoRange + str(AutoRange) + ';' + cmd_curr_RangeSet + str(Range)
        cmd = cmd_sens_curr + ';' + cmd_setRange + ';' + cmd_curr_dig + str(
            Digits) + ';'
        self.cmd_send(cmd, wait=300, receive_flag=False)

    def current_nplc(self,nplc):
        """

        set the nplc for current measurement 0.01,1,10=Fastest,Normal,Slowest
        :param nplc:
        :return:
        """
        cmd=cmd_curr_nplc + str(nplc)
        wait = 1000 if self.nplc == 10 else 2000
        self.cmd_send(cmd, wait=wait, receive_flag=False)

    def current_filter(self, useFilter=True, FilterType='ADV', AverConTr='REP'):
        """
        configure the current filter,
        :param useFilter: True:ON,False:OFF
        :param FilterType: SCALar or ADVanced
        :param AverConTr: REPeat or MOVing
        :param averCount: average over 1-100
        :param Noise: +/- [val]% val:1-100
        :param MediaMode: True is On, False is OFF
        :return:
        """
        cmd_filter = cmd_curr_filterON if useFilter else cmd_curr_filterOFF
        cmd_FilterType = cmd_curr_aver_typeADV if FilterType == 'ADV' else cmd_curr_aver_typeSCAL
        cmd_AverConTr = cmd_curr_averREP if AverConTr == 'REP' else cmd_curr_averMOV
        #cmd_curr_aver_noiseToL = cmd_curr_aver_Noise_N + str(Noise)
        # write the cmd
        self.cmd_send(cmd_filter,wait=500,receive_flag=False)
        cmd =cmd_FilterType + ';' + cmd_AverConTr + ';'
        print(cmd)
        self.cmd_send(cmd, wait=500, receive_flag=False)
        # remove filter
        self.cmd_send(cmd_curr_filterOFF,wait=200,receive_flag=False)

    def curr_medianMode(self,MediaMode=False):
        """
        cmd=SENS:CURRent:median:STATe ON/OFF
        medianMode On or OFF
        :return:
        """
        cmd_curr_medianMode = cmd_curr_medianON if MediaMode else cmd_curr_medianOFF
        self.cmd_send(cmd_curr_medianMode,wait=200,receive_flag=False)


    def curr_aver_counts(self, num: int = 5):
        """
        cmd=:SENS:CURR:AVERage:Count [num]
        set the average num in filter
        :param num:
        :param counts:
        :return:
        """
        cmd = cmd_curr_aver_Num + str(num)
        self.cmd_send(cmd, wait=100, receive_flag=False)

    def initiate(self):
        """
        cmd=:INITiate
        take the Model 6517B out of the idle state
        :return:
        """
        self.cmd_send(cmd_initiate, wait=100, receive_flag=False)

    def initiate_continuous(self, continu=True):
        """
        cmd=:INITiate:CONTinuous ON/OFF
        Enable/Disable continuous initiation
        True=Enable,False=Disable
        :param continu:
        :return:
        """
        cmd = cmd_ini_continuON if continu else cmd_ini_continuOFF
        self.cmd_send(cmd, wait=100, receive_flag=False)

    # configure measure function
    def conf_function(self, func='current'):
        """
        function:CURRent[:DC]: Amps function
                RESistance: Ohms function
                CHARge: Coulombs function
                VOLTage[:DC]:default voltage
        :return:
        """
        if func == 'current':
            cmd_conf_func = ':CONFigure:CURRent:DC;'
        elif func == 'resistance':
            cmd_conf_func = ':CONFigure:RESistance;'
        elif func == 'charge':
            cmd_conf_func = ':CONFigure:CHARge;'
        else:
            cmd_conf_func = ':CONFigure:VOLTage:DC;'
        self.cmd_send(cmd_conf_func, wait=100, receive_flag=False)

    # common cmd for measurement
    # Signal-oriented measurement commands
    def fetch(self, wait: int = 100):
        """
        cmd=:FETCH?
        Requests the latest reading
        :return:
        """
        result = self.cmd_send(cmd_fetch, wait=wait, receive_flag=True)
        return result

    def _MEAs(self, wait: int = 100):
        """
        Performs an :ABORt, :CONFigure:<function>, and a :READ?
        NOT recommended
        :return:
        """
        return self.cmd_send(cmd_mea, wait=wait, receive_flag=True)

    def read_data(self, wait: int = 100):
        """
        Performs an :ABORt, :INITiate, and a :FETCh?
        :return:
        """
        return self.cmd_send(cmd_read, wait=wait, receive_flag=True)

    def fresh_data(self, wait: int = 100):
        """
        cmd=:SENS:DATA:FRESh?
        get a new value from readings
        :return:
        """
        return self.cmd_send(cmd_get_newval, wait=wait, receive_flag=True)

    @staticmethod
    def get_value(resp: str):
        """
        test_data='+198.4891E-12NADC,+0007633.858813secs,+58454RDNG#\r\n'
        :param resp:
        :return:0 if wrong, else currents  in Amps
        """
        data_value = 0
        if resp:
            # val = re.fullmatch(r'([+\-0-9E.]+)[A-Z]{4}', resp.split(',')[0])
            # data_value = float(val.group(1))
            val=resp.split(',')[0].split('NADC')
            data_value = float(val[0])
        #print(f'get new read:{data_value}A')
        return data_value

    def run(self):
        print(self.func)
        t0 = time.time()
        status = 'OK'
        pA_currents=0
        # measure current
        if self.func == 'currents':
            if not self.initiate_state_flag:
                self.current_nplc(nplc=self.nplc)
                self.curr_aver_counts(num=self.points)
                self.zero_check(status='OFF')
                self.initiate_state_flag=True
            while self.run_flag and time.time() - t0 < self.monitor_time:
                try:
                    resp = self.fresh_data()
                    pA_currents = self.get_value(resp)
                    status = 'error' if pA_currents == 0 else 'OK'
                except Exception as e:
                    error_info = traceback.format_exc()
                    print(error_info+str(e))
                finally:
                    #print(f'start emit:{[pA_currents, pA_currents, status]}')
                    self.data_sig.emit([pA_currents, pA_currents, status])
                if self._keep_on == 0:
                    self.run_flag = False
    
    def __del__(self):
        self._keep_on = 0
        self.run_flag=False
    
    def close(self):
        self.run_flag=False

class pAMeterMonitor(QWidget,Ui_Form):
    """Monitor pAmeter read ,plot the data by time
    emit data if required

    example:
    """
    emit_data_sig=Signal(str,float)
    close_sig=Signal(str)

    def __init__(self, parent =None, pAname:str=None,address:tuple=('10.30.95.167',54211),
        func: str='currents', points: int = 5, delay: float = 0.1, full_time: float = 10000,keep_on: int = 0, nplc: int = 1,emit_data:bool=True) -> None:
        super(pAMeterMonitor,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f'{pAname} Monitor ')
        self.pA_name= pAname
        self.Device_label.setText(pAname)
        self.address=address
        self.func=func
        self.points=points
        self.delay=delay
        self.full_time=full_time
        self.nplc=nplc
        self.run_flag = True
        # 0 is run once, 1 is keep on monitoring until runtime runs out.
        self.keep_on = keep_on
        self.emit_data=emit_data
        self.__ini_monitor()
        self.__init__matplotlib()
        self.__init__datasave()
        #self.Channel_cbx.currentIndexChanged['int'].connect(self.set_channel)
        #self.Range_cbx.currentIndexChanged['int'].connect(self.set_ulRange)
        self.ZCHK_rbtn.toggled["bool"].connect(self.zero_check)
        self.NPLC_cbx.currentIndexChanged['int'].connect(self.set_nplc)
        #self.Channel_cbx.setCurrentIndex(self.channel)
        self.NPLC_cbx.setCurrentIndex(NPLC_list.index(self.nplc))


# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    #  start of data plot part by matplotlib
    def __init__matplotlib(self):
        """Initialize matplotlib plot part
        """
        Figure_Canvas=FigureCanvas(Figure(figsize=(4,3)))
        self.verticalLayout_plot.addWidget(Figure_Canvas)
        self.verticalLayout_plot.addWidget(NavigationToolbar(Figure_Canvas,self))
        self.data_fig_ax=Figure_Canvas.figure.subplots()
        
    def plot_read_data(self, x_list: list, y_list: list, x_name: str, y_name: str):
        """
        plot any x_list and y_list data,and set the Axis name x_name,y_name
        :param x_list:
        :param y_list:
        :param x_name:
        :param y_name:
        :return:
        """
        # plot
        self.data_fig_ax.cla()
        self.data_fig_ax.plot(x_list, y_list, marker='o', markersize=2, markerfacecolor='orchid',
                                   markeredgecolor='orchid', linestyle='-', color='c')
        self.data_fig_ax.set_xlabel(x_name, fontsize=12, color='m')
        self.data_fig_ax.set_ylabel(y_name, fontsize=12, color='m')
        self.data_fig_ax.set_title(self.pA_name,color='#ff5500')
        self.data_fig_ax.figure.autofmt_xdate(rotation=25)
        self.data_fig_ax.figure.canvas.draw()

#  end of data plot part by matplotlib
# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    #  start of UL_range and channel set part
    @Slot(bool)
    def zero_check(self,checked:bool):
        print(f'zero check:{checked}')
        if self.monitor_on_flag and checked:
            #stop monitor
            self.monitor_on_flag=False
            #self._DaqQthread.__del__()
            self._DaqQthread.close()
            self._DaqQthread.initiate_state_flag=False
            self._DaqQthread.zero_check("ON")
        elif not self.monitor_on_flag and not checked:
            self._DaqQthread.zero_check("OFF")

    @Slot(int)
    def set_nplc(self,index:int):
        """set the nplc of pA meter
        nplc=[0.01,0.1,1,5,10] means fasteses->slowest

        Args:
            index (int): 
        """
        nplc=NPLC_list[self.NPLC_cbx.currentIndex()]
        print(f'current nplc: {nplc}')
        self.nplc=nplc

    #  end of UL_range and channel set part
# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    #  start of action and data-acquisition-plot part
    
    def __ini_monitor(self):
        # for data save list
        self.data_list=list()
        self.time_list=list()
        self.timestamp_list=list()
        self.monitor_on_flag=False
        self.start_time=time.time()
        self.hide_details_flag=True
        self.Details_box.hide()

        
    @Slot()
    def on_Start_monitor_btn_clicked(self):
        """start pAmeter monitor
        """
        self.start_monitor()
        
    def start_monitor(self):
        #clear old data
        self.data_list=[]
        self.time_list=[]
        self.timestamp_list=[]
        if not self.monitor_on_flag:
            self.start_time=time.time()
            try:
                self._DaqQthread=Keithley6517BCom(address=self.address,func=self.func,points=self.points,delay=self.delay,
                full_time=self.full_time,keep_on=self.keep_on,nplc=self.nplc)
                self._DaqQthread.data_sig.connect(self.get_ReadValue)
                self._DaqQthread.start()
            except Exception as e:
                print(traceback.format_exc()+str(e))
        else:
            print(f'{self.pA_name} already monitoring')
    
    @Slot()
    def on_Details_btn_clicked(self):
        if self.hide_details_flag:
            self.Details_box.show()
            self.Details_btn.setText("<-->")
            self.hide_details_flag=False
        else:
            self.Details_box.hide()
            self.Details_btn.setText(">--<")
            self.hide_details_flag=True

    def lcd_display(self,current:'int|float'):
        """display current by uA, nA or pA

        Args:
            current (_type_): _description_

        Returns:
            _type_: _description_
        """
        lcd_value=-1.0
        if current*1.0e6>=1:
            # > 1uA
            lcd_value=current*1.0e6
            self.Current_label.setText('uA')
        elif current*1.0e6<1 and current*1.0e9>=1:
            # 1nA~1uA
            lcd_value=current*1.0e9
            self.Current_label.setText('nA')
        else:
            # < 1nA
            lcd_value=current*1.0e12
            self.Current_label.setText('pA')
        self.lcd_pA.display(lcd_value)


    @Slot(list)
    def get_ReadValue(self,read_list:list):
        """_summary_

        Args:
            data_list (list): Form:[pA_currents, pA_currents, status] 
            status='error'|'OK'
        """
        self.monitor_on_flag=True 
        if read_list[-1]=='OK':
            new_value=read_list[0]
            self.lcd_display(new_value)
            t_elapse=time.time()-self.start_time
            self.data_list.append(new_value)
            self.time_list.append(t_elapse)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.timestamp_list.append(timestamp)
            # decide wether emit data  or not
            if self.emit_data:
                self.emit_data_sig.emit(self.pA_name,new_value)
            # plot the data verus time
            max_length=200
            if len(self.data_list)>max_length:
                data_list=self.data_list[-max_length:]
                time_list=self.time_list[-max_length:]
            else:
                data_list=self.data_list
                time_list=self.time_list
            
            # plot the changes
            self.plot_read_data(x_list=time_list,y_list=data_list,x_name='time/s',y_name='currents(pA)')


    @Slot()
    def on_Stop_monitor_btn_clicked(self):
        print(f'monitor status: {self.monitor_on_flag}')
        if self.monitor_on_flag:
            self.monitor_on_flag=False
            #self._DaqQthread.__del__()
            self._DaqQthread.close()
            self._DaqQthread.initiate_state_flag=False
    
    #  end of action and data-acquisition-plot part
# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    
            
# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    #  start of data save and close part            

    def __init__datasave(self):
        self.datasave_timer=QTimer()
        self.datasave_timer.timeout.connect(self.routine_data_save)
        self.datasave_timer.start(1000*600) # auto save data every 10min
        self.datasave_num=0
        self._usr_save_N=0

    @Slot()
    def on_Savedata_btn_clicked(self):
        """save data to file
        """
        print("Saved data to file")
        all_valid_data = self.get_full_data()
        data_path=os.path.join(save_path,'save_data')
        self.usr_save_full_data(all_valid_data,data_path,usr_define=1)
    
    def routine_data_save(self):
         self.datasave_num+=1
         all_valid_data = self.get_full_data()
         cur_datetime=time.strftime("%Y-%m-%d-%H-%M", time.localtime())
         save_header=self.pA_name.replace(":","_")
         filename=f'{save_header}-{cur_datetime}N{self.datasave_num}'
         today_folder=createPath(os.path.join(save_path,time.strftime('%Y-%m-%d', time.localtime())))
         routine_folder=createPath(os.path.join(today_folder,"pAMonitorMonitorData"))
         self.save_all_data(all_valid_data,routine_folder,filename,filetype=('excel',"sqlite"))
        
    def get_full_data(self):
        """
        get all the data whcih is not empty
        """
        valid_full_data=dict()
        read_fulldata={"time_elapsed(s)":self.time_list,"volts(V)":self.data_list,"timestamp":self.timestamp_list}
        # get the valid scan data (not empty)
        for key, value in read_fulldata.items():
            if value:
                valid_full_data[key] = value
        return valid_full_data


    def save_all_data(self,full_data:dict,path,filename,filetype:tuple=("excel","csv","sqlite","json")):
        """save all sensor data
        save to excel xlsx,json,csv and sqlite database
        Args:
            full_data[dict]: full data in dict
            path: save path
            filename: filename
            filetype:tuple(excel,csv,sqlite,json)
        """
        if full_data and os.path.isdir(path):
            if "csv" in filetype:
                dict_to_csv(full_data, path, filename + '.csv')
            if "excel" in filetype:
                dict_to_excel(full_data, path, filename + '.xlsx')
            if "sqlite" in filetype:
                dict_to_SQLTable(full_data,filename, SQLiteDB_path, 'PAMonitorData.db')
            if "json" in filetype:
                dict_to_json(full_data, path, filename + '.json')
            details=f'save to excel/csv/json files.\nFilename:{path+filename}\nSqlite database:{SQLiteDB_path}/SensorData.db\ntablename:{filename}'
            print(details)
            

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
        self._usr_save_N += 1
        filename = f'{usrname}_{t_stamp}_N{self._usr_save_N}'
        usr_path = path if os.path.isdir(path) else save_path
        print(filename, usr_path)
        # save full data
        if full_data:
            if usr_define == 1:
                file_in_path, filetype = QFileDialog.getSaveFileName(self, 'save file', usr_path, 'xlsx(*.xlsx)')
                usr_path = os.path.dirname(file_in_path)
                usr_file =  os.path.basename(file_in_path)
                filename = usr_file.split('.')[0]
            self.save_all_data(full_data, usr_path, filename)
        else:
            if usr_define == 1:
                print(f'No data to save')
            else:
                pass

#  end of data save part             
# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    #close event
    
    def closeEvent(self, event):
        if self.monitor_on_flag:
            
            # self.monitor_on_flag=False
            # self._DaqQthread.__del__()
            # self.close_sig.emit(self.pA_name)
            event.ignore()
            #event.accept()
        else:
            event.accept()
            self.close_sig.emit(self.pA_name)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = pAMeterMonitor(pAname="REXS_Au",address=('10.30.95.170',26),func='currents', points= 5, delay= 0.1, 
        full_time = 10000,keep_on = 1, nplc= 0.1,emit_data=True)
    win.show()
    sys.exit(app.exec())
        




        




