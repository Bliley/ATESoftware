import os
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import math
import numpy as np
from lmfit import Model
import PySimpleGUI as sg
import pyodbc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import ScalarFormatter

def connect_to_database(dc_sn):
    try:
        server = 'tcp:BTI-PC37\\SQLEXPRESS,49170' 
        database = 'AppleCore'
        username = 'ApolloBow1'
        password = '8goodfood!'  

        connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')
        cursor = connect.cursor()

        cursor.execute("SELECT Waveform,NominalFrequency FROM MASTER WHERE DC_SN= '"+str(dc_sn)+"'") 
        waveFreq = cursor.fetchone()
        waveform = waveFreq[0]
        nominal = float(waveFreq[1])

        cursor.execute("SELECT WorkOrder,SubNumber,SystemNumber,RackNumber FROM OSC WHERE DC_SN= '"+str(dc_sn)+"'") 
        numLink = cursor.fetchone()
        if numLink is not None:
            cursor.execute("SELECT DC_SN, MAX(TimeStart) AS TimeStart FROM OSC WHERE WorkOrder ='"+str(numLink[0])+"' AND SubNumber ='"+str(numLink[1])+"' AND SystemNumber ='"+str(numLink[2])+"' AND RackNumber ='"+str(numLink[3])+"' GROUP BY DC_SN")
            items = cursor.fetchall()
            oscData=[]
            for i in items:
                
                j = str(i[0]) 
                k = str (i[1])
                      
                cursor.execute("SELECT * FROM OSC WHERE DC_SN= '"+ j +"' AND TimeStart = '"+ k +"'")
                stats = cursor.fetchone()
                oscData.append(stats)
                
            results(oscData,waveform,nominal)
        else:
            sg.Popup("Error: DC_SN does not exist")       
            
        # Close cursors and connections when done
        cursor.close()
        connect.close()
        
    except Exception as e:
        print(f"Error: {str(e)}")

