# this is the test SCPI cmd for keithley 6517B via RS232

# get the version
cmd_version=':SYSTem:VerSion?'

# zero check on
cmd_zch=':SYSTem:ZCHeck?' # 0 is OFF , 1 is ON
cmd_zch_on=':SYSTem:ZCHeck ON'
cmd_zch_off=':SYSTem:ZCHeck OFF'

# enables or disables local lockout.
cmd_lock=':SYSTem:LLOCkout?'
cmd_lock_on=':SYSTem:LLOCkout ON'
cmd_lock_off=':SYSTem:LLOCkout OFF'

# local state and remote state
cmd_local=':SYSTem:LOCal'
cmd_remote=':SYSTem:REMote'

# reads the identification code
cmd_ID='*IDN?' # KEITHLEY INSTRUMENTS INC.,MODEL 6517B,4402161,A13/700x

# *CLS (clear status)
cmd_cls='*CLS'
# reset 6517B
cmd_RST='*RST'
cmd_preset=':SYSTem:PRESet' # Return to :SYST:PRES defaults

# initiate 6517B
cmd_initiate=':INITiate' #  take the Model 6517B out of the idle state
cmd_ini_continuON=':INITiate:CONTinuous ON'# Enable continuous initiation
cmd_ini_continuOFF=':INITiate:CONTinuous OFF'

# Signal-oriented measurement commands
cmd_fetch=':FETCH?' #Requests the latest reading
cmd_config_use=':CONFigure:<function>' #CONFigure:CURR:DC

cmd_read=':READ?' # Performs an :ABORt, :INITiate, and a :FETCh?
cmd_mea=':MEASure[:<function>]?' #Performs an :ABORt, :CONFigure:<function>, and a :READ?

# configure measure current
cmd_config_CURR=':CONFigure:CURR:DC'
cmd_sens_curr=":SENS:FUNC 'CURR'"
cmd_curr_AutoRange=':SENS:CURR:RANGe:AUTO '
cmd_curr_RangeSet=':SENS:CURR:RANGe ' # add [val]:0-21E-3
cmd_curr_nplc=':SENS:CURR:NPLC '# add [val]:0.01-10
cmd_curr_dig=':SENS:CURR:DIG ' # add [val]:4=3.5,5=4.5, 6=5.5, 7=6.5,

# filter type average
cmd_curr_filter=':SENS:CURRent:AVERage:STATe?'
cmd_curr_filterON=':SENS:CURRent:AVERage:STATe ON'
cmd_curr_filterOFF=':SENS:CURRent:AVERage:STATe OFF'
cmd_curr_aver=':SENS:CURR:AVERage:TCONtrol?'
cmd_curr_averREP=':SENS:CURR:AVERage:TCONtrol REPeat'
cmd_curr_averMOV=':SENS:CURR:AVERage:TCONtrol MOVing'
cmd_curr_aver_Num=':SENS:CURR:AVERage:Count ' #add [val]:1-100
cmd_curr_aver_type=':SENS:CURR:AVERage:TYPE?'
cmd_curr_aver_typeADV=':SENS:CURR:AVERage:TYPE ADV' # advanced filter
cmd_curr_aver_typeSCAL=':SENS:CURR:AVERage:TYPE SCALar' # scalar filter
# for noise tolerance +/-1%
cmd_curr_aver_Noise=':SENS:CURR:AVERage:ADVanced:NTOLerance?'
cmd_curr_aver_Noise_N=':SENS:CURR:AVERage:ADVanced:NTOLerance ' # add [val]:1-100

# return a new value
cmd_get_newval=':SENS:DATA:FRESh?'
# filter type median
cmd_curr_median=':SENS:CURRent:median:STATe?'
cmd_curr_medianON=':SENS:CURRent:median:STATe ON'
cmd_curr_medianOFF=':SENS:CURRent:median:STATe OFF'