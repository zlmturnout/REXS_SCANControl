from PySide6.QtCore import QTimer, Slot, QThread, Signal, QObject
from epics import ca, caget, cainfo, camonitor, caput, PV, camonitor_clear, get_pv
import time, random
import sys, os

from EPICS_PV_names import *

"""
This is the control driver file for Monochromator motion control, including PV parameter and QThread 
"""

# # PV names for Energy SE=Soft_Energy
# PV_SE_SET = "X20U:OP:PGM1:Soft_Energy.VAL"  # set energy
# PV_SE_RBV = "X20U:OP:PGM1:Soft_Energy.RBV"  # energy read back
# PV_SE_MV_RTRY = "X20U:OP:PGM1:Soft_Energy.RTRY"  # retries
# # PV names for Mirror motion control
# PV_MR_SET = "X20U:OP:PGM1:MR.VAL"  # set mirror angle <arcsec>
# PV_MR_RBV = "X20U:OP:PGM1:MR.RBV"  # Readback mirror angle <arcsec>
# PV_MR_Motor = "X20U:OP:PGM1:MR.DMOV"  # status mirror motor <0,1>
# PV_MR_Motor_HLS = "X20U:OP:PGM1:MR.HLS"  # status mirror motor high limit <0,1>
# PV_MR_Motor_LLS = "X20U:OP:PGM1:MR.LLS"  # status mirror motor high limit <0,1>
# PV_MR_Motor_MOVN = "X20U:OP:PGM1:MR.MOVN"  # status mirror motor moving <0,1>
# PV_MR_Motor_DMOV = "X20U:OP:PGM1:MR.DMOV"  # status mirror motor done moving <0,1>
# # PV names for Grating Rotation
# PV_GR_SET = "X20U:OP:PGM1:GR.VAL"  # set grate angle <arcsec>
# PV_GR_RBV = "X20U:OP:PGM1:GR.RBV"  # Readback grate angle <arcsec>
# PV_GR_Type = "X20U:OP:PGM1:GRATE_TYPE"  # set grate type GRATE<1,2,3>
# PV_GR_Motor = "X20U:OP:PGM1:GR.DMOV"  # status mirror motor <0,1>
# PV_GR_Motor_HLS = "X20U:OP:PGM1:GR.HLS"  # status mirror motor high limit <0,1>
# PV_GR_Motor_LLS = "X20U:OP:PGM1:GR.LLS"  # status mirror motor high limit <0,1>
# PV_GR_Motor_MOVN = "X20U:OP:PGM1:GR.MOVN"  # status mirror motor moving <0,1>
# PV_GR_Motor_DMOV = "X20U:OP:PGM1:GR.DMOV"  # status mirror motor done moving <0,1>
# # basic parameter for grate <b2*e-5,K0:l/mm>
# Param_Grate = {'Grate1': {"b2": 9.856, "K0": 300},
#                'Grate2': {"b2": 8.186, "K0": 800},
#                'Grate3': {"b2": 7.224, "K0": 1200}
#                }


class MonoSetThread(QThread):
    """
    Working QThread for setting PV variables of Monochromator like <Energy> <motor motion>,
    emit done signal when put process is finished successfully.
    """
    done_signal = Signal(list)

    def __init__(self, set_pv, set_value, num: int = 0, parent=None):
        super(MonoSetThread, self).__init__()
        self._set_pv = PV(set_pv)
        self._new_value = set_value
        self._check_n = 0
        # set the moving
        # self._rbv_pv=PV(PV_SE_RBV,callback=self.readback_val)  # readback energy
        # set retries 2
        self._set_rtry = PV(PV_SE_MV_RTRY)
        self._set_rtry.put(2)

        self._MR_mvn = PV(PV_MR_Motor_MOVN)  # mirror moving
        self._MR_dmv = PV(PV_GR_Motor_DMOV)  # mirror moving done
        self._GR_mvn = PV(PV_GR_Motor_MOVN)  # grate moving
        self._GR_dmv = PV(PV_GR_Motor_DMOV)  # grate moving done
        # add callback
        self._MR_mvn.add_callback(self.mirror_mvn)
        self._MR_dmv.add_callback(self.mirror_dmv)
        self._GR_mvn.add_callback(self.grate_mvn)
        self._MR_dmv.add_callback(self.grate_dmv)
        # flag to determinate the status put process
        self._MR_mvn_flag = 0
        self._MR_dmv_flag = 1
        self._GR_mvn_flag = 0
        self._GR_dmv_flag = 1
        self._set_flag = False
        # the new read back value
        self._RBK_val = []
        self.set_info = ''

    def run(self):
        t0 = time.time()
        print('start setting energy:...')
        self._rbv_pv = PV(PV_SE_RBV, callback=self.readback_val)
        self._set_flag = True
        if self._set_pv.connect():
            self._set_pv.put(self._new_value)
            print('set value now: %f' % self._new_value)
            # self.msleep(100)
            print('sleep 100ms')
            while self._set_flag:
                print('sleep 100ms')
                # self.msleep(100)
                # may work should check
                # self._MR_mvn_flag=self._MR_mvn.value
                print('Mirror moving: %d' % self._MR_mvn_flag)
                # self._MR_dmv_flag=self._MR_dmv.value
                # self._GR_mvn_flag=self._GR_mvn.value
                print('Grate moving: %d' % self._MR_mvn_flag)
                # self._GR_dmv_flag=self._GR_dmv.value
                if self._MR_mvn_flag == 1 or self._GR_mvn_flag == 1:
                    print('Mirror moving' + 'or' + 'Grate moving')
                    self.msleep(100)
                elif self._MR_dmv_flag == 0 or self._GR_dmv_flag == 0:
                    print('motor moving not done')
                    self.msleep(100)
                elif self._MR_mvn_flag == 0 and self._GR_mvn_flag == 0 and self._MR_dmv_flag == 1 and self._GR_dmv_flag == 1:
                    print('moving finished')
                    self.set_info = 'done'
                    self._set_flag = False
                    break
            print('get out and emit signal:')
            # final_energy=self._rbv_pv.get
            # check if the Read_back value have been updated, <RBK_val[-2]>
            pv_tem = get_pv(PV_SE_RBV)
            final_energy = pv_tem.value
            self.msleep(100)
            t_jump = time.time()
            while time.time() - t0 < 60.0:
                if abs(final_energy - self._new_value) < 0.002:
                    t_jump = time.time()
                    break
                else:
                    self.msleep(100)
                    pv_tem = get_pv(PV_SE_RBV)
                    final_energy = pv_tem.value

            info = [final_energy, self._new_value, self._check_n, self.set_info]
            print(info)
            print(f'set energy done in {(t_jump - t0):.2f} seconds ')
            self._rbv_pv.remove_callback()
            self.msleep(100)
            self.done_signal.emit(info)

    def readback_val(self, pvname, value, **kwargs):
        """
        read back value
        :return:
        """
        if value:
            self._RBK_val.append(value)
            # print(self._RBK_val)
            # print(f'call back get: {value}')

    def mirror_mvn(self, pvname, value, **kw):
        """
        callback when mirror moving
        :return:
        """
        if value:
            print(f'mirror mvn {value}')
            self._MR_mvn_flag = value

    def mirror_dmv(self, pvname, value, **kw):
        """
        callback when mirror done moving
        :return:
        """
        if value:
            self._MR_dmv_flag = value

    def grate_mvn(self, pvname, value, **kw):
        """
        callback when grate moving
        :return:
        """
        if value:
            print(f'grate mvn {value}')
            self._GR_mvn_flag = value

    def grate_dmv(self, pvname, value, **kw):
        """
        callback when grate moving
        :return:
        """
        if value:
            self._GR_dmv_flag = value


