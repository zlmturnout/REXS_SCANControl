import time, random, sys, os, math, datetime, traceback
import pandas as pd
from PySide6.QtCore import Qt,Signal,Slot,QTimer,QThread
from PySide6.QtWidgets import QTreeView,QTreeWidget,QTreeWidgetItem,QHBoxLayout,QHeaderView,QWidget
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox
# import MCCDAQ lib mcculw
from mcculw import ul
from mcculw.enums import ULRange, InterfaceType
from mcculw.ul import ULError, get_net_device_descriptor, create_daq_device
from mcculw.device_info import DaqDeviceInfo
sys.path.append('.')
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
from UI_ADC_widget import Ui_Form

# QThread to read data from DAQ E-1608
class E1608QThread(QThread):
    """
    Work QThread to read data from ADC type MCC E-1608
    """
    data_sig = Signal(list)

    def __init__(self, channel: int = 0, ul_range_n: int = 3, repeat_n: int = 1, t_interval: float = 0.1,
                 board_num:int=0,keep_on: int = 0, host='10.30.95.167',port = 54211):
        """
        read the output signal from channel,and repeat n times for average,time_interval 0.1s
        :param channel:
        :param repeat_n:
        :param t_interval:
        """
        #QThread.__init__(self)
        super().__init__()
        self.channel = channel
        self.repeat_n = repeat_n
        self.t_interval = t_interval
        self.t_ms = int(self.t_interval * 1000)
        self.host = host
        self.port = port
        self.board_num = board_num
        self.ul_range_list = [ULRange.BIP1VOLTS, ULRange.BIP2VOLTS, ULRange.BIP5VOLTS, ULRange.BIP10VOLTS]
        self.UL_range = self.ul_range_list[ul_range_n]
        ul.ignore_instacal()
        self.run_flag = True
        # 0 is run once, 1 is keep on monitoring until runtime runs out.
        self.keep_on = keep_on
        self.__ini_device()

    def __del__(self):
        self.keep_on = 0
        self._run_flag=False
    
    def __ini_device(self):
        try:
            self.device = get_net_device_descriptor(self.host, self.port, 5)
            create_daq_device(self.board_num, self.device)
        except Exception as e:
            print(traceback.format_exc()+str(e))
            self.run_flag = False
        else:
            self.run_flag = True


    def run(self):
        t0 = time.time()
        run_time = 3600
        while self.run_flag and time.time() - t0 < run_time:
            read_value = []
            sum_value = 0
            try:
                i = 0
                while i < self.repeat_n:
                    self.msleep(self.t_ms)
                    # Get a value from the device
                    # Use the a_in method for devices with a resolution <= 16
                    value = ul.a_in(self.board_num, self.channel, self.UL_range)
                    # Convert the raw value to engineering units
                    eng_units_value = ul.to_eng_units(self.board_num, self.UL_range, value)
                    read_value.append(eng_units_value)
                    sum_value += eng_units_value
                    i += 1
            except Exception as e:
                print(e)
            finally:
                average_value = float('{:.3f}'.format(sum_value / self.repeat_n))
                # emit list form [[x,x,x,x,x],average]
                all_read = read_value
                self.data_sig.emit([all_read, average_value])
                print(f'emit data info: {[all_read, average_value]}')
                self.msleep(100)
                if self.keep_on == 0:
                    print('set run flag to False')
                    ul.release_daq_device(self.board_num)
                    self.run_flag = False


class ADCMonitor(QWidget,Ui_Form):
    """Monitor ADC read ,plot the data by time
    emit data if neded

    example:
    """
    emit_data_sig=Signal(float)

    def __init__(self, parent =None, ADCname:str=None,host:str='10.30.95.167',port:int=54211,
        board_num:int=0,channel: int = 0, ul_range_n: int = 3, repeat_n: int = 1, t_interval: float = 0.1,keep_on: int = 0,emit_data=True) -> None:
        super(ADCMonitor,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f'{ADCname} Monitor ')
        self.adc_name=ADCname
        self.Device_label.setText(ADCname)
        self.host=host
        self.port=port
        self.channel=channel
        self.board_num=board_num
        self.ul_range_num=ul_range_n
        self.repeat_n=repeat_n
        self.t_interval=t_interval
        ul.ignore_instacal()
        self.run_flag = True
        # 0 is run once, 1 is keep on monitoring until runtime runs out.
        self.keep_on = keep_on
        self.emit_data=emit_data
        self.__ini_monitor()
        self.__init__matplotlib()
        self.__init__datasave()
        self.Channel_cbx.currentIndexChanged['int'].connect(self.set_channel)
        self.Range_cbx.currentIndexChanged['int'].connect(self.set_ulRange)


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
        self.data_fig_ax.set_title(self.tagname,color='#ff5500')
        self.data_fig_ax.figure.autofmt_xdate(rotation=25)
        self.data_fig_ax.figure.canvas.draw()

