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

index=[]

def connect_to_database(dc_sn):
    x=[]
    y=[]
    dc_snList=[]
    duplicateRun=[]
    try:
        server = 'tcp:BTI-PC37\\SQLEXPRESS,49170' 
        database = 'AppleCore'
        username = 'ApolloBow1'
        password = '8goodfood!'  

        connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')
        cursor = connect.cursor()

        locationList=[]

        cursor.execute("SELECT WorkOrder,SubNumber,SystemNumber,RackNumber FROM FVT WHERE DC_SN= '"+str(dc_sn)+"'") 
        numLink = cursor.fetchone()
        if numLink is not None:
            cursor.execute("SELECT DC_SN, MAX(TimeStart) AS TimeStart FROM FVT WHERE WorkOrder ='"+str(numLink[0])+"' AND SubNumber ='"+str(numLink[1])+"' AND SystemNumber ='"+str(numLink[2])+"' AND RackNumber ='"+str(numLink[3])+"' GROUP BY DC_SN")
            items = cursor.fetchall()
            count = 0
            for i in items: 

                i=str(i)[2:12]       
                cursor.execute("SELECT * FROM FVT WHERE DC_SN= '"+ str(i) +"' ORDER BY TimeMeasured ASC")
                stats = cursor.fetchall()

                checker=stats[0][9]
                tempDuplicate=[]
                for j in range(len(stats)):
                    tempIndex=[]
                    if stats[j][9] > (checker + timedelta(minutes=30)):
                        tempIndex.append(stats[j][0])
                        tempIndex.append(j)
                        count=1
                        for k in range(len(index)):
                            if index[k][0] == stats[j][0]:
                                count+=1
                        tempIndex.append(count)
                        index.append(tempIndex)
                        for k in range(len(stats)):
                            if k >= j:
                                tempDuplicate.append(stats[k]) 
                        duplicateRun.append(tempDuplicate)
                        break
                    else:
                        checker = stats[j][9]

                dc_snList.append(str(stats[0][0]))

                locTemp=[]
                for j in range(3,6):
                    locTemp.append(stats[0][j])
                locationList.append(locTemp)

                xTemp=[]
                for j in range(len(stats)):
                    xTemp.append(stats[j][10])
                x.append(xTemp)

                for j in range(len(stats)):
                    if (j == 0):
                        fMax = float(stats[j][7])
                        fMin = float(stats[j][7])
                    else:
                        if fMax < float(stats[j][7]):
                            fMax = float(stats[j][7])
                        elif fMin > float(stats[j][7]):
                            fMin = float(stats[j][7])    

                yTemp=[]
                nom =(fMax+fMin)/2
                for j in range(len(stats)):
                    numer=(float(stats[j][7])-nom)
                    denom=float(stats[j][11])
                    yTemp.append(1000 * (numer/denom))
                y.append(yTemp)
                count+=count+1
            
            results(x,y,dc_snList,locationList,duplicateRun,count)
        else:
            sg.Popup("Error: DC_SN does not exist")       
            
        # Close cursors and connections when done
        cursor.close()
        connect.close()
        
    except Exception as e:
        print(f"Error: {str(e)}")