def results(oscData,waveform,nominal):
    passList=[]
    failList=[]
    isPassingListP=[]
    isPassingListF=[]
    watts=0

    """
    connectPSQL = pyodbc.connect(f"DSN=xTuple")
    cursorPSQL = connectPSQL.cursor()
    cursorPSQL.execute("SELECT wo_itemsite_id FROM wo WHERE wo_number = "+str(numLink[0]) +" AND wo_subnumber = "+str(numLink[1]) +"")
    temp=str(cursorPSQL.fetchone()[0])
    cursorPSQL.execute("SELECT itemsite_item_id FROM itemsite WHERE itemsite_id = " + temp)
    temp=str(cursorPSQL.fetchone()[0])
    cursorPSQL.execute("SELECT charass_value FROM charass WHERE charass_target_id = " +temp +" AND charass_char_id = 57 ")
    ppdSpec=str(cursorPSQL.fetchone()[0])
    cursorPSQL.execute("SELECT * FROM charass WHERE charass_target_id = " +temp +" AND charass_char_id = 58 ")
    print(cursorPSQL.fetchall())
    cursorPSQL.close()
    connectPSQL.close()
    """  

    for i in range(len(oscData)):
        isPassing= ""

        #Deviation
        if (0<float(oscData[i][22])<20 and 0<float(oscData[i][23])<20 and 0<float(oscData[i][24])<20):
            isPassing+='1'
        else:
            isPassing+='0'

        #Frequency
        if (abs(float(oscData[i][19])-float(oscData[i][20]))<10 and abs(float(oscData[i][21])-float(oscData[i][20]))<10 or
            float(oscData[i][21])<float(oscData[i][19])<float(oscData[i][20])):
            isPassing+='1'
        else:
            isPassing+='0'

        #Power
        if (float(oscData[i][9])) == 3.3:
            watts = 1.15
        elif (float(oscData[i][9])) == 5.0:
            watts = 3.5
        else:
            watts = 6    
        
        if (float(oscData[i][10])*float(oscData[i][9])) < watts:
            isPassing+='1'
        else:
            isPassing+='0'

        #Square Waveform Tests
        if waveform == 'Square':

            #State One/Zero
            if (float(oscData[i][9])*.9)<float(oscData[i][11]) and (float(oscData[i][9])*.1)>=float(oscData[i][12]):
                isPassing+='1'
            else:
                isPassing+='0'
                
            #Rise/Fall Time
            if 0<float(oscData[i][13])-float(oscData[i][14])< 1:
                isPassing+='1'
            else:
                isPassing+='0'

            #Symmetry
            if (float(oscData[i][15]) < 55 and 45 < float(oscData[i][15])):
                isPassing+='1'
            else:
                isPassing+='0'
    
            isPassing+='1'

        #Sine Waveform Tests    
        else:
            isPassing+='111'

            #Vpp
            if (4.75<float(oscData[i][16])<5.25):
                isPassing+='1'
            else:
                isPassing+='0'

        #Voltages
        if float(oscData[i][17]) == float(oscData[i][9]) and float(oscData[i][25])==(float(oscData[i][9])/2) and float(oscData[i][18])== 0:
            isPassing+='1'
        else:
            isPassing+='0'

        if ('0' in isPassing):
            failList.append(oscData[i])
            isPassingListF.append(isPassing)
        else:
            passList.append(oscData[i])
            isPassingListP.append(isPassing)

    fDc_snList = []
    pDc_snList = []
    dataset = failList + passList
    isPassingList = isPassingListF + isPassingListP

    for i in range(len(failList)):
        fDc_snList.append(failList[i][0])
    
    failure = [(item, 'FAIL') for item in fDc_snList]

    print(failure)

    for i in range(len(passList)):
        pDc_snList.append(passList[i][0])

    passing = [(item, 'PASS') for item in pDc_snList]

    combo = failure + passing


    dc_snList= [x[0] for x in combo]
    PassFailList= [x[1] for x in combo]

    sys=dataset[0][3]
    rack=dataset[0][4]
    pos=dataset[0][5]

    pfCrit = []
    pf=isPassingList[0]
    if waveform == 'Sine':
        for i in range(0,8):
            if i == 3 or i == 4 or i == 5:
                pfCrit.append('N/A')
            else:
                if pf[i]== '1':
                    pfCrit.append('Pass')
                else:
                    pfCrit.append('Fail')        
    else:
        for i in range(0,8):
            if i == 6:
                pfCrit.append('N/A')
            else:
                if pf[i]== '1':
                    pfCrit.append('Pass')
                else:
                    pfCrit.append('Fail')

    # Layout for the GUI window
    layouT = [
        [
            sg.Column([
            [sg.Text("Location", font=("Arial", 14, "bold"))],
            [sg.Text("System Number: " + sys, font=("Arial", 12), key='Sys')],
            [sg.Text("Rack Number: " + rack, font=("Arial", 12), key='Rack')],
            [sg.Text("Position Number: " + pos, font=("Arial", 12), key='Pos')],
            [sg.Text("", font=("Arial", 14, "bold"))],
            [sg.Text('List of DC_SNs \nin current Work Order', font=("Arial", 14, "bold"))],
            [sg.Listbox(combo, size=(20, 6), enable_events=True, key="woDCSN")],
            [sg.Text("", font=("Arial", 12))],
            [sg.Text(PassFailList[0], font=("Arial", 20, "bold"), key='pfList')],
        ], key='-COL0-'),
        sg.Frame('Results', layout=[
                [
                    sg.Column([
                        [sg.Text("DC_SN: " + dc_snList[0], font=("Arial", 12, "underline bold"), key='dcsn')],
                        [sg.Text("", font=("Arial", 1, "bold"))],
                        [sg.Text("Voltage Supply: " + '{:.2f}'.format(float(dataset[0][9])), font=("Arial", 12), key='vsup')],
                        [sg.Text("Current Supply: " + '{:.2f}'.format(float(dataset[0][10])), font=("Arial", 12), key='csup')],
                        [sg.Text("", font=("Arial", 1, "bold"))],
                        [sg.Text("State One " + '{:.2f}'.format(float(dataset[0][11])), font=("Arial", 12), key='stat1')],
                        [sg.Text("State Zero " + '{:.2f}'.format(float(dataset[0][12])), font=("Arial", 12), key='stat0')],
                        [sg.Text("", font=("Arial", 1, "bold"))],
                        [sg.Text("Rise Time: " + '{:.5f}'.format(float(dataset[0][13])), font=("Arial", 12), key='rise')],
                        [sg.Text("Fall Time: " + '{:.5f}'.format(float(dataset[0][14])), font=("Arial", 12), key='fall')],
                        [sg.Text("", font=("Arial", 1, "bold"))],
                        [sg.Text("Symmetry: " + '{:.2f}'.format(float(dataset[0][15])), font=("Arial", 12), key='sym')],
                        [sg.Text("", font=("Arial", 1, "bold"))],
                        [sg.Text("Vpp: " + '{:.2f}'.format(float(dataset[0][16])), font=("Arial", 12), key='vpp')],
                        [sg.Text("", font=("Arial", 1, "bold"))],
                        [sg.Text("EFC Upper Frequency: " + '{:.2f}'.format(float(dataset[0][20])), font=("Arial", 12), key='efcU freq')],
                        [sg.Text("EFC Middle Frequency: " + '{:.2f}'.format(float(dataset[0][19])), font=("Arial", 12), key='efcM freq')],
                        [sg.Text("EFC Lower Frequency: " + '{:.2f}'.format(float(dataset[0][21])), font=("Arial", 12), key='efcL freq')],
                        [sg.Text("", font=("Arial", 14, "bold"))],
                        [sg.Text("EFC Voltage (Upper): " + '{:.2f}'.format(float(dataset[0][17])), font=("Arial", 12), key='efcU')],
                        [sg.Text("EFC Voltage (Middle): " + str(dataset[0][25]), font=("Arial", 12), key='efcM')],
                        [sg.Text("EFC Voltage (Lower): " + '{:.2f}'.format(float(dataset[0][18])), font=("Arial", 12), key='efcL')],
                        [sg.Text("", font=("Arial", 14, "bold"))],
                        [sg.Text("Middle Deviation: " + '{:.2f}'.format(float(dataset[0][22])), font=("Arial", 12), key='nomDev')],
                        [sg.Text("Upper Deviation: " + '{:.2f}'.format(float(dataset[0][23])), font=("Arial", 12), key='UMDev')],
                        [sg.Text("Lower Deviation: " + '{:.2f}'.format(float(dataset[0][24])), font=("Arial", 12), key='MLDev')],
                    ],key='-COL1-'),
                    sg.Column([
                        [sg.Text("", font=("Arial", 20, "bold"))],
                        [sg.Text(pfCrit[2], font=("Arial", 12, "bold"), key='sup')],
                        [sg.Text("", font=("Arial", 20, "bold"))],
                        [sg.Text(pfCrit[3], font=("Arial", 12, "bold"), key='stat')],
                        [sg.Text("", font=("Arial", 15, "bold"))],
                        [sg.Text(pfCrit[4], font=("Arial", 12, "bold"), key='time')],
                        [sg.Text("", font=("Arial", 5,"bold"))],
                        [sg.Text(pfCrit[5], font=("Arial", 12, "bold"), key='symP')],
                        [sg.Text("", font=("Arial", 4,"bold"))],
                        [sg.Text(pfCrit[6], font=("Arial", 12, "bold"), key='vppP')],
                        [sg.Text("", font=("Arial", 20, "bold"))],
                        [sg.Text(pfCrit[1], font=("Arial", 12, "bold"), key='freq')],
                        [sg.Text("", font=("Arial", 50, "bold"))],
                        [sg.Text(pfCrit[7], font=("Arial", 12, "bold"), key='volt')],
                        [sg.Text("", font=("Arial", 50, "bold"))],
                        [sg.Text(pfCrit[0], font=("Arial", 12, "bold"), key='dev')],
                    ],key='-COL2-')
                ],
            ]),
        ],
        [sg.Text('', size=(35, 1)), sg.Button('Change DC_SN'), sg.Button('Exit')],
    ]

    # Create the window
    windoW = sg.Window('Graph Display', layouT, location=(20,20), finalize=True,margins=(100,50 ))

    while True:
        event, values = windoW.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Change DC_SN':
            selected_items=values['woDCSN'] 
            indexY = dc_snList.index([item[0] for item in selected_items][0])

            pfCrit = []
            pf=isPassingList[indexY]

            if waveform == 'Sine':
                for i in range(0,8):
                    if i == 3 or i == 4 or i == 5:
                        pfCrit.append('N/A')
                    else:
                        if pf[i]== '1':
                            pfCrit.append('Pass')
                        else:
                            pfCrit.append('Fail')        
            else:
                for i in range(0,8):
                    if i == 6:
                        pfCrit.append('N/A')
                    else:
                        if pf[i]== '1':
                            pfCrit.append('Pass')
                        else:
                            pfCrit.append('Fail')

            windoW["dcsn"].update("DC_SN: "+dataset[indexY][0],font=("Arial", 12, "underline bold"))
            windoW["pfList"].update(PassFailList[indexY],font=("Arial", 20))
            windoW["vsup"].update("Voltage Supply: "+'{:.2f}'.format(float(dataset[indexY][9])),font=("Arial", 12))
            windoW["csup"].update("Current Supply: "+'{:.2f}'.format(float(dataset[indexY][10])),font=("Arial", 12))
            windoW["stat1"].update("State One: "+'{:.2f}'.format(float(dataset[indexY][11])),font=("Arial", 12))
            windoW["stat0"].update("State Zero: "+'{:.2f}'.format(float(dataset[indexY][12])),font=("Arial", 12))
            windoW["rise"].update("Rise Time: "+'{:.5f}'.format(float(dataset[indexY][13])),font=("Arial", 12))
            windoW["fall"].update("Fall Time: "+'{:.5f}'.format(float(dataset[indexY][14])),font=("Arial", 12))
            windoW["sym"].update("Symmetry: "+'{:.2f}'.format(float(dataset[indexY][15])),font=("Arial", 12))
            windoW["vpp"].update("Vpp: "+'{:.2f}'.format(float(dataset[indexY][16])),font=("Arial", 12))
            windoW["efcU"].update("EFC Voltage (Upper): "+'{:.2f}'.format(float(dataset[indexY][17])),font=("Arial", 12))
            windoW["efcM"].update("EFC Voltage (Middle): "+str(dataset[indexY][25]),font=("Arial", 12))
            windoW["efcL"].update("EFC Voltage (Lower): "+'{:.2f}'.format(float(dataset[indexY][18])),font=("Arial", 12))
            windoW["efcU freq"].update("EFC Upper Frequency: "+'{:.2f}'.format(float(dataset[indexY][20])),font=("Arial", 12))
            windoW["efcM freq"].update("EFC Middle Frequency: "+'{:.2f}'.format(float(dataset[indexY][19])),font=("Arial", 12))
            windoW["efcL freq"].update("EFC Lower Frequency: "+'{:.2f}'.format(float(dataset[indexY][21])),font=("Arial", 12))
            windoW["nomDev"].update("Middle Deviation: "+'{:.2f}'.format(float(dataset[indexY][22])),font=("Arial", 12))
            windoW["UMDev"].update("Upper Deviation: "+'{:.2f}'.format(float(dataset[indexY][23])),font=("Arial", 12))
            windoW["MLDev"].update("Lower Deviation: "+'{:.2f}'.format(float(dataset[indexY][24])),font=("Arial", 12))
            windoW["Sys"].update("Sys Number: "+dataset[indexY][3],font=("Arial", 12))
            windoW["Rack"].update("Rack Number: "+dataset[indexY][4],font=("Arial", 12))
            windoW["Pos"].update("Pos Number: "+dataset[indexY][5],font=("Arial", 12))
            windoW["sup"].update(pfCrit[2],font=("Arial", 12, "bold"))
            windoW["stat"].update(pfCrit[3],font=("Arial", 12, "bold"))
            windoW["time"].update(pfCrit[4],font=("Arial", 12, "bold"))
            windoW["symP"].update(pfCrit[5],font=("Arial", 12, "bold"))
            windoW["vppP"].update(pfCrit[6],font=("Arial", 12, "bold"))
            windoW["freq"].update(pfCrit[1],font=("Arial", 12, "bold"))
            windoW["volt"].update(pfCrit[7],font=("Arial", 12, "bold"))
            windoW["dev"].update(pfCrit[0],font=("Arial", 12, "bold"))
            
    windoW.close()


fullResultString=""

# Define the layout for the window
layout = [
    [sg.Text('',size=(5,1)),sg.Text("OSC Test Data Checker", font=("Helvetica", 30, "bold"))],
    [sg.Text("Please Enter one of the DC_SN from your Work Order", font=("Helvetica", 14))],
    [sg.Text('',size=(5,1)),sg.Text("DC_SN"), sg.Input(key='DCSN')],
    [sg.Text('',size=(20,1)),sg.Button("DC_SN"),sg.Button("EXIT")]
]

# Create the window
window = sg.Window("Data Retrieval", layout, margins=(150, 150))

# Create variables to store input values
dc_sn = 0

# Create an event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "EXIT":
        break
    if event == "DC_SN":
        # Extract input values
        dc_sn = values['DCSN']
        connect_to_database(dc_sn)

        # You can add your database connection and query code here
        # Make sure to handle exceptions and display results as needed

window.close()
