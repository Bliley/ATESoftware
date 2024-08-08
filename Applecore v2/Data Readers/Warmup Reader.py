import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import MaxNLocator
from matplotlib.dates import DateFormatter, AutoDateLocator
import numpy as np
import pyodbc


def connect_to_database(dc_sn):
    x=[]
    y=[]
    dc_snList=[]
    locationList=[]
    
    server = 'tcp:BTI-PC37\\SQLEXPRESS,49170'
    database = 'AppleCore'
    username = 'ApolloBow1'
    password = '8goodfood!'
    
    try:
        connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')
        cursor = connect.cursor()
        
        cursor.execute("SELECT WorkOrder,SubNumber,TimeStart FROM MASTER WHERE DC_SN= '"+str(dc_sn)+"'") 
        numLink = cursor.fetchone()
        
        if numLink is not None:
            
            cursor.execute("SELECT DC_SN, MAX(WarmupTime) AS WarmupTime FROM WARMUP WHERE WorkOrder ='"+str(numLink[0])+"' AND SubNumber ='"+str(numLink[1])+"' AND TimeStart ='"+str(numLink[2])+"' GROUP BY DC_SN ORDER BY MAX(TimeStart) DESC;")
            items = cursor.fetchall()
            count = 0

            for i in items:
                
                m=i[0]
                n=i[1]

                cursor.execute("SELECT * FROM WARMUP WHERE DC_SN = '" + str(m) + "' AND WarmupTime = '" + str(n) + "' ORDER BY TimeStart DESC, TimeMeasured ASC")
                stats = cursor.fetchall()

                dc_snList.append(str(stats[0][0]))

                nom = float(stats[0][10])*1000000

                locTemp=[]
                for j in range(3,6):
                    locTemp.append(stats[0][j])
                locationList.append(locTemp)

                xTemp=[]
                for j in range(len(stats)):
                    xTemp.append(stats[j][9])
                x.append(xTemp)

                yTemp=[]
                for j in range(len(stats)):
                    numer=float(stats[j][7])-nom
                    denom=float(stats[0][10])
                    yTemp.append(numer/denom)
                y.append(yTemp)
                count+=count+1

            results(x,y,dc_snList,locationList,nom)
        else:
            sg.Popup("Error: DC_SN does not exist")       
            
        cursor.close()
        connect.close()
        
    except Exception as e:
        print(f"Error: {str(e)}")

