import os,sys,time,datetime,traceback
import re

from matplotlib.pyplot import table

# QT for python import
import PySide6
from PySide6.QtCore import QTimer, Slot, QThread, Signal, Qt,QTime,QDate,QDateTime
from PySide6.QtGui import QDoubleValidator, QIntValidator, QTextCursor,QAction
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QBrush
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
	QMessageBox,QAbstractItemView
# QSql support
from PySide6.QtSql import QSqlDatabase,QSqlError,QSqlTableModel,QSqlDriver,QSqlField
# QCharts support
from PySide6.QtCharts import QLineSeries,QVXYModelMapper,QChartView,QChart,QValueAxis,QDateTimeAxis
# data process
import sqlite3
import numpy as np
import pandas as pd
# matplotlib
from matplotlib.backends.backend_qtagg import(FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
# UI import
from UI.UI_SQLData_view import Ui_Dialog

class RunQThread(QThread):
	"""
	run any time consuming operation of func(*args,**kwargs)
	:argument can provide keyword args <timeout:float=1000.0>ms
	:return the signal will send function's return value in list form (return=funcs())
	Notice: if run exception occurs,will emit the <Exception info>
	"""
	run_sig = Signal(list)

	def __init__(self, func, *args, timeout: float = 1000.0, **kwargs):
		super(RunQThread, self).__init__()
		self.args = args
		self.kwargs = kwargs
		self.run_flag = True
		self.run_time = timeout
		self.func = func
		self.result = None

	def run(self):
		t0 = time.time()
		print('QThread start')
		while self.run_flag and time.time() - t0 < self.run_time:
			try:
				self.result = self.func(*self.args, **self.kwargs)
			except Exception as e:
				# print(e)
				error_info = traceback.format_exc() + str(e) + '\n'
				self.run_sig.emit([error_info])
			else:
				self.run_flag = False
				self.run_sig.emit([self.result])

	def __del__(self):
		self.run_time = False

def msg_box(title, text, details):
	msg_box = QMessageBox()
	msg_box.setWindowTitle(title)
	msg_box.setText(text)
	msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Close)
	msg_box.setDetailedText(details)
	close_event = msg_box.exec()
	if close_event == QMessageBox.Yes:
		return 1
	else:
		return 0

class SqlCustomTableModel(QSqlTableModel):
	"""
	Customized QSqlTableModel for python
	not working properly deprecated
	Usage example:
		SqlCustomTableModel(parent,db:QSqlDatabase)
	"""
	def __init__(self,parent,db:QSqlDatabase):
		super(SqlCustomTableModel, self).__init__(parent,db)
		self.db = db
		self.parent = parent
		self.TableModel=QSqlTableModel(parent,db)
		print(f'tablemodel now:{self.TableModel.database()}')

	# override the default data func
	#not working properly
	def data(self,idx,role):
		if role==8 and self.isDirty(idx):
			return QBrush(QColor('yellow'))
		resp=QSqlTableModel.data(idx,role)
		print(f'get result:{resp}')
		return resp