def results(x,y,dc_snList,locationList,duplicateRun,count):
    passList=[]
    failList=[]
    XPList=[]
    YPList=[]
    XFList=[]
    YFList=[]
    measNomPList=[]
    measNomFList=[]
    locLPList=[]
    locLFList=[]

    ppdSpec=100
    y_min = 0
    y_max = 0

    for i in range(len(dc_snList)):
        if (float(ppdSpec) > float(max(y[i])) and -float(ppdSpec) < float(min(y[i]))):
            passList.append(dc_snList[i])
            XPList.append(x[i])
            YPList.append(y[i])
            locLPList.append(locationList[i])
        else:
            failList.append(dc_snList[i])
            XFList.append(x[i])
            YFList.append(y[i])
            locLFList.append(locationList[i])
    
    combo = [(item, 'FAIL') for item in failList] + [(item, 'PASS') for item in passList]
    dc_snList= [x[0] for x in combo]
    PassFailList= [x[1] for x in combo]
    XList=XFList + XPList 
    YList=YFList + YPList
    locList=locLFList + locLPList

    sys=locList[0][0]
    rack=locList[0][1]
    pos=locList[0][2]

    tY_min = min(YList[0])
    tY_max = max(YList[0])

    if tY_max > 500 or tY_min < -500:
        axisLim = 1050
    else:
        if tY_max > 100 or tY_min < -100:
            axisLim = 505
        else:
            if tY_max > 50 or tY_min < -50:
                axisLim = 105
            else:
                axisLim = 10.5

    if tY_max > 10 or tY_min < -10:
        maxer = "{:.2f}".format(tY_max)
        miner = "{:.2f}".format(tY_min)
    else:
        maxer = "{:.2e}".format(tY_max)
        miner = "{:.2e}".format(tY_min)

    # Layout for the GUI window
    layouT = [
        [
            sg.Column([
                [sg.Text('List of DC_SNs \nin current Work Order', font=("Arial", 14, "bold"))],
                [sg.Listbox(combo, size=(20, 6), enable_events=True, key="woDCSN")],
                [sg.Text("", font=("Arial", 14, "bold"))],                
            ]),
            sg.Column([
                [sg.Graph((250, 350), (250, 0), (250, 350), key='Graph')],
            ]),
            sg.Column([
                [sg.Text("Location", font=("Arial", 14, "bold"))],
                [sg.Text("System Number: " + sys, font=("Arial", 12), key='Sys')],
                [sg.Text("Rack Number: " + rack, font=("Arial", 12), key='Rack')],
                [sg.Text("Position Number: " + pos, font=("Arial", 12), key='Pos')],
                [sg.Text("Results", font=("Arial", 14, "bold"))],
                [sg.Text("Y Maximum: " + maxer + " ppb", font=("Arial", 12), key='max')],
                [sg.Text("Y Minimum: " + miner + " ppb", font=("Arial", 12), key='min')],
                [sg.Text("Range Spec: +/-" + str(ppdSpec) + " ppb", font=("Arial", 12))],
                [sg.Text('', size=(10, 1)), sg.Text(PassFailList[0], font=("Arial", 20), key='pfList')],
            ]),
        ],
        [sg.Text('', size=(55, 1)), sg.Button('Change DC_SN'), sg.Button('Exit')],
    ]


    # Create the window
    windoW = sg.Window('Graph Display', layouT, location=(20,20), finalize=True,margins=(100, 100))

    graph = windoW['Graph']                      
    fig, ax = plt.subplots()
    

    ax.plot(XList[0], YList[0],color='red', label='Not fitted', linewidth=1,marker='o')
        
    ax.grid(True)
    ax.set_xlabel('Temp')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=10))
    ax.set_ylabel('Delta Ppb')
    ax.set_ylim(-axisLim, axisLim)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=12))
    ax.set_title('FVT Winplot'+' (' +str(dc_snList[0])+')') 
     
    canvas = FigureCanvasTkAgg(fig, graph.Widget)
    plot_widget = canvas.get_tk_widget()
    plot_widget.pack(side='top', fill='both', expand=1)

                       
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

            tY_min = min(YList[indexY])
            tY_max = max(YList[indexY])

            if tY_max > 500 or tY_min < -500:
                axisLim = 1050
            else:
                if tY_max > 100 or tY_min < -100:
                    axisLim = 505
                else:
                    if tY_max > 50 or tY_min < -50:
                        axisLim = 105
                    else:
                        axisLim = 10.5

            if tY_max > 10 or tY_min < -10:
                maxer = "{:.2f}".format(tY_max)
                miner = "{:.2f}".format(tY_min)
            else:
                maxer = "{:.2e}".format(tY_max)
                miner = "{:.2e}".format(tY_min)

            ax.clear()

            ax.plot(XList[indexY], YList[indexY],color='red', label='Not fitted', linewidth=1,marker='o')
                    
            ax.grid(True)
            ax.set_xlabel('Temperatures')
            ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=10))
            ax.set_ylabel('Delta Ppb')
            ax.set_ylim(-axisLim, axisLim)
            ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=12))
            ax.set_title('FVT Winplot '+' (' +str(dc_snList[indexY])+')')
     
            fig.canvas.draw()
          
            windoW["max"].update("Y Maximum: " + maxer + " ppb",font=("Arial", 12))
            windoW["min"].update("Y Minimum: " + miner + " ppb",font=("Arial", 12))
            windoW["pfList"].update(PassFailList[indexY],font=("Arial", 20))
            windoW["Sys"].update("Sys Number: "+sys,font=("Arial", 12))
            windoW["Rack"].update("Rack Number: "+rack,font=("Arial", 12))
            windoW["Pos"].update("Pos Number: "+pos,font=("Arial", 12))
    
    windoW.close()


fullResultString=""

layout = [
    [sg.Text('',size=(5,1)),sg.Text("FVT Data Checker", font=("Helvetica", 30, "bold"))],
    [sg.Text("Please Enter one of the DC_SN from your Work Order", font=("Helvetica", 14))],
    [sg.Text('',size=(5,1)),sg.Text("DC_SN"), sg.Input(key='DCSN')],
    [sg.Text('',size=(20,1)),sg.Button("DC_SN"),sg.Button("EXIT")]
]

window = sg.Window("Data Retrieval", layout, margins=(150, 150))

dc_sn = 0

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "EXIT":
        break
    if event == "DC_SN":
        window.hide()
        dc_sn = values['DCSN']
        connect_to_database(dc_sn)
        window.un_hide()


window.close()
