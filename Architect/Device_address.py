"""
device address for data acqusition
1.ADC device
address:(host,port,channel,ul_range_n)

2. pAmeter RS232-ethernet
address:(host,port)
"""
# device address
# for REXS station
Q_REXS_DeviceAddress={"TEY_V":('10.30.95.164',54211,0,3),"Au_V":('10.30.95.164',54211,1,3),"PD_V":('10.30.95.164',54211,2,3),
"TEY_I":('10.30.95.170',26),"Au_I":('10.30.95.170',26),"PD_I":('10.30.95.170',26)}

# for RXES station
RXES_DeviceAddress={"TEY_V":('10.30.95.163',54211,0,3),"Au_V":('10.30.95.163',54211,1,3),"PD_V":('10.30.95.163',54211,2,3),
"TEY_I":('10.30.95.170',26),"Au_I":('10.30.95.170',26),"PD_I":('10.30.95.170',26)}
#
O_REXS_DeviceAddress={"TEY_V":('10.30.95.164',54211,0,3),"Au_V":('10.30.95.164',54211,1,3),"PD_V":('10.30.95.164',54211,2,3),
"TEY_I":('10.30.95.170',26),"Au_I":('10.30.95.170',26),"PD_I":('10.30.95.170',26)}

#all address
EndStationAddress=(Q_REXS_DeviceAddress,RXES_DeviceAddress,O_REXS_DeviceAddress)