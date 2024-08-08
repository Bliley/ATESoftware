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
import matplotlib.dates as mdates


x=[]
y=[]
ppbPD=[]
ppbPY=[]
dc_snList=[]

def nonlinear_model(x, a, b, c):
    return a+b*np.log(abs(1+c*x))

def connect_to_database(dc_sn,  startTime, endTime):
    dc_snList=[]
    x=list(range(int(startTime),int(endTime)))
    y=[]
    try:
        server = 'tcp:BTI-PC37\\SQLEXPRESS,49170' 
        database = 'AppleCore'
        username = 'ApolloBow1'
        password = '8goodfood!'  

        connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')
        cursor = connect.cursor()

        ageRateDList =[]
        ageRateYList = []
        rmsList = []
        err=False

        cursor.execute("SELECT WorkOrder,SubNumber,TimeStart FROM AGING WHERE DC_SN= '"+str(dc_sn)+"'") 
        numLink = cursor.fetchone()
        if numLink is not None:
            cursor.execute("SELECT NominalFrequency,RackNumber,TimeStart FROM MASTER WHERE DC_SN= '"+str(dc_sn)+"'")
            res = cursor.fetchone()
            nominal = res[0]
            rackNumber = res[1]
            timeStart = res[2]
            
            rackNumb1 = 0;
            rackNumb2 = 0;
            
            if (float(rackNumber) == 1):
                rackNumb1 = 1;
                rackNumb2 = 2;
            elif (float(rackNumber) == 2):
                rackNumb1 = 1;
                rackNumb2 = 2;
            elif (float(rackNumber) == 3):
                rackNumb1 = 3;
                rackNumb2 = 4;
            elif (float(rackNumber) == 4):
                rackNumb1 = 3;
                rackNumb2 = 4;
            elif (float(rackNumber) == 5):
                rackNumb1 = 5;
                rackNumb2 = 6;
            elif (float(rackNumber) == 6):
                rackNumb1 = 5;
                rackNumb2 = 6;
            elif (float(rackNumber) == 7):
                rackNumb1 = 7;
                rackNumb2 = 8;
            elif (float(rackNumber) == 8):
                rackNumb1 = 7;
                rackNumb2 = 8;
            elif (float(rackNumber) == 9):
                rackNumb1 = 9;
                rackNumb2 = 10;
            elif (float(rackNumber) == 10):
                rackNumb1 = 9;
                rackNumb2 = 10;
            elif (float(rackNumber) == 11):
                rackNumb1 = 11;
                rackNumb2 = 12;
            elif (float(rackNumber) == 12):
                rackNumb1 = 11;
                rackNumb2 = 12;
            elif (float(rackNumber) == 13):
                rackNumb1 = 13;
                rackNumb2 = 14;
            elif (float(rackNumber) == 14):
                rackNumb1 = 13;
                rackNumb2 = 14;
            elif (float(rackNumber) == 15):
                rackNumb1 = 15;
                rackNumb2 = 16;
            elif (float(rackNumber) == 16):
                rackNumb1 = 15;
                rackNumb2 = 16;

            startT = numLink[2] - timedelta(days=1)
            endT = numLink[2] + timedelta(days=1)
            query = """
                SELECT DC_SN, SystemNumber, RackNumber, PositionNumber, Frequency, TimeMeasured 
                FROM AGING 
                WHERE WorkOrder = ? 
                AND SubNumber = ? 
                AND (RackNumber = ? OR RackNumber = ?)
                AND TimeStart >= DATEADD(day, -3, ?)
                AND DC_SN IN (
                    SELECT DC_SN 
                    FROM AGING
                    WHERE WorkOrder = ? 
                    AND SubNumber = ? 
                    AND (RackNumber = ? OR RackNumber = ?)
                    AND TimeStart >= DATEADD(day, -3, ?)
                    GROUP BY DC_SN
                    HAVING COUNT(*) >= 1
                )
                ORDER BY TimeMeasured DESC
            """

            params = (numLink[0], numLink[1], rackNumb1, rackNumb2, timeStart, numLink[0], numLink[1], rackNumb1, rackNumb2, timeStart)
            cursor.execute(query, params)
            dataPoints = cursor.fetchall()
            query = """
                SELECT DISTINCT DC_SN 
                FROM AGING
                WHERE WorkOrder = ? 
                AND SubNumber = ? 
                AND (RackNumber = ? OR RackNumber = ?)
                AND TimeStart >= DATEADD(day, -3, ?)
                AND DC_SN IN (
                    SELECT DC_SN 
                    FROM AGING
                    WHERE WorkOrder = ? 
                    AND SubNumber = ? 
                    AND (RackNumber = ? OR RackNumber = ?)
                    AND TimeStart >= DATEADD(day, -3, ?)
                    GROUP BY DC_SN
                    HAVING COUNT(*) >= 1
                )
            """

            params = (numLink[0], numLink[1], rackNumb1, rackNumb2, timeStart, numLink[0], numLink[1], rackNumb1, rackNumb2, timeStart)
            cursor.execute(query, params)
            items = cursor.fetchall()
            for i in items:
                yTemp=[]
                
                if 'E' in str(i):
                    i=str(i)[2:7]
                else:
                    i=str(i)[2:12]
                    
                cursor.execute("SELECT * FROM AGING_STATS WHERE DC_SN= '"+ str(i) +"'")
                stats = cursor.fetchone()
                
                dc_snList.append(str(stats[0]))

                a=float(stats[1])
                b=float(stats[2]) 
                c=float(stats[3])

                ageRateDList.append(str(stats[4]))
                #ageRateYList.append(str(stats[5]))
                ageRateYList.append(a+b*math.log10(abs(1+c*365.25)))
                rmsList.append(str(stats[6]))

                for j in x:
                    yTemp.append(a+b*math.log10(abs(1+c*j)))
                y.append(yTemp)
                
        else:
            sg.popup("DC_SN does not exist")
            err=True
            
        cursor.close()
        connect.close()

        if not err:
            results(x,y,dc_snList,numLink,ageRateDList,ageRateYList,rmsList,dataPoints,startTime,endTime,nominal)
    except Exception as e:
        print(f"Error: {str(e)}")

