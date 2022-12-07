import sys, os, time, typing
import datetime, traceback
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QGridLayout, QLabel, QToolBar, QDialog, \
    QMessageBox,QStyle
from PySide6.QtCore import Qt, QTimer, Slot, QThread, Signal, QDate, QDateTime,QObject
from PySide6 import QtCore, QtWidgets
from UI_my_msg_box import Ui_Dialog
from UI_About_box import Ui_Form



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
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
    msg_box.setDetailedText(details)
    close_event = msg_box.exec_()
    if close_event == QMessageBox.Yes:
        return 1
    else:
        return


class EmittingStr(QtCore.QObject):
    """
    send every system output into a qt text box
    code example:
    sys.stdout = EmittingStr(textWritten=self.outputWritten)
    sys.stderr = EmittingStr(textWritten=self.outputWritten)
    """
    textWritten = QtCore.Signal(str)

    # def __init__(self,parent=None,*args, **kwargs):
    #     super(EmittingStr, self).__init__(parent)

    def write(self, text):
        self.textWritten.emit('>' + str(text))
    
    def flush(self):
        pass



# my custom msg box to show info with close event
class MyMsgBox(QDialog, Ui_Dialog):
    """My customed message box
    
    show a message box contain info and detailed info
    
    Note on signal:
        choose to send signal <str> when msg_box close-event is accepted <YES> or canceled <Cancel>

        1 is send signal,0 is do not send 

    close event send info:
        1. Confirmed will send "Yes"
        2. Cenceled will send "Cancel"

    
    Args:
        title: str= 
        text: str=
        details: str=
        signal: int=0
    """
    close_sig = Signal(str)
    

    def __init__(self, title: str, text: str, details=None, signal: int = 0):
        super(MyMsgBox, self).__init__()
        self.setupUi(self)
        self.title = title
        self.text = text
        self.details = details
        self.setWindowTitle(title)
        self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxInformation))
        self.Detail_text.setText(details)
        self.Info_box.setText(text)
        # hide the details when initialized
        self.Detail_text.hide()
        self.hide_flag = 0  # 0 is hide,1 is
        self.send_signal = signal  # 0 is not send signal,1 is send signal
        self.send_info = None

    @Slot()
    def on_Hide_btn_clicked(self):
        if self.hide_flag == 0:
            self.Detail_text.show()
            self.Hide_btn.setText('Hide details')
            self.hide_flag = 1
        elif self.hide_flag == 1:
            self.Detail_text.hide()
            self.Hide_btn.setText('Show details')
            self.hide_flag = 0

    @Slot()
    def on_Confirm_btn_clicked(self):
        self.send_info = 'Yes'
        self.close()

    @Slot()
    def on_Cancel_btn_clicked(self):
        self.send_info = 'Cancel'
        self.close()

    def closeEvent(self, event):
        #print(self.send_info)
        if self.send_info is None:
            event.ignore()
        elif self.send_signal == 1:
            # print('send signal')
            self.close_sig.emit(self.send_info)
            event.accept()
        elif self.send_signal == 0:
            event.accept()


@Slot(str)
def get_info(info: str):
    print(info)

class AboutInfo(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super(AboutInfo,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("About the Program")
        self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_DesktopIcon))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMsgBox('test','info',details='test test')
    window.show()
    app.exec()

