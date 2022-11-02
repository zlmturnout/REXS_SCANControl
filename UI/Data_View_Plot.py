import sys, os, time, math, datetime
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QGridLayout, QLabel, QToolBar, QDialog, \
    QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt, QTimer, Slot, QThread, Signal
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import  QStatusBar, QFileDialog, QGraphicsPixmapItem, QGraphicsView, QGraphicsScene
# import UI file
from UI_DataViewPlot import Ui_Dialog
# import my own matplotlib InitialPlot
from resource.My_Matplotlib_PySide6 import Myplot, InitialPlot, NavigationToolbar, MonitorPlot
# import my tool functions for usage
from resource.Tools_functions import get_datetime, my_logger, creatPath, suppress_error, log_exception, log_exceptions, deco_count_time
import pandas as pd
import numpy as np
# import class to display pandas dataFrame data
from resource.Class_Pandas_data_QTable import PandasInQTable
#from Dependant.Class_Pandas_data_QTable import PandasInQTable
from QtforPython_useful_tools import MyMsgBox
log_path = os.path.join(os.getcwd(), 'log_info')
creatPath(log_path)
from UI.Calculate_derivative import cal_deriv, interp_derivative,GaussianFit,plot_Gaussfit_line
# logger
log_file = f'{time.strftime("%Y-%m-%d", time.localtime())}.log'
#logger = my_logger(log_file=os.path.join(log_path, log_file), logger_name='Limin')

"""
This is the main file for data view in QTableView and plot by matplotlib
"""


class DataViewPlot(QDialog, Ui_Dialog):
    data_sig = Signal(dict)

    def __init__(self,pd_data=pd.DataFrame()):
        """
        import and show data in Qtableview and plot by matplotlib
        """
        super(DataViewPlot, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Data view and plot')
        self.__ini_plot()
        # data structure
        self.pd_data = pd_data
        self.dict_data = dict()
        self.filename=None
        self.save_folder=os.getcwd()

    def __ini_plot(self):
        # initialize BPM figure Myplot for usage
        self.figure = Myplot()
        # add NavigationToolbar in the figure (widgets)
        self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.Plot_box)
        self.gridlayout.addWidget(self.figure)
        self.gridlayout.addWidget(self.fig_ntb)
        # plot X axis info
        self.Select_X_axis.currentIndexChanged.connect(self.get_X_axis)
        self.Select_Y_axis.currentIndexChanged.connect(self.get_Y_axis)

    @Slot()
    def get_X_axis(self):
        return self.Select_X_axis.currentText()

    @Slot()
    def get_Y_axis(self):
        return self.Select_Y_axis.currentText()

    # raise info part
    def raise_warning(self, text):
        return QMessageBox.warning(self, 'ERROR', text, QMessageBox.Yes | QMessageBox.Cancel)

    def raise_info(self, text):
        return QMessageBox.information(self, 'info', text, QMessageBox.Yes | QMessageBox.Cancel)

    #@log_exceptions(log_func=logger.error)
    @suppress_error()
    def import_data(self):
        """
        import data from files as pandas dataframe,
        support filetype:<.xlsx>,<.csv>,<.json>.
        :return: data in pandas dataframe form
        """
        pd_data = pd.DataFrame()
        filename, filetype = QFileDialog.getOpenFileName(self, "read data file(supported filetype:xlsx/csv/json)",
                                                         self.save_folder, '*.xlsx;;*.csv;;*.json')
        print(filename, filetype)
        self.save_folder,file=os.path.split(filename)
        self.filename,extension=os.path.splitext(file)
        if filename.endswith('.xlsx'):
            # add dtype={'time stamp': 'datetime64[ns]'} if have 'time stamp'
            pd_data = pd.read_excel(filename, index_col=0, na_values=["NA"], engine='openpyxl')
            # print(pd_data)
        if filename.endswith('.csv'):
            pd_data = pd.read_csv(filename, index_col=0)
        if filename.endswith('.json'):
            pd_data = pd.read_json(filename)
        # drop the row with NaN and return
        return pd_data.dropna()

    @Slot()
    def on_Import_btn_clicked(self):
        self.pd_data = self.import_data()
        self.show_data_table(self.pd_data)

    @Slot()
    def on_Export_btn_clicked(self):
        """
        export the data in table
        :return:
        """
        if not self.pd_data.empty:
            filename, filetype = QFileDialog.getSaveFileName(self, "save data file(supported filetype:xlsx/csv/json)",
                                                             './', '*.xlsx;;*.csv;;*.json')

            # excel writer
            print(filename, filetype)
            if filename.endswith('.xlsx'):
                excel_writer = pd.ExcelWriter(filename)
                self.pd_data.to_excel(excel_writer)
                excel_writer.save()
                print('save to excel xlsx file successfully')
            if filename.endswith('.csv'):
                self.pd_data.to_csv(filename)
            if filename.endswith('.json'):
                self.pd_data.to_json(filename)
    def show_data_table(self, pd_data):
        """
        show all the data in Qtableview
        :param pd_data: pandas dataframe data
        :return:
        """
        # clear previous import data from combox
        self.Select_X_axis.clear()
        self.Select_Y_axis.clear()
        #print(pd_data)
        pd_data_model = PandasInQTable(pd_data)
        self.tableView.setModel(pd_data_model)
        # self.view_table.resize(600,800)
        self.tableView.setWindowTitle('show data')
        self.tableView.setAlternatingRowColors(True)
        # self.tableView.setCornerButtonEnabled(True)
        # show pd_data header in combox
        self.dict_data = self.pd_to_dict(pd_data)
        for name, data in self.dict_data.items():
            self.Select_X_axis.addItem(name)
            self.Select_Y_axis.addItem(name)

    #@log_exceptions(log_func=logger.error)
    @suppress_error()
    def pd_to_dict(self, pd_data):
        """
        read a pd DataFrame data and convert to dict form data
        Format:
        dict={'label':list[content]...}
        :param pd_data:
        :return:
        """
        dict_data = dict()
        if not pd_data.empty:
            for label, content in pd_data.items():
                dict_data[str(label)] = content.tolist()
        print(dict_data)
        return dict_data

    def dict_to_pd(self,data_dict:dict):
        """
        read dict_data and convert to pd DataFrame
        Format:
        dict={'label':list[content]...}
        :param dict_data:
        :return:
        """
        # change to the data from to standard dict {'key': pd.Series([list],index=[index])}
        new_dict = {}
        for key in data_dict:
            num = len(data_dict[key])
            new_dict[key] = pd.Series(list(data_dict[key]), index=list(range(num)))
        pd_data = pd.DataFrame(new_dict)
        return pd_data.dropna()

    #@log_exceptions(log_func=logger.error)
    @suppress_error()
    @Slot()
    def on_Plot_data_btn_clicked(self):
        """
        ask to choose X axis and Y axis, then plot data
        :return:
        """
        self.dict_data = self.pd_to_dict(self.pd_data)
        if self.dict_data:
            X_axis = self.get_X_axis()
            Y_axis = self.get_Y_axis()
            if self.dict_data.get(X_axis):
                X_list = self.dict_data.get(X_axis)
                Y_list = self.dict_data.get(Y_axis)
                print(X_list, Y_list)
                self.plot_scan_data(X_list, Y_list, X_axis, Y_axis)

    def plot_scan_data(self, x_list: list, y_list: list, x_name: str, y_name: str):
        """
        plot any x_list and y_list data,and set the Axis name x_name,y_name
        :param x_list:
        :param y_list:
        :param x_name:
        :param y_name:
        :return:
        """
        # plot
        self.figure.axes.cla()
        self.figure.axes.plot(x_list, y_list, marker='o', markersize=3, markerfacecolor='orchid',
                              markeredgecolor='orchid', linestyle='-', color='c')
        self.figure.axes.set_xlabel(x_name, fontsize=18, color='#20B2AA')
        self.figure.axes.set_ylabel(y_name, fontsize=18, color='#20B2AA')
        self.figure.axes.set_title('direct derivative')
        self.figure.draw()

    #@log_exceptions(log_func=logger.error)
    @Slot()
    def on_Derivative_btn_clicked(self):
        """
        calculate the 1st Derivative of the selected X Y data
        :return:
        """
        self.dict_data = self.pd_to_dict(self.pd_data)
        if self.dict_data:
            X_axis = self.get_X_axis()
            Y_axis = self.get_Y_axis()
            if self.dict_data.get(X_axis):
                X_list = self.dict_data.get(X_axis)
                Y_list = self.dict_data.get(Y_axis)
                #print(X_list, Y_list)
                derv_y2, derv_x2 = interp_derivative(X_list, Y_list, 100, X_axis, Y_axis)
                self.plot_scan_data(derv_x2, derv_y2, X_axis, '1st deriv by interp')
                # another method
                derv_y1,derv_x1=cal_deriv(X_list,Y_list,X_axis,Y_axis)
                self.plot_scan_data(derv_x1, derv_y1, X_axis, '1st deriv by cal')
                
                x1_fit=np.array(derv_x1)
                y1_fit=np.array(derv_y1)
                mid_index1=round(len(x1_fit)/2)
                x2_fit=np.array(derv_x2)
                y2_fit=np.array(derv_y2)
                mid_index2=round(len(x2_fit)/2)
                if np.sum(y1_fit)>0:
                    Fit_result1,FWHM1=GaussianFit(x1_fit,y1_fit,center=x1_fit[mid_index1])
                    Fit_result2,FWHM1=GaussianFit(x2_fit,y2_fit,center=x2_fit[mid_index2])
                else:
                    Fit_result1,FWHM1=GaussianFit(x1_fit,-y1_fit,center=x1_fit[mid_index1])
                    Fit_result2,FWHM1=GaussianFit(x2_fit,-y2_fit,center=x2_fit[mid_index2])
                plot_Gaussfit_line(Fit_result1,self.save_folder,self.filename+'direct',title='direct')
                plot_Gaussfit_line(Fit_result2,self.save_folder,self.filename+'interplote',title='quadraticinterplote')
                


    @Slot()
    def on_Close_btn_clicked(self):
        """
        close dialog
        :return:
        """
        self.close()

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                               "QUIT",
                                               "Are you sure to exit?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataViewPlot()
    window.show()
    app.exec_()
