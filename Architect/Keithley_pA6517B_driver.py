from socket import *
import os, re, sys, time, math, traceback, logging
from PySide6.QtCore import QTimer, Slot, QThread, Signal, QObject
import numpy as np
import pandas as pd
from time import sleep
# from Dependant.Tools_functions import my_logger, creatPath
from SCIP_CMD_6517B import *


def my_logger(log_file: str = 'output.log', logger_name: str = 'usr_test'):
    """
    return a logger for logging
    :return:
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def creatPath(file_path):
    """
    create a given path if not exist and return it
    :param file_path:
    :return: file_path
    """
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    return file_path


HOST = '10.30.95.170'
Port_list = [23, 26, 29, 32]  # port in USR_N540,26 is for keithley 6517B
BUFSIZ = 1024
log_path = os.path.join(os.getcwd(), 'log_info')
creatPath(log_path)
# logger
log_file = f'Keithley6517B_{time.strftime("%Y-%m-%d", time.localtime())}.log'
Keithley6517B_logger = my_logger(log_file=os.path.join(log_path, log_file), logger_name='Keithley6517B')

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
        # function:read currents implemented
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
            Keithley6517B_logger.error("Connection fail %s", e, exc_info=True)
        else:
            self.connect_flag = True
            self.socket_TCP.send(self.send_msg)
            self.msleep(wait)
            t_start = time.time()
            while self.connect_flag and receive_flag and time.time() - t_start < 10:
                resp = self.socket_TCP.recv(BUFSIZ)
                if resp:
                    self.response_msg = resp.decode('utf-8')
                    Keithley6517B_logger.info("get response %s", self.response_msg)
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

    def current_nplc(self,nplc:int=5):
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
        print(f'get new read:{data_value}A')
        return data_value

    def run(self):
        print(self.func)
        t0 = time.time()
        status = 'OK'
        pA_currents=0
        # measure current
        if self.func == 'currents':
            #self.current_nplc(nplc=self.nplc)
            self.curr_aver_counts(num=self.points)
            self.zero_check(status='OFF')
            while self.run_flag and time.time() - t0 < self.monitor_time:
                try:
                    resp = self.fresh_data()
                    pA_currents = self.get_value(resp)
                    status = 'error' if pA_currents == 0 else 'OK'
                except Exception as e:
                    error_info = traceback.format_exc()
                    print(error_info)
                    Keithley6517B_logger.error("Connection fail %s", e, exc_info=True)
                finally:
                    #print(f'start emit:{[pA_currents, pA_currents, status]}')
                    self.data_sig.emit([pA_currents, pA_currents, status])
                if self._keep_on == 0:
                    self.run_flag = False


if __name__ == '__main__':
    print('OK')
    Keithley6517B = Keithley6517BCom(address=(HOST, Port_list[1]), func='currents', points=5)
    ID = Keithley6517B.deviceID
    version = Keithley6517B.version
    print(f'get ID: {ID}\n version:{version}')
    #Keithley6517B.reset()
    Keithley6517B.clear_status()
    Keithley6517B.configure_current()
    Keithley6517B.current_filter()
    Keithley6517B.curr_medianMode(MediaMode=False)
    Keithley6517B.current_nplc(nplc=5)
    Keithley6517B.curr_aver_counts(num=5)
    Keithley6517B.initiate_continuous(continu=True)
    Keithley6517B.zero_check(status='OFF')

    time.sleep(5)
    resp = Keithley6517B.fresh_data(wait=2000)
    # resp = Keithley6517B.fetch(wait=2000)
    data = Keithley6517B.get_value(resp)
    # Keithley6517B.start()
    #time.sleep(5)

    # resp = Keithley6517B.fresh_data()
    # data = Keithley6517B.get_value(resp)