class PVmotorThread(QThread):
    """
    Working QThread for setting position of beam position motor,
    emit done signal when set position is finished successfully.
    emit signal: list[read_back,set_value,check_n,set_info]
    need pv name of [set,rbv,mvn] and the set value,num for check usage
    """
    done_signal = Signal(list)

    def __init__(self, set_pv, set_value, rbv_pv, movn_pv, check_num: int = 0,resolution=0.02, parent=None):
        """
        need pv name of [set,rbv,mvn] and the set value,num for check usage
        :param set_pv:
        :param set_value:
        :param rbv_pv:
        :param mov_pv:
        :param num:
        :param parent:
        """
        #QThread.__init__(self, parent)
        super().__init__(parent)
        self._set_pv = PV(set_pv)
        self._set_value = set_value
        self._rbv_pv = rbv_pv
        self._check_n = check_num
        # set the moving
        self._mvn = movn_pv
        # limit  for motor resolution
        self.resolution = resolution

        # self._pv_mvn = PV(movn_pv)  # motor moving
        # # add callback
        # self._pv_mvn.add_callback(self.motor_mvn)
        # flag to determinate the status of put process
        self._motor_mvn_flag = 0
        self._set_flag = False
        # the new read back value and set info
        self._RBK_val = []
        self.set_info = ''

    def run(self):
        t0 = time.time()  # for time out
        print('start setting energy:...')
        self._pv_RBV = PV(self._rbv_pv, callback=self.readback_val)
        self._pv_mvn = PV(self._mvn)  # motor moving
        # add callback
        self._pv_mvn.add_callback(self.motor_mvn)
        self._set_flag = True
        if self._set_pv.connect():
            self._set_pv.put(self._set_value)
            # print('set value now: %f' % self._set_value)
            self.msleep(100)
            # print('sleep 100ms')
            t_motor = time.time()
            t_motor_timeout = 1
            while self._set_flag and time.time() - t_motor < t_motor_timeout:
                # print('sleep 100ms')
                self.msleep(200)
                # self._MR_mvn_flag=self._MR_mvn.value
                # print(f'motor status: {self._motor_mvn_flag}')
                # check if motor is moving or not
                # self._motor_mvn_flag = caget(self._mvn)
                if self._motor_mvn_flag == 1:
                    self.msleep(100)
                elif self._motor_mvn_flag == 0:
                    print(f'motor stopped: {self._motor_mvn_flag}')
                    self._set_flag = False
                    break
            print('get out and emit signal:')
            # check if the Read_back value have been updated, <RBK_val[-2]>
            # pv_tem = PV(self._rbv_pv)
            final_pos = self._RBK_val[-1]
            # print(f'final_pos:{final_pos}')
            self.msleep(200)
            t_cur = time.time()
            # Set time out=10s if the target value are not reached
            distance = abs(final_pos - self._set_value)
            time_out = 3.0 + distance * 0.5
            while time.time() - t_cur < time_out:
                # self.resolution=0.02
                if abs(final_pos - self._set_value) < self.resolution*0.3:
                    t_jump = time.time()
                    self.set_info = 'done'
                    break
                else:
                    self.msleep(1000)
                    # pv_tem = PV(self._rbv_pv)
                    final_pos = self._RBK_val[-1]
                    t_jump = time.time()
                    # self.set_info = 'done with time out'
                    self.set_info = 'done'
            #jump out time
            self.msleep(1000)
            final_pos = self._RBK_val[-1]
            print(f'jump out after: {t_jump - t_cur:.4f}s with time out of {time_out}s')
            self.set_info = 'done'
            info = [final_pos, self._set_value, self._check_n, self.set_info]
            print(info)
            # print(f'set position done in {(t_jump - t0):.2f} seconds ')
            self._pv_RBV.remove_callback()
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