def results(x,y,dc_snList,numLink,ageRateDList,ageRateYList,rmsList,dataPoints,startTime,endTime,nominal):

    passList = []
    failList = []
    recordFailure = []
    tempDPList = []
    tempYPList = []
    tYPList = []
    tempDFList = []
    tempYFList = []
    tYFList = []

    ppdSpec = '1'
    ppySpec = '100'
    
    for i in range(len(dc_snList)):
        has_invalid_frequency = False
        
        for index, value in enumerate(dataPoints):
            if value[0] == dc_snList[i]:
                frequency = float(value[4])
                if frequency == -1 or frequency == 50000000000.000000:
                    recordFailure.append(dc_snList[i])
                    has_invalid_frequency = True
                    break

        if has_invalid_frequency:
            continue

        if ((float(ppdSpec) > float(ageRateDList[i])) and float(ageRateDList[i]) > 0) or ((-float(ppdSpec) < float(ageRateDList[i])) and float(ageRateDList[i]) < 0):
            if ((float(ppySpec) > float(ageRateYList[i]) * 1000) and float(ageRateYList[i]) * 1000 > 0) or ((-float(ppySpec) < float(ageRateYList[i]) * 1000) and float(ageRateYList[i]) * 1000 < 0):
                passList.append(dc_snList[i])
                tempDPList.append(ageRateDList[i])
                tempYPList.append(ageRateYList[i])
                tYPList.append(y[i])
            else:
                failList.append(dc_snList[i])
                tempDFList.append(ageRateDList[i])
                tempYFList.append(ageRateYList[i])
                tYFList.append(y[i])
        else:
            failList.append(dc_snList[i])
            tempDFList.append(ageRateDList[i])
            tempYFList.append(ageRateYList[i])
            tYFList.append(y[i])

    combo = [(item, 'FAIL') for item in failList] + [(item, 'PASS') for item in passList]
    dc_snList = [x[0] for x in combo]
    PassFailList = [x[1] for x in combo]
    ageRateDList = tempDFList + tempDPList
    ageRateYList = tempYFList + tempYPList
    y = tYFList + tYPList

    freqs = []
    time = []
    x1 = []
    location = 0
    
    for index, value in enumerate(dataPoints):
        if value[0] == dc_snList[0]:
            freqs.append((float(dataPoints[index][4])-(1000000*float(nominal)))/float(nominal))
            time.append(dataPoints[index][5])
            location = index
    
    baseppb=freqs[0]
    freqs=freqs[1:]
    time=time[1:]
    timeStart = time[-1]

    for i in range(len(freqs)):
        if freqs[i] > 0:
            freqs[i] = freqs[i] - baseppb
        else:
            freqs[i] = freqs[i] + baseppb

    for i in range(len(y[0])):
        x1.append(timeStart + timedelta(days=1) * i)

    for i in range(len(y[0])):
        y[0][i] = freqs[0] + y[0][i]

    layouT = [
        [
            sg.Column([
                [sg.Text('List of DC_SNs \nin current Work Order', font=("Arial", 14, "bold"))],
                [sg.Text('Faulty Readings', font=("Arial", 14, "bold"))],
                [sg.Multiline('\n'.join(recordFailure), size=(20, 6), disabled=True, key="recordFailure")],
                [sg.Text('Intact Readings', font=("Arial", 14, "bold"))],
                [sg.Listbox(combo, size=(20, 6), enable_events=True, key="woDCSN")],
                [sg.Button('Change DC_SN'), sg.Button('Exit')],
            ]),
             sg.Column([
                [sg.Graph((60, 90), (60, 0), (60, 90), key='Graph')],
            ]),
            sg.Column([
                [sg.Graph((60, 90), (60, 0), (60, 90), key='Graph2')],
            ]),
            sg.Column([
                [sg.Text("Location", font=("Arial", 14, "bold"))],
                [sg.Text("System Number: " + dataPoints[location][1], font=("Arial", 12), key='Sys')],
                [sg.Text("Rack Number: " + dataPoints[location][2], font=("Arial", 12), key='Rack')],
                [sg.Text("Position Number: " + dataPoints[location][3], font=("Arial", 12), key='Pos')],
                [sg.Text("Results", font=("Arial", 14, "bold"))],
                [sg.Text("Rate at 30 Days: " + f"{float(ageRateDList[0]):.3f}"+ " ppb/day", font=("Arial", 12), key='Pass')],
                [sg.Text("Value at 1 Year: " + f"{float(ageRateYList[0]) * 1000:.3f}" + " ppb/day", font=("Arial", 12), key='Fail')],
                [sg.Text("RMS Error: " + str(float(rmsList[0])), font=("Arial", 12), key='RMS')],
                [sg.Text("Aging Specs", font=("Arial", 14, "bold"))],
                [sg.Text("Less than " + ppdSpec + " ppb per day", font=("Arial", 12))],
                [sg.Text("Less than " + ppySpec + " ppb at 1 Year", font=("Arial", 12))],
                [sg.Text('', size=(10, 1)), sg.Text(PassFailList[0], font=("Arial", 20), key='pfList')],
            ]),
        ],
    ]

    windoW = sg.Window('Graph Display', layouT,location=(20,20),resizable=True,finalize=True)

    graph = windoW['Graph']
    graph2 = windoW['Graph2']                        
    fig, ax = plt.subplots(figsize=(5, 4)) 
    fig2, ax2 = plt.subplots(figsize=(5, 4))

    ax.plot(x1, y[0],color='#0502A8',label='Fitted')
    ax.grid(True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Fitted Delta Ppb')
    ax.set_title('Aging Curve Fit'+' (' +str(dc_snList[0])+')')
    
    ax2.plot(time, freqs, '#420C09', label='Not fitted', linewidth=1,marker='o')
    ax2.grid(True)
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Delta Ppb')
    ax2.set_title('Aging Data'+' (' +str(dc_snList[0])+')')

    xlim = ax2.get_xlim()
    ylim = ax2.get_ylim()

    date_formatter = mdates.DateFormatter('%m-%d') 

    ax.xaxis.set_major_formatter(date_formatter)
    ax2.xaxis.set_major_formatter(date_formatter)
      
    canvas = FigureCanvasTkAgg(fig, graph.Widget)
    plot_widget = canvas.get_tk_widget()
    plot_widget.pack(side='top', fill='both', expand=1)

    canvas2 = FigureCanvasTkAgg(fig2, graph2.Widget)
    plot_widget2 = canvas2.get_tk_widget()
    plot_widget2.pack(side='top', fill='both', expand=1)                        

    while True:
        event, values = windoW.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Change DC_SN':
            selected_items=values['woDCSN'] 
            indexY = dc_snList.index([item[0] for item in selected_items][0])

            freqs = []
            time = []
            x1 = []
            location = 0

            for index, value in enumerate(dataPoints):
                if value[0] == dc_snList[indexY]:
                    freqs.append((float(dataPoints[index][4])-(1000000*float(nominal)))/40)
                    time.append(dataPoints[index][5])
                    location = index

            baseppb=freqs[0]
            freqs=freqs[1:]
            time=time[1:]
            timeStart = time[-1]

            for i in range(len(y[indexY])):
                x1.append(timeStart + timedelta(days=1) * i)

            for i in range(len(y[indexY])):
                y[indexY][i] = freqs[0] + y[indexY][i]

            ax.clear()
            ax.plot(x1, y[indexY],color='#0502A8',label='Fitted')
            ax.grid(True)
            ax.set_xlabel('Date')
            ax.set_ylabel('Fitted Delta Ppb')
            ax.set_title('Aging Curve Fit'+' (' +str(dc_snList[indexY])+')')

            ax2.clear()
            ax2.plot(time, freqs, '#420C09', label='Not fitted', linewidth=1,marker='o')
            ax2.grid(True)
            ax2.set_xlabel('Date')
            ax2.set_ylabel('Delta Ppb')
            ax2.set_title('Aging Data'+' (' +str(dc_snList[indexY])+')')

            xlim = ax2.get_xlim()
            ylim = ax2.get_ylim()

            ax.xaxis.set_major_formatter(date_formatter)
            ax2.xaxis.set_major_formatter(date_formatter)
                 
            fig.canvas.draw()
            fig2.canvas.draw()
            windoW["Pass"].update("Rate at 30 Days: "+f"{float(ageRateDList[indexY]):.3f}"+ " ppb")
            windoW["Fail"].update("Value at 1 Year: "+f"{float(ageRateYList[indexY]) * 1000:.3f}"+ " ppb")    
            windoW["RMS"].update("RMS Error: "+str(float(rmsList[indexY])))   
            windoW["pfList"].update(PassFailList[indexY],font=("Arial", 20))
            windoW["Sys"].update("Sys Number: "+dataPoints[location][1],font=("Arial", 12))
            windoW["Rack"].update("Rack Number: "+dataPoints[location][2],font=("Arial", 12))
            windoW["Pos"].update("Pos Number: "+dataPoints[location][3],font=("Arial", 12))
    
    windoW.close()


fullResultString=""

layout = [
    [sg.Text('',size=(5,1)),sg.Text("Aging Data Checker", font=("Helvetica", 30, "bold"))],
    [sg.Text("Please Enter one of the DC_SN from your Work Order and", font=("Helvetica", 14))],
    [sg.Text('',size=(3,1)),sg.Text("indicate the start/end time for your fitted curve", font=("Helvetica", 14))],
    [sg.Text('',size=(4,1)),sg.Text("DC_SN"), sg.Input(key='DCSN')],
    [sg.Text('',size=(20,1)),sg.Button("DC_SN"),sg.Button("EXIT")]
]

window = sg.Window("Data Retrieval", layout,resizable=True,margins=(150, 150))

dc_sn = 0

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "EXIT":
        break
    if event == "DC_SN":
        wo=""
        dc_sn = values['DCSN']
        connect_to_database(dc_sn,0,30)

window.close()
