"""
This is list of the EPICS PV names
"""

# PV names for Energy SE=Soft_Energy
PV_SE_SET = "X20U:OP:PGM1:Soft_Energy.VAL"  # set energy
PV_SE_RBV = "X20U:OP:PGM1:Soft_Energy.RBV"  # energy read back
PV_SE_MV_RTRY = "X20U:OP:PGM1:Soft_Energy.RTRY"  # retries
# PV names for Mirror motion control
PV_MR_SET = "X20U:OP:PGM1:MR.VAL"  # set mirror angle <arcsec>
PV_MR_RBV = "X20U:OP:PGM1:MR.RBV"  # Readback mirror angle <arcsec>
PV_MR_Motor = "X20U:OP:PGM1:MR.DMOV"  # status mirror motor <0,1>
PV_MR_Motor_HLS = "X20U:OP:PGM1:MR.HLS"  # status mirror motor high limit <0,1>
PV_MR_Motor_LLS = "X20U:OP:PGM1:MR.LLS"  # status mirror motor high limit <0,1>
PV_MR_Motor_MOVN = "X20U:OP:PGM1:MR.MOVN"  # status mirror motor moving <0,1>
PV_MR_Motor_DMOV = "X20U:OP:PGM1:MR.DMOV"  # status mirror motor done moving <0,1>
# PV names for Grating Rotation
PV_GR_SET = "X20U:OP:PGM1:GR.VAL"  # set grate angle <arcsec>
PV_GR_RBV = "X20U:OP:PGM1:GR.RBV"  # Readback grate angle <arcsec>
PV_GR_Type = "X20U:OP:PGM1:GRATE_TYPE"  # set grate type GRATE<1,2,3>
PV_GR_Motor = "X20U:OP:PGM1:GR.DMOV"  # status mirror motor <0,1>
PV_GR_Motor_HLS = "X20U:OP:PGM1:GR.HLS"  # status mirror motor high limit <0,1>
PV_GR_Motor_LLS = "X20U:OP:PGM1:GR.LLS"  # status mirror motor high limit <0,1>
PV_GR_Motor_MOVN = "X20U:OP:PGM1:GR.MOVN"  # status mirror motor moving <0,1>
PV_GR_Motor_DMOV = "X20U:OP:PGM1:GR.DMOV"  # status mirror motor done moving <0,1>