class ViewSQLiteData(QWidget,Ui_Dialog):
	"""View Covid19 data in ShangHai@2022

	data start from 2022-03-01
	"""
	def __init__(self, *args, **kwargs):
		super(ViewSQLiteData, self).__init__()
		self.setupUi(self)
		self.setWindowTitle("View SQLite Data")
		self.Covid19Data=pd.DataFrame()
		self.__init__sqlconnection()
		self.__init__plot()
		self.__init__matplotlib()

	# **************************************VerTicaL@zlm**************************************


	# **************************************VerTicaL@zlm**************************************
	# start of SQL data part
	def __init__sqlconnection(self):
		self.dbconnect_N=0
		self.current_dbTable=''
		self.current_Tablemodel=QSqlTableModel()
		# show table data when db_table in treeView activated
		self.treeView.tableActivated_sig.connect(self.show_tabledata)


	@Slot()
	def on_Open_datebase_btn_clicked(self):
		"""open filedialog to connect to a SQLite database
		"""
		database_file,filetype=QFileDialog.getOpenFileName(self, "Open database file",os.getcwd(), "databasefile(*.db)")
		if database_file:
			print(f'get database file: {database_file}')
			self.Database_txt.setText(database_file)
			# connect database by SQLite driver
			qError=self.sqlite_connect(database_file)
			if qError.type() != QSqlError.NoError:
				self.msgbox=msg_box('open database failed',f'error while connecting to database{database_file}',qError.text())
				self.msgbox.show()
			else:
				# database connected refresh database in treeView
				self.treeView.refresh()

	def sqlite_connect(self, db_name:str,driver:str="QSQLITE"):
		"""
		sqlite connection to database
		"""
		qerror=QSqlError()
		self.dbconnect_N+=1
		connection_name=f'DBconnect{self.dbconnect_N}'
		db=QSqlDatabase.addDatabase(driver,connection_name)
		db.setDatabaseName(db_name)

		# db is not open,reomve connection and return error
		if not db.open():
			qerror=db.lastError()
			db=QSqlDatabase()
			QSqlDatabase.removeDatabase(connection_name)
		return qerror

	@Slot(str)
	def show_tabledata(self,tableName:str):
		"""show table data by Model/View framework

		Args:
			tableName (str): table name
		"""
		print(f'get table name:{tableName}')
		self.current_dbTable=tableName
		#Table_model=SqlCustomTableModel(self.tableView,self.treeView.currentDatabase())
		Table_model=QSqlTableModel(self.tableView,self.treeView.currentDatabase())
		#print(f'current driver:{self.treeView.currentDatabase().driver().escapeIdentifier(tableName,QSqlDriver.TableName)}')
		Table_model.setTable(self.treeView.currentDatabase().driver().escapeIdentifier(tableName,QSqlDriver.TableName))
		# update all data in the table
		Table_model.select()

		if Table_model.lastError().type()!=QSqlError.NoError:
			print(f'last error: {Table_model.lastError().text()}')

		Table_model.setEditStrategy(QSqlTableModel.OnRowChange)
		# set table model in table view
		self.tableView.setModel(Table_model)
		#self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked)
		self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers) # can not edit

		# add headers of the actived table into plot axis cbx
		self.setTableHeaders(Table_model)
		self.current_Tablemodel=Table_model

	def setTableHeaders(self,Table_model:QSqlTableModel):
		"""
		add all headers into to X and Y axis_cbx for dataplot
		"""
		# clear X/Y_axis_cbx
		self.X_axis_cbx.clear()
		self.Y_axis_cbx.clear()
		# get all headers in the actived table
		sql_record=Table_model.record(0)
		for i in range(sql_record.count()):
			field_name=sql_record.field(i).name()
			value=sql_record.field(i).value()
			#print(f'field name: {field_name}\nvalue: {value}')
			self.X_axis_cbx.addItem(str(field_name))
			self.Y_axis_cbx.addItem(str(field_name))
	# end of SQL data  part
	# **************************************VerTicaL@zlm**************************************
	# **************************************VerTicaL@zlm**************************************
	#  start of SQL data plot part by Qt

	def __init__plot(self):
		self.linechart = QChart()
		self.linechart.setAnimationOptions(QChart.AllAnimations)
		self.XYmapper=QVXYModelMapper()
		self.line_series=QLineSeries()
		self.X_axis=QValueAxis()
		self.Y_axis=QValueAxis()
		self.Xdate_axis=QDateTimeAxis()
		self.Ydate_axis=QDateTimeAxis()
		self.chartView=QChartView()
		self.chartView.setRenderHint(QPainter.Antialiasing)
		self.chartView.setMinimumSize(400, 300)
		self.plot_once_flag=0
		#add chart to chartView
		self.chartView.setChart(self.linechart)
		#self.Plot_gridlayout.addWidget(self.chartView)


	@Slot()
	def on_Plot_database__btn_clicked(self):
		"""plot data by selected X/Y axis cbx
		"""
		#self.Qt_lineplot()
		self.matplotlib_lineplot()

	def Qt_lineplot(self):
		"""plot table data by Qt"""

		table_model=self.tableView.model()
		#self.line_series.clear()
		if self.X_axis_cbx.count() != 0 and self.Y_axis_cbx.count()!=0:
			X_column_idx=self.X_axis_cbx.currentIndex()
			Y_column_idx=self.Y_axis_cbx.currentIndex()
			x_axis=self.X_axis_cbx.currentText()
			y_axis=self.Y_axis_cbx.currentText()
		else:
			print(f'no data selected')
			self.msgbox=msg_box('plot error','no data to plot','open database first and select plot axis')
			return 0
		
		if self.X_axis_cbx.currentText() in ['Date','date'] or self.Y_axis_cbx.currentText() in ['Date','date']:
			# date-value plot
			print(f'plot date-value')
			
			#table_model=self.tableView.model()
			self.line_series.clear()
			self.getPlot_XYdata(table_model)
		else:
			self.line_series.clear()
			self.getPlot_XYdata(table_model)
		self.lineseries_plot()
	
	def lineseries_plot(self):
		x_min=self.line_series.at(0).x()
		x_max=self.line_series.at(0).x()
		y_min=self.line_series.at(0).y()
		y_max=self.line_series.at(0).y()
		for i in range(self.line_series.count()):
			x_min=self.line_series.at(i).x() if self.line_series.at(i).x()<x_min else x_min
			y_min=self.line_series.at(i).y() if self.line_series.at(i).y()<y_min else y_min
			x_max=self.line_series.at(i).x() if self.line_series.at(i).x()>x_max else x_max
			y_max=self.line_series.at(i).y() if self.line_series.at(i).y()>y_max else y_max
		if self.plot_once_flag==0:
			self.linechart.addSeries(self.line_series)
			#self.linechart.createDefaultAxes()
			self.plot_once_flag=1
		else:
			self.linechart.removeSeries(self.line_series)
			self.linechart.removeAxis(self.X_axis)
			self.linechart.removeAxis(self.Y_axis)
			print(f'x_max:{self.X_axis.max()}\nx_min:{self.X_axis.min()}\n')
			print(f'y_max:{self.Y_axis.max()}\ny_min:{self.Y_axis.min()}\n')
			self.X_axis.setRange(x_min, x_max)
			self.Y_axis.setRange(y_min, y_max)
			self.linechart.addSeries(self.line_series)
			self.linechart.addAxis(self.X_axis,Qt.AlignBottom)
			self.linechart.addAxis(self.Y_axis,Qt.AlignLeft)
			self.X_axis.setTitleText(self.X_axis_cbx.currentText())
			self.Y_axis.setTitleText(self.Y_axis_cbx.currentText())
		
	def getPlot_XYdata(self,Table_model:QSqlTableModel):
		"""
		get the plot data set of [x_value,y_value] 
		"""
		x_list=[]
		y_list=[]
		x_axis=self.X_axis_cbx.currentText()
		y_axis=self.Y_axis_cbx.currentText()
		self.line_series.setName(f'{self.current_dbTable}\nNote:Date=days since 1970-01-01')
		#print(f'Table_model:{Table_model}:{Table_model.rowCount()}')
		print(f'x_axis:{x_axis},y_axis:{y_axis},')
		for i in range(Table_model.rowCount()):
			x_dvalue=Table_model.record(i).field(x_axis).value()
			y_dvalue=Table_model.record(i).field(y_axis).value()
			if x_axis in ['Date','date'] and y_axis in ['Date','date']:
				#x_dvalue=Table_model.record(i).field(x_axis).value()
				x_value=QDateTime.fromString(x_dvalue,'yyyy-MM-dd').toSecsSinceEpoch()//(24*3600)
				y_value=QDateTime.fromString(y_dvalue,'yyyy-MM-dd').toSecsSinceEpoch()//(24*3600)
				#print(f'x_date:{x_dvalue}\nmsc: {x_value}\n')
			elif x_axis not in ['Date','date'] and y_axis in ['Date','date']:
				#y_dvalue=Table_model.record(i).field(y_axis).value()
				y_value=QDateTime.fromString(y_dvalue,'yyyy-MM-dd').toSecsSinceEpoch()//(24*3600)
				x_value=x_dvalue
				#print(f'y_date:{y_value}\nmsc: {y_value}\n')
			elif x_axis in ['Date','date'] and y_axis not in ['Date','date']:
				x_value=QDateTime.fromString(x_dvalue,'yyyy-MM-dd').toSecsSinceEpoch()//(24*3600)
				y_value=y_dvalue
			else:
				x_value=x_dvalue
				y_value=y_dvalue
			x_list.append(x_value)
			y_list.append(y_value)
			self.line_series.append(x_value,y_value)
		print(f'x_list:{x_list}\ny_list:{y_list}\n')

	#  start of SQL data plot part by Qt
