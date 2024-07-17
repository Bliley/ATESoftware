import pyvisa
from pyvisa.constants import Parity, StopBits, ControlFlow, VI_READ_BUF_DISCARD, VI_WRITE_BUF_DISCARD
import time

def initialize(usb):
    rm = pyvisa.ResourceManager()
    try:
        device = rm.open_resource(usb)
        device.baud_rate = 115200  
        device.data_bits = 8
        device.parity = Parity.none  
        device.stop_bits = StopBits.one
        device.flow_control = ControlFlow.none
        device.read_termination = None
        device.write_termination = '\n'
        
        return device
    except pyvisa.errors.VisaIOError as e:
        return None

def holzCommand(holz,command):
    try:
        holz.write(command)

        time.sleep(1)
        response = holz.read()
        
        return response
    
    except pyvisa.errors.VisaIOError as e:
        return "Failure"

def holzRead(holz):
    try:
        response = holz.read()
        
        return response
    
    except pyvisa.errors.VisaIOError as e:
        return "Failure"

def holzRun(usb,stopFreq):
    holz = initialize(usb)
    if holz:
        holz.flush(VI_READ_BUF_DISCARD)
        holz.flush(VI_WRITE_BUF_DISCARD)

        responses = []
        freqLev = []
        phnLev = []

        tempResponse = ""
        tempFreqLev = ""
        tempPhnLev = ""
        
        responses.append(holzCommand(holz,":SENS:PN:MEAS:TYPE:ABSOLUTE"))
        responses.append(holzCommand(holz,":SENS:PN:MODE:SINGLE"))
        responses.append(holzCommand(holz,":SENS:PN:CORR:COUN:10"))
        responses.append(holzCommand(holz,":SENS:PN:SAMPLES:COUN:512"))
        responses.append(holzCommand(holz,":SENS:PN:VCO:TRUE"))
        responses.append(holzCommand(holz,":SENS:PN:DATA:TYPE:CROSS"))
        responses.append(holzCommand(holz,":SENS:PN:FREQ:STAR:1Hz"))
        responses.append(holzCommand(holz,":SENS:PN:FREQ:STOP:"+str(stopFreq)))
        responses.append(holzCommand(holz,":SENS:PN:LO:STATUS:INT"))
        
        responses.append(holzCommand(holz,":INIT:PN:CAL"))
        while tempResponse.find("Instrument Ready") == -1:
            tempResponse = holzCommand(holz,":STAT:OPER:COND?")
            time.sleep(3)
        responses.append(tempResponse)
        holzRead(holz)
        
        tempResponse = ""
        responses.append(holzCommand(holz,":INIT:PN:IMM"))
        while tempResponse.find("Instrument Ready") == -1:
            tempResponse = holzCommand(holz,":STAT:OPER:COND?")
            time.sleep(3)
        responses.append(tempResponse)
        holzRead(holz)
        
        responses.append(holzCommand(holz,":SENS:PN:SWE:POIN?"))
        
        freqLev = holzCommand(holz,":CALC:PN:DATA:XDAT?")     
        phnLev = holzCommand(holz,":CALC:PN:DATA:FDAT?")
        
        holz.close()

        responsesString = ', '.join(responses)

        freqLev = freqLev.replace(',', '|')
        phnLev = phnLev.replace(',', '|')
        responsesString = responsesString.replace(',', '|')

        results = [freqLev, phnLev, responsesString]

        return results
        

#me = holzRun("ASRL7::INSTR","1MHz")
#rm = pyvisa.ResourceManager()
#print(rm.list_resources())
#print(me)
        

