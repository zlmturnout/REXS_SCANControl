from calendar import c
from epics import ca, caget, cainfo, camonitor, caput, PV, camonitor_clear, get_pv
import time, random, sys, os, math, datetime, traceback
import pandas as pd
from PySide6.QtCore import Qt,Signal,Slot,QTimer
from PySide6.QtWidgets import QTreeView,QTreeWidget,QTreeWidgetItem,QHBoxLayout,QHeaderView,QWidget
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox
from numpy import save
sys.path.append('.')
# data save part
from resource.Dict_DataFrame_Sqlite import dict_to_csv,dict_to_excel,dict_to_json,dict_to_SQLTable
from resource.Tools_functions import createPath
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
from UI_PV_monitor import Ui_Form

def get_timestamp():
    """ get current date time, as accurate as milliseconds

        Args: None

        Returns:
            str type
            eg: "2018-10-01 00:32:39.993176"
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

class PVMonitor(QWidget,Ui_Form):
    """Monitor a EPICS PV name
    should provide a PVname
    example: PVMonitor(pvname='example')
    """
    close_sig=Signal(str)
    
    def __init__(self,parent=None,PVname:str=None,TagName:str=None,):
        super(PVMonitor,self).__init__()
        self.pvname=PVname
        self.tagname=TagName if TagName else PVname
        self.setupUi(self)
        self.setWindowTitle(f'Monitoring {PVname}')
        self.monitoring_flag=False
        self._pv=''
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_time)
        # for data list
        self.pv_changed_Num:int=0
        self.pv_value_list=list()
        self.pv_num_list=list()
        self.pv_timestamps=list()
        self.__init__matplotlib()
        self.__init__datasave()
        self.timer.start(500)

    @Slot()
    def update_time(self):
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.Time_stamp_label.setText(timestamp)
# **************************************VerTicaL@zlm**************************************
#  start of pv value part

    def get_pv_value(self):
        value=None
        try:
            value=caget(self.pvname,timeout=2)
        except Exception as e:
            print(traceback.format_exc()+str(e))
        finally:
            return value

    @Slot()
    def on_Start_monitor_btn_clicked(self):
        # start PV monitor
        pv_setinfo=f'{self.pvname} Monitor'
        if not self.monitoring_flag:
            try:
                self._pv=PV(self.pvname,callback=self.pv_value_changed,connection_timeout=5)
                if self._pv.connect(timeout=5):
                    current_value=self._pv.get()
                    if current_value:
                        # self.pv_value_list.append(float(value))
                        # self.pv_changed_Num+=1
                        # self.pv_num_list.append(self.pv_changed_Num)
                        # self.pv_timestamps.append(get_timestamp())
                        self.PV_value_input.setText(f'{current_value:.4f}')
                else:
                    pv_setinfo+=' not connected'
            except Exception as e:
                print(traceback.format_exc() + str(e))
            else:
                self.monitoring_flag=True
            finally:
                print(f'end PV:{self.pvname} set')
                self.PV_name_label.setText(pv_setinfo)

    def pv_value_changed(self,pvname=None,value=None,**kw):
        """
        read PV value back
        update and plot
        """
        if value:
            self.PV_value_input.setText(f'{value:.4f}')
            timestamp=get_timestamp()
            self.pv_changed_Num+=1
            self.pv_value_list.append(float(value))
            self.pv_num_list.append(self.pv_changed_Num)
            self.pv_timestamps.append(get_timestamp())
            max_num=200
            if self.pv_changed_Num>max_num:
                num_list=self.pv_num_list[-max_num:]
                value_list=self.pv_value_list[-max_num:]
                timestamps=self.pv_timestamps[-max_num:]
            else:
                num_list=self.pv_num_list
                value_list=self.pv_value_list
                timestamps=self.pv_timestamps
            # plot the changes
            if self.Y_change_cbx.currentIndex()==0:
                self.plot_PV_data(num_list,value_list,self.pvname,'ChangeNum')
            else:
                temp_timestamps=pd.Series(timestamps)
                pd_timestamps=pd.to_datetime(temp_timestamps)
                pd_value_list=pd.Series(value_list)
                self.plot_PV_data(pd_timestamps,pd_value_list,self.pvname,'timestamp')

    @Slot()
    def on_Stop_monitor_btn_clicked(self):
        if self.monitoring_flag:
            self.monitoring_flag=False
            self._pv.remove_callback(0)

   #  end of pv value part
# **************************************VerTicaL@zlm**************************************

# **************************************VerTicaL@zlm**************************************
    #  start of pv plot part by matplotlib
    def __init__matplotlib(self):
        """Initialize matplotlib plot part
        """
        Figure_Canvas=FigureCanvas(Figure(figsize=(4,3)))
        self.verticalLayout_plot.addWidget(Figure_Canvas)
        self.verticalLayout_plot.addWidget(NavigationToolbar(Figure_Canvas,self))
        self.data_fig_ax=Figure_Canvas.figure.subplots()
        
    def plot_PV_data(self, x_list: list, y_list: list, x_name: str, y_name: str):
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

#  end of pv plot part by matplotlib
# **************************************VerTicaL@zlm**************************************

# **************************************VerTicaL@zlm**************************************
    #  start of data save part 

    def __init__datasave(self):
        self.datasave_timer=QTimer()
        self.datasave_timer.timeout.connect(self.routine_data_save)
        self.datasave_timer.start(1000*600) # save data every 10min
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
        pv_data={"id":self.pv_num_list,"value":self.pv_value_list,"timestamp":self.pv_timestamps}
        # get the valid scan data (not empty)
        for key, value in pv_data.items():
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
            dict_to_json(full_data, path, filename + '.json')
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
        filename = usrname + t_stamp + str(self._usr_save_N)
        usr_path = path if os.path.isdir(path) else save_path
        print(filename, usr_path)
        # save full data
        if full_data:
            if usr_define == 1:
                file_in_path, filetype = QFileDialog.getSaveFileName(self, 'save file', usr_path, 'xlsx(*.xlsx)')
                usr_path = os.path.dirname(file_in_path)
                usr_file = os.path.basename(file_in_path)
                filename = usr_file.split('.')[0]
            self.save_all_data(full_data, usr_path, filename)
        else:
            if usr_define == 1:
                print(f'No data to save')
            else:
                pass

#  end of data save part 
# **************************************VerTicaL@zlm**************************************
    

# **************************************VerTicaL@zlm**************************************
    #  start of closeEvent
    
    def closeEvent(self, event):
        if self.monitoring_flag:
            self.monitoring_flag=False
            self._pv.remove_callback(0)
            #event.accept()
            self.close_sig.emit(self.pvname)
        elif not self.monitoring_flag:
            #event.accept()
            self.close_sig.emit(self.pvname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PVMonitor(PVname='LiminZhou:ai1',TagName='LiminZhou:ai1')
    win.show()
    sys.exit(app.exec())