# **************************************VerTicaL@zlm**************************************
	


# **************************************VerTicaL@zlm**************************************
	#  start of SQL data plot part by matplotlib
	def __init__matplotlib(self):
		"""Initialize matplotlib plot part
		"""
		Figure_Canvas=FigureCanvas(Figure(figsize=(4,3)))
		self.Plot_gridlayout.addWidget(Figure_Canvas)
		self.Plot_gridlayout.addWidget(NavigationToolbar(Figure_Canvas,self))
		self.data_fig_ax=Figure_Canvas.figure.subplots()

	def get_table_XYdata(self,Table_model:QSqlTableModel):
		"""
		get the plot data set of [x_value,y_value] 
		"""
		x_list=[]
		y_list=[]
		x_axis=self.X_axis_cbx.currentText()
		y_axis=self.Y_axis_cbx.currentText()
		#print(f'Table_model:{Table_model}:{Table_model.rowCount()}')
		print(f'x_axis:{x_axis},y_axis:{y_axis},')
		for i in range(Table_model.rowCount()):
			x_value=Table_model.record(i).field(x_axis).value()
			y_value=Table_model.record(i).field(y_axis).value()
			x_list.append(x_value)
			y_list.append(y_value)
		return x_list,y_list,x_axis,y_axis

	def matplotlib_lineplot(self):
		"""plot the table data by  matplotlib
		"""
		table_model=self.tableView.model()
		x_list,y_list,x_axis,y_axis=self.get_table_XYdata(table_model)
		self.plot_sql_data(x_list,y_list,x_axis,y_axis)


	def plot_sql_data(self, x_list: list, y_list: list, x_name: str, y_name: str):
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
		self.data_fig_ax.figure.autofmt_xdate(rotation=35)
		self.data_fig_ax.figure.canvas.draw()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = ViewSQLiteData()
	win.show()
	sys.exit(app.exec())
