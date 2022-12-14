from PySide6.QtCore import QTimer, Slot, QThread, Signal, QObject
from epics import ca, caget, cainfo, camonitor, caput, PV, camonitor_clear, get_pv
import time, random
import sys, os,traceback


"""
This is the control driver file for PV set and move control, including PV parameter and QThread 
"""

class PVsetThread(QThread):
    """
    ## basic functionality
    Working QThread for setting the value of one PV (mostly involves motor movement) 
    
    need several PV names:
    1. PV-set: for set value
    2. PV-rbv: for Readback value
    3. PV-movn: (optional) indication for motor moving

    emit done signal when set position is finished successfully.
    emit signal form: list[read_back,set_value,check_n,set_info]
    resolution: resolution for PV value set,default 0.02 
    ## Usage 
    example code:
    ```python
    self.PVsetQThread = PVmotorThread(PV_SET, set_value, PV_RBV, PV_Motor_MOVN, check_num=0, resolution=0.02)
    self.PVsetQThread.done_signal.connect(self.PV_set_done)
    self.PVsetQThread.start()
    ```
    """
    done_signal = Signal(list)

    def __init__(self, set_pv, set_value, rbv_pv, movn_pv, check_num: int = 0,resolution=0.02, parent=None):
        """
        ## introduction

        Working QThread for setting the value of one PV (mostly involves motor movement)
        
        emit done signal when set position is finished successfully.
        
        emit signal form: list[read_back,set_value,check_n,set_info]
        
        ## Usage 
        example code:
        ```python
        self.PVsetQThread = PVmotorThread(PV_SET, set_value, PV_RBV, PV_Motor_MOVN, check_num=0, resolution=0.02)
        self.PVsetQThread.done_signal.connect(self.PV_set_done)
        self.PVsetQThread.start()
        ```
        need pv name of [set,rbv,mvn] and the set value,check_num for check usage
        :param set_pv:
        :param set_value:
        :param rbv_pv:
        :param mov_pv:
        :param check_num:
        :param resolution: resolution for PV value set,default 0.02 
        """
        super(PVsetThread, self).__init__(parent)
        self._set_pv = PV(set_pv)
        self._set_value = set_value
        self._rbv_pv = rbv_pv
        self._check_n = check_num
        # set the moving PV
        self._mvn = movn_pv
        # limit  for motor resolution
        self.resolution = resolution
        # flag to determinate the status of put process
        self._motor_mvn_flag = 0
        self._set_flag = False
        # the new read back value and set info
        self._RBK_val = []
        self.set_info = ''

    def run(self):
        t0 = time.time()  # for time out
        print('start setting :...')
        self._pv_RBV = PV(self._rbv_pv, callback=self.readback_val)
        if self._mvn:
            self._pv_mvn = PV(self._mvn)  # for motor moving
            # add callback
            self._pv_mvn.add_callback(self.motor_mvn)
        self._set_flag = True
        if self._set_pv.connect():
            self._set_pv.put(self._set_value)
            print('set value now: %f' % self._set_value)
            self.msleep(100)
            # print('sleep 100ms')
            t_motor = time.time()
            t_motor_timeout = 1
            while self._set_flag and time.time() - t_motor < t_motor_timeout:
                # print('sleep 100ms')
                self.msleep(200)
                # check if motor is moving or not
                # self._motor_mvn_flag = caget(self._mvn)
                if self._mvn:
                    if self._motor_mvn_flag == 1:
                        self.msleep(100)
                    elif self._motor_mvn_flag == 0:
                        print(f'motor stopped: {self._motor_mvn_flag}')
                        self._set_flag = False
                        break
                else:
                    self._set_flag = False
            print('get out and emit signal:')
            # check if the Read_back value have been updated, <RBK_val[-2]>
            final_pos = self._RBK_val[-1]
            self.msleep(100)
            t_cur = time.time()
            # Set time out=10s if the target value are not reached
            time_out = 3.0 + abs(final_pos - self._set_value) * 0.5
            #print(f'time out is {time_out}')
            while time.time() - t_cur < time_out:
                # self.resolution=0.02
                if abs(final_pos - self._set_value) < self.resolution*0.8:
                    t_jump = time.time()
                    self.set_info = 'done'
                    break
                else:
                    self.msleep(200)
                    # pv_tem = PV(self._rbv_pv)
                    final_pos = self._RBK_val[-1]
                    t_jump = time.time()
                    self.set_info = 'done with time out'
                    #self.set_info = 'done'
            #jump out time
            #self.msleep(1000)
            final_pos = self._RBK_val[-1]
            #self.set_info = 'done'
            info = [final_pos, self._set_value, self._check_n, self.set_info]
            print(info)
            print(f'set position done: {t_jump - t0:.4f}s with time out of {time_out}s')
            # print(f'set position done in {(t_jump - t0):.2f} seconds ')
            self._pv_RBV.remove_callback()
            if self._mvn:
                self._pv_mvn.remove_callback() # remove mvn call back
            self.msleep(100)
            self.done_signal.emit(info)

    def readback_val(self, pvname, value, **kwargs):
        """
        read back value
        :return:
        """
        if value:
            # print(f'read back: {value}')
            self._RBK_val.append(value)
            # print(self._RBK_val)
            # print(f'call back get: {value}')

    def motor_mvn(self, pvname, value, **kw):
        """
        callback when mirror moving, 0 is stop,1 is moving
        :return:
        """
        if value:
            # print(f'Motor status: {value}')
            self._motor_mvn_flag = value

SSRF_BeamcurentPV="SR-BI:DCCT:CURRENT"
PV_20U_OpenSS2="X20U1:OP:SS2_S:OpenSts:Bl"
class SSRFBeamLine(object):
    
    def __init__(self) -> None:
        super(SSRFBeamLine, self).__init__()
        self.monitor_beamcurrent()
        self.__beamcurrent=-1
        self.__SS2status_20U=0 # 1 is open=beam on, 0 is close=beam off

    def monitor_beamcurrent(self):
        self.BeamCurrent_pv = PV(SSRF_BeamcurentPV, callback=self.SSRFCurrent_rbv)
        self.__beamcurrent=self.BeamCurrent_pv.get() if self.BeamCurrent_pv.get() else -1

    def SSRFCurrent_rbv(self, pvname, value, **kwargs):
        """
        read back value
        :return:
        """
        if isinstance(value,float):
            # print(f'read back: {value}')
            self.__beamcurrent=value
    
    @property
    def beamcurrent(self):
        return self.__beamcurrent
    
    @beamcurrent.setter
    def beamcurrent(self,current:float):
        self.__beamcurrent=current

    def monitor_20USS2(self):
        self.PV_20U_OpenSS2 = PV(PV_20U_OpenSS2, callback=self.PV_20U_OpenSS2_rbv)
        self.__SS2status_20U=self.PV_20U_OpenSS2.get() if self.PV_20U_OpenSS2.get() else 0

    def PV_20U_OpenSS2_rbv(self,pvname,value,**kwargs):
        if isinstance(value,int):
            self.__SS2status_20U=value
    
    @property
    def SS2status_20U(self):
        """
        ** SS2 shutter status (0,1) of 20U ** 
        <1 is open=beam on, 0 is close=beam off>
        Returns:
            _type_: _description_
        """
        return self.__SS2status_20U
    
    @SS2status_20U.setter
    def SS2status_20U(self,status:int):
        self.__SS2status_20U=status