def results(x,y,dc_snList,locationList,nom):
    passList=[]
    failList=[]
    XPList=[]
    YPList=[]
    XFList=[]
    YFList=[]
    locLPList=[]
    locLFList=[]
    finValP=[]
    finValF=[]

    ppdSpec=2
    y_min = 0
    y_max = 0

    for i in range(len(dc_snList)):
        if (float(ppdSpec) > abs(float(y[i][-1]))):
            passList.append(dc_snList[i])
            XPList.append(x[i])
            YPList.append(y[i])
            locLPList.append(locationList[i])
            finValP.append(float(y[i][-1]))
        else:
            failList.append(dc_snList[i])
            XFList.append(x[i])
            YFList.append(y[i])
            locLFList.append(locationList[i])
            finValF.append(float(y[i][-1]))
    
    combo = [(item, 'FAIL') for item in failList] + [(item, 'PASS') for item in passList]
    dc_snList= [x[0] for x in combo]
    PassFailList= [x[1] for x in combo]
    XList=XFList + XPList 
    YList=YFList + YPList
    locList=locLFList + locLPList
    finVal= finValF +finValP

    sys=locList[0][0]
    rack=locList[0][1]
    pos=locList[0][2]

    val = finVal[0]

    tY_min = min(YList[0])
    tY_max = max(YList[0])

    rang = abs(tY_max) + abs(tY_min)

    layouT = [
        [
            sg.Column([
                [sg.Text('List of DC_SNs \nin current Work Order', font=("Arial", 14, "bold"))],
                [sg.Listbox(combo, size=(20, 6), enable_events=True, key="woDCSN")],
                [sg.Text("", font=("Arial", 14, "bold"))]
            ]),
            sg.Column([
                [sg.Graph((250, 350), (250, 0), (250, 350), key='Graph')],
            ]),
            sg.Column([
                [sg.Text("Location", font=("Arial", 14, "bold"))],
                [sg.Text("System Number: " + sys, font=("Arial", 12), key='Sys')],
                [sg.Text("Rack Number: " + rack, font=("Arial", 12), key='Rack')],
                [sg.Text("Position Number: " + pos, font=("Arial", 12), key='Pos')],
                [sg.Text("Warmup Stats", font=("Arial", 14, "bold"))],
                [sg.Text("Y Maximum: " + f"{tY_max:.2f}" + " ppm", font=("Arial", 12), key='max')],
                [sg.Text("Y Minimum: " + f"{tY_min:.2f}" + " ppm", font=("Arial", 12), key='min')],
                [sg.Text("Range: " + f"{rang:.2f}" + " ppm", font=("Arial", 12), key='range')],
                [sg.Text("Results", font=("Arial", 14, "bold"))],
                [sg.Text("Value: " + f"{val:.2f}" + " ppm", font=("Arial", 12), key='val')],
                [sg.Text("Spec: +/- " + str(ppdSpec) + " ppm", font=("Arial", 12))],
                [sg.Text('', size=(10, 1)), sg.Text(PassFailList[0], font=("Arial", 20), key='pfList')],
            ]),
        ],
        [sg.Text('', size=(55, 1)), sg.Button('Change DC_SN'), sg.Button('Exit')],
    ]

    windoW = sg.Window('Graph Display', layouT, location=(20,20), finalize=True,margins=(100, 100))

    graph = windoW['Graph']                      
    fig, ax = plt.subplots() 

    pad = 0.2
    if abs(tY_max) > abs(tY_min):
        y_min = -(2 + (abs(tY_max) * pad))
        y_max = 2 + (abs(tY_max) * pad)
    else:
        y_min = -(2 + (abs(tY_min) * pad))
        y_max = 2 + (abs(tY_min) * pad)

    ax.plot(XList[0], YList[0],color='#420C09', label='Not fitted', linewidth=1,marker='o')
    ax.grid(True)
    ax.set_xlabel('Time')
    ax.xaxis.set_major_locator(AutoDateLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%M:%S'))
    plt.xticks(rotation=45)
    ax.set_ylabel('Delta Ppm')
    ax.set_ylim(y_min, y_max)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=12))
    ax.set_title('Warmup Plot'+' (' +str(dc_snList[0])+')') 
     
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
            
            val = finVal[indexY]

            tY_min = min(YList[indexY])
            tY_max = max(YList[indexY])

            rang = abs(tY_max) + abs(tY_min)
           
            pad = 0.5
            if abs(tY_max) > abs(tY_min):
                y_min = -(2 + (abs(tY_max) * pad))
                y_max = 2 + (abs(tY_max) * pad)
            else:
                y_min = -(2 + (abs(tY_min) * pad))
                y_max = 2 + (abs(tY_min) * pad)
    
            ax.clear()
            ax.plot(XList[indexY], YList[indexY],color='#420C09', label='Not fitted', linewidth=1,marker='o')
            ax.grid(True)
            ax.set_xlabel('Time')
            ax.xaxis.set_major_locator(AutoDateLocator())
            ax.xaxis.set_major_formatter(DateFormatter('%M:%S'))
            plt.xticks(rotation=45)
            ax.set_ylabel('Delta Ppm')
            ax.set_ylim(y_min, y_max)
            ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=12))
            ax.set_title('Warmup Plot '+' (' +str(dc_snList[indexY])+')')
     
            fig.canvas.draw()
          
            windoW["max"].update("Y Maximum: " + f"{tY_max:.2f}" + " ppm",font=("Arial", 12))
            windoW["min"].update("Y Minimum: " + f"{tY_min:.2f}" + " ppm",font=("Arial", 12))
            windoW["range"].update("Range: " + f"{rang:.2f}" + " ppm",font=("Arial", 12))
            windoW["pfList"].update(PassFailList[indexY],font=("Arial", 20))
            windoW["Sys"].update("System Number: "+sys,font=("Arial", 12))
            windoW["Rack"].update("Rack Number: "+rack,font=("Arial", 12))
            windoW["Pos"].update("Position Number: "+pos,font=("Arial", 12))
            windoW["val"].update("Value: " + f"{val:.2f}" + " ppm", font=("Arial", 12))
    
    windoW.close()



def main():
    try:
        layout = [
            [sg.Text('',size=(5,1)),sg.Text("Warmup Data Checker", font=("Helvetica", 30, "bold"))],
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

