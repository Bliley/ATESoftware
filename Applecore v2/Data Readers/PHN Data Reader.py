import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import MaxNLocator
import numpy as np
import pyodbc


def connect_to_database(dc_sn):
    x=[]
    y=[]
    dc_snList=[]
    locationList=[]
    phnLev=[]
    freqLev=[]
    
    server = 'tcp:BTI-PC37\\SQLEXPRESS,49170'
    database = 'AppleCore'
    username = 'ApolloBow1'
    password = '8goodfood!'
    
    try:
        connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')
        cursor = connect.cursor()
        
        cursor.execute("SELECT WorkOrder,SubNumber FROM PHN WHERE DC_SN= '"+str(dc_sn)+"'") 
        numLink = cursor.fetchone()
        
        if numLink is not None:
            
            cursor.execute("SELECT DC_SN, MAX(TimeMeasured) AS TimeMeasured FROM PHN WHERE WorkOrder ='"+str(numLink[0])+"' AND SubNumber ='"+str(numLink[1])+"' GROUP BY DC_SN")
            items = cursor.fetchall()
            
            for i in items:
                
                i=str(i)[2:12]

                phnLevTemp = []
                freqLevTemp = []

                for k in range(1,8):
                    freq = 10**k
                    cursor.execute("SELECT * FROM PHN WHERE DC_SN = '"+ str(i) +"' ORDER BY ABS(CONVERT(float, Frequency) - "+ str(freq) +"), TimeMeasured DESC")
                    stats = cursor.fetchall()
                    phnLevTemp.append(float(str(stats[0][9])))
                    freqLevTemp.append(float(str(stats[0][8])))

                phnLev.append(phnLevTemp)
                freqLev.append(freqLevTemp)

                dc_snList.append(str(stats[0][0]))

                locTemp=[]
                for j in range(3,6):
                    locTemp.append(stats[0][j])
                locationList.append(locTemp)

            results(freqLev,phnLev,dc_snList,locationList)
        else:
            sg.Popup("Error: DC_SN does not exist")       
            
        cursor.close()
        connect.close()
        
    except Exception as e:
        print(f"Error: {str(e)}")