#  end of data plot part by matplotlib
# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    #  start of UL_range and channel set part
    @Slot(int)
    def set_channel(self,ch_num:int):
        self.channel=ch_num

    @Slot(int)
    def set_ulRange(self,ul_num:int):
        """set the volts range of adc device
        UL_range=[ULRange.BIP1VOLTS, ULRange.BIP2VOLTS, ULRange.BIP5VOLTS, ULRange.BIP10VOLTS]
        self.UL_range = self.ul_range_list[ul_range_n]
        Args:
            uL_num (int): _description_
        """
        self.ul_range_num = ul_num

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

        
    @Slot()
    def on_Start_monitor_btn_clicked(self):
        """start adc monitor
        """
        if not self.monitor_on_flag:
            print(self.ul_range_num)
            self.start_time=time.time()
            self._DaqQthread=E1608QThread(channel=self.channel,ul_range_n=self.ul_range_num,host=self.host,
                port=self.port,board_num=self.board_num,keep_on=1,repeat_n=self.repeat_n,t_interval=self.t_interval)
            self._DaqQthread.data_sig.connect(self.get_ReadValue)
            self._DaqQthread.start()
            self.monitor_on_flag=True
        else:
            print(f'{self.adc_name} already monitoring')
    
    @Slot(list)
    def get_ReadValue(self,read_list:list):
        """_summary_

        Args:
            data_list (list): Form:[[x1,x2,x3,x4],x]=[all_read, average_value]
        """
        if isinstance(read_list[-1],float):
            new_value=read_list[-1]
            t_elapse=time.time()-self.start_time
            self.data_list.append(new_value)
            self.time_list.append(t_elapse)
            self.timestamp_list.append(get_datetime())
            # decide wether emit data  or not
            if self.emit_data:
                self.emit_data_sig.emit(new_value)
            # plot the data verus time
            max_length=200
            if len(self.data_list)>max_length:
                data_list=self.data_list[-max_length:]
                time_list=self.time_list[-max_length:]
            else:
                data_list=self.data_list
                time_list=self.time_list
            
            # plot the changes
            self.plot_read_data(x_list=time_list,y_list=data_list,x_name='time',y_name='volts(V)')

    @Slot()
    def on_Stop_monitor_btn_clicked(self):
        if self.monitor_on_flag:
            self.monitor_on_flag=False
            self._DaqQthread.__del__()
    
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
         save_header=self.pvname.replace(":","_")
         filename=f'{save_header}-{cur_datetime}N{self.datasave_num}'
         today_folder=createPath(os.path.join(save_path,time.strftime('%Y-%m-%d', time.localtime())))
         self.save_all_data(all_valid_data,today_folder,filename)
        
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


    def save_all_data(self,full_data:dict,path,filename):
        """save all sensor data
        save to excel xlsx,json,csv and sqlite database
        Args:
            full_data[dict]: full data in dict
            path: save path
            filename: filename
        """
        if full_data and os.path.isdir(path):
            dict_to_csv(full_data, path, filename + '.csv')
            dict_to_excel(full_data, path, filename + '.xlsx')
            #dict_to_json(full_data, path, filename + '.json')
            dict_to_SQLTable(full_data,filename, SQLiteDB_path, 'PVMonitorData.db')
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
            self.monitor_on_flag=False
            self._DaqQthread.__del__()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ADCMonitor(ADCname="REXS_Au",host='10.30.95.167',port=54211,
        board_num=0,channel= 0, ul_range_n= 0)
    win.show()
    sys.exit(app.exec())
        




        




