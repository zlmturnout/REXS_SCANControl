# coding=utf-8
import sys, os, time, math,traceback
from mcculw import ul
from mcculw.enums import ULRange, InterfaceType
from mcculw.ul import ULError, get_net_device_descriptor, create_daq_device
from mcculw.device_info import DaqDeviceInfo
# import QT
from PySide6.QtCore import QTimer, Slot, QThread, Signal, QObject
from PySide6 import QtCore, QtWidgets


# example file from mcculw
def config_first_detected_device(board_num, dev_id_list=None):
    """Adds the first available device to the UL.  If a types_list is specified,
    the first available device in the types list will be add to the UL.

    Parameters
    ----------
    board_num : int
        The board number to assign to the board when configuring the device.

    dev_id_list : list[int], optional
        A list of product IDs used to filter the results. Default is None.
        See UL documentation for device IDs.
    """
    ul.ignore_instacal()
    devices = ul.get_daq_device_inventory(InterfaceType.ANY)
    if not devices:
        raise Exception('Error: No DAQ devices found')

    print('Found', len(devices), 'DAQ device(s):')
    for device in devices:
        print('  ', device.product_name, ' (', device.unique_id, ') - ',
              'Device ID = ', device.product_id, sep='')

    device = devices[0]
    if dev_id_list:
        device = next((device for device in devices
                       if device.product_id in dev_id_list), None)
        if not device:
            err_str = 'Error: No DAQ device found in device ID list: '
            err_str += ','.join(str(dev_id) for dev_id in dev_id_list)
            raise Exception(err_str)

    # Add the first DAQ device to the UL with the specified board number
    ul.create_daq_device(board_num, device)


def get_ADC_value(channel: int = 0, repeat_n: int = 1, t_interval: float = 0.1):
    """
    read the output signal from channel,and repeat n times for average,time_interval 0.1s
    :param t_interval:
    :param channel:
    :param repeat_n:
    :return:
    """
    # By default, the example detects and displays all available devices and
    # selects the first device listed. Use the dev_id_list variable to filter
    # detected devices by device ID (see UL documentation for device IDs).
    # If use_device_detection is set to False, the board_num variable needs to
    # match the desired board number configured with Instacal.
    use_device_detection = True
    dev_id_list = []
    board_num = 0
    # channel = channel
    read_value = 0

    try:
        if use_device_detection:
            config_first_detected_device(board_num, dev_id_list)

        daq_dev_info = DaqDeviceInfo(board_num)
        if not daq_dev_info.supports_analog_input:
            raise Exception('Error: The DAQ device does not support '
                            'analog input')

        print('\nActive DAQ device: ', daq_dev_info.product_name, ' (',
              daq_dev_info.unique_id, ')\n', sep='')

        ai_info = daq_dev_info.get_ai_info()
        ai_range = ai_info.supported_ranges[0]
        i = 0
        while i < repeat_n:
            time.sleep(t_interval)
            # Get a value from the device
            if ai_info.resolution <= 16:
                # Use the a_in method for devices with a resolution <= 16
                value = ul.a_in(board_num, channel, ai_range)
                # Convert the raw value to engineering units
                eng_units_value = ul.to_eng_units(board_num, ai_range, value)
            else:
                # Use the a_in_32 method for devices with a resolution > 16
                # (optional parameter omitted)
                value = ul.a_in_32(board_num, channel, ai_range)
                # Convert the raw value to engineering units
                eng_units_value = ul.to_eng_units_32(board_num, ai_range, value)
            read_value += eng_units_value
            i += 1

        # Display the raw value
        print('Raw Value:', value)
        # Display the engineering value
        print('Engineering Value: {:.3f}'.format(eng_units_value))
    except Exception as e:
        print('\n', e)
    finally:
        if use_device_detection:
            ul.release_daq_device(board_num)
        # average_value=f'{read_value/repeat_n:.3f}'
        average_value = '{:.3f}'.format(read_value / repeat_n)
        return float(average_value)


# set up the host and port of the ethernet device for E-1608
host = '169.254.111.100'
#host = '10.30.95.167'
port = 54211
# ignore instacal Prevents the Universal Library from automatically adding a DAQ device that has been stored
#     in the cb.cfg file by InstaCal
ul.ignore_instacal()
board_num = 1


def search_adc_device(host, port,timeout=5):
    board_num = 1
    device_info = dict()
    try:
        device = get_net_device_descriptor(host, port, timeout)
        create_daq_device(board_num, device)
        # get the device info
        daq_dev_info = DaqDeviceInfo(board_num)
        product_id = device.product_id
        product_type = device.product_name
        product_name = device.dev_string
        interface = device.interface_type
        ai_info = daq_dev_info.get_ai_info()
        resolution = ai_info.resolution
        MAC = device.unique_id
        print(f'device type: {product_type}\n device id: {product_id}\ndevice name: {product_name}\n '
              f'interface:{interface}\n resolution:{resolution}')
        device_info={'product_name':product_name,'product_id':product_id,
                     'product_type':product_type,'interface':interface,
                     'resolution':resolution,'address':host+':'+str(port),'MAC':MAC}
    except Exception as e:
        print('\n', e)
    else:
        ul.release_daq_device(board_num)
    finally:
        return device_info


# QThread to read data from DAQ E-1608
class E1608QThread(QThread):
    """
    Work QThread to read data from ADC type MCC E-1608
    """
    data_sig = Signal(list)

    def __init__(self, channel: int = 0, ul_range_n: int = 3, repeat_n: int = 1, t_interval: float = 0.1,
                 keep_on: int = 0, host='10.30.95.167',port = 54211):
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
        self.board_num = 0
        self.ul_range_list = [ULRange.BIP1VOLTS, ULRange.BIP2VOLTS, ULRange.BIP5VOLTS, ULRange.BIP10VOLTS]
        self.UL_range = self.ul_range_list[ul_range_n]
        ul.ignore_instacal()
        self.run_flag = True
        # 0 is run once, 1 is keep on monitoring until runtime runs out.
        self.keep_on = keep_on
        self.__ini_device()

    def __del__(self):
        self.keep_on = 0
        # self._run_flag=False
    
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