def results(freqLev,phnLev,dc_snList,locationList):
    passList=[]
    failList=[]
    freqPList=[]
    phnPList=[]
    freqFList=[]
    phnFList=[]
    locLPList=[]
    locLFList=[]
    
    phnMax = -60

    for i in range(len(dc_snList)):
        count = 0
        for value in phnLev[i]:
            if (float(value) < float(phnMax)):
                count = count + 1
            else:
                count = count

        if count == 7:
            passList.append(dc_snList[i])
            freqPList.append(freqLev[i])
            phnPList.append(phnLev[i])
            locLPList.append(locationList[i])
        else:
            failList.append(dc_snList[i])
            freqFList.append(freqLev[i])
            phnFList.append(phnLev[i])
            locLFList.append(locationList[i])
    
    combo = [(item, 'FAIL') for item in failList] + [(item, 'PASS') for item in passList]
    dc_snList= [x[0] for x in combo]
    PassFailList= [x[1] for x in combo]
    freqList=freqFList + freqPList 
    phnList=phnFList + phnPList
    locList=locLFList + locLPList

    sys=locList[0][0]
    rack=locList[0][1]
    pos=locList[0][2]

    phnOne=phnList[0][0]
    phnTwo=phnList[0][1]
    phnThree=phnList[0][2]
    phnFour=phnList[0][3]
    phnFive=phnList[0][4]
    phnSix=phnList[0][5]
    phnSeven=phnList[0][6]

    freqOne=freqList[0][0]
    freqTwo=freqList[0][1]
    freqThree=freqList[0][2]
    freqFour=freqList[0][3]
    freqFive=freqList[0][4]
    freqSix=freqList[0][5]
    freqSeven=freqList[0][6]
    
    
    layouT = [
        [
            sg.Column([
                [sg.Text('List of DC_SNs \nin current Work Order', font=("Arial", 14, "bold"))],
                [sg.Listbox(combo, size=(20, 6), enable_events=True, key="woDCSN")],
                [sg.Text("", font=("Arial", 14, "bold"))]
            ]),
            sg.Column([
                [sg.Text("Frequency", font=("Arial", 14, "bold"))],
                [sg.Text(f"{freqOne:.2f}", font=("Arial", 12), key='fVal1')],
                [sg.Text(f"{freqTwo:.2f}", font=("Arial", 12), key='fVal2')],
                [sg.Text(f"{freqThree:.2f}", font=("Arial", 12), key='fVal3')],
                [sg.Text(f"{freqFour:.2f}", font=("Arial", 12), key='fVal4')],
                [sg.Text(f"{freqFive:.2f}", font=("Arial", 12), key='fVal5')],
                [sg.Text(f"{freqSix:.2f}", font=("Arial", 12), key='fVal6')],
                [sg.Text(f"{freqSeven:.2f}", font=("Arial", 12), key='fVal7')],
            ]),
            sg.Column([
                [sg.Text("PHN Level", font=("Arial", 14, "bold"))],
                [sg.Text(f"{phnOne:.2f}", font=("Arial", 12), key='pVal1')],
                [sg.Text(f"{phnTwo:.2f}", font=("Arial", 12), key='pVal2')],
                [sg.Text(f"{phnThree:.2f}", font=("Arial", 12), key='pVal3')],
                [sg.Text(f"{phnFour:.2f}", font=("Arial", 12), key='pVal4')],
                [sg.Text(f"{phnFive:.2f}", font=("Arial", 12), key='pVal5')],
                [sg.Text(f"{phnSix:.2f}", font=("Arial", 12), key='pVal6')],
                [sg.Text(f"{phnSeven:.2f}", font=("Arial", 12), key='pVal7')],
            ]),
            sg.Column([
                [sg.Text(dc_snList[0], font=("Arial", 12, "underline bold"), key='dcsn')],
                [sg.Text("Location", font=("Arial", 14, "bold"))],
                [sg.Text("System Number: " + sys, font=("Arial", 12), key='Sys')],
                [sg.Text("Rack Number: " + rack, font=("Arial", 12), key='Rack')],
                [sg.Text("Position Number: " + pos, font=("Arial", 12), key='Pos')],
                [sg.Text("Results", font=("Arial", 14, "bold"))],
                [sg.Text("Spec: "+ str(phnMax)+ " dBm/Hz", font=("Arial", 12))],
                [sg.Text(PassFailList[0], font=("Arial", 20), key='pfList')],
            ]),
        ],
        [sg.Text('', size=(30, 1)), sg.Button('Change DC_SN'), sg.Button('Exit')],
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

            sys=locList[indexY][0]
            rack=locList[indexY][1]
            pos=locList[indexY][2]

            phnOne=phnList[indexY][0]
            phnTwo=phnList[indexY][1]
            phnThree=phnList[indexY][2]
            phnFour=phnList[indexY][3]
            phnFive=phnList[indexY][4]
            phnSix=phnList[indexY][5]
            phnSeven=phnList[indexY][6]

            freqOne=freqList[indexY][0]
            freqTwo=freqList[indexY][1]
            freqThree=freqList[indexY][2]
            freqFour=freqList[indexY][3]
            freqFive=freqList[indexY][4]
            freqSix=freqList[indexY][5]
            freqSeven=freqList[indexY][6]

            windoW["dcsn"].update(dc_snList[indexY],font=("Arial", 12, "underline bold"))
            windoW["fVal1"].update(f"{freqOne:.2f}", font=("Arial", 12))
            windoW["fVal2"].update(f"{freqTwo:.2f}", font=("Arial", 12))
            windoW["fVal3"].update(f"{freqThree:.2f}", font=("Arial", 12))
            windoW["fVal4"].update(f"{freqFour:.2f}", font=("Arial", 12))
            windoW["fVal5"].update(f"{freqFive:.2f}", font=("Arial", 12))
            windoW["fVal6"].update(f"{freqSix:.2f}", font=("Arial", 12))
            windoW["fVal7"].update(f"{freqSeven:.2f}", font=("Arial", 12))
            windoW["pVal1"].update(f"{phnOne:.2f}", font=("Arial", 12))
            windoW["pVal2"].update(f"{phnTwo:.2f}", font=("Arial", 12))
            windoW["pVal3"].update(f"{phnThree:.2f}", font=("Arial", 12))
            windoW["pVal4"].update(f"{phnFour:.2f}", font=("Arial", 12))
            windoW["pVal5"].update(f"{phnFive:.2f}", font=("Arial", 12))
            windoW["pVal6"].update(f"{phnSix:.2f}", font=("Arial", 12))
            windoW["pVal7"].update(f"{phnSeven:.2f}", font=("Arial", 12))
            windoW["pfList"].update(PassFailList[indexY],font=("Arial", 20))
            windoW["Sys"].update("Sys Number: "+sys,font=("Arial", 12))
            windoW["Rack"].update("Rack Number: "+rack,font=("Arial", 12))
            windoW["Pos"].update("Pos Number: "+pos,font=("Arial", 12))
    
    windoW.close()


def main():
    try:
        layout = [
            [sg.Text('',size=(5,1)),sg.Text("Phase Noise Data Checker", font=("Helvetica", 30, "bold"))],
            [sg.Text("Please Enter one of the DC_SN from your Work Order", font=("Helvetica", 14))],
            [sg.Text('',size=(5,1)),sg.Text("DC_SN"), sg.Input(key='DCSN')],
            [sg.Text('',size=(20,1)),sg.Button("Enter"),sg.Button("Exit")]
        ]

        window = sg.Window("Data Retrieval", layout, margins=(150, 150))

        dc_sn = 0

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Exit":
                break
            if event == "Enter":
                window.hide()
                dc_sn = values['DCSN']
                connect_to_database(dc_sn)
                window.un_hide()
    except:
        sg.Popup("Connection to database failed. Talk to Engineer")

    window.close()

main()

