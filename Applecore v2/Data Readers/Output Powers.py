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
    
    server = 'tcp:BTI-PC37\\SQLEXPRESS,49170'
    database = 'AppleCore'
    username = 'ApolloBow1'
    password = '8goodfood!'
    
    try:
        connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')
        cursor = connect.cursor()
        
        cursor.execute("SELECT WorkOrder,SubNumber,OscVoltage FROM MASTER WHERE DC_SN= '"+str(dc_sn)+"'") 
        numLink = cursor.fetchone()
        
        if numLink is not None:
            
            cursor.execute("SELECT DC_SN, MAX(TimeStart) AS TimeStart FROM OUTPUT_POWERS WHERE WorkOrder ='"+str(numLink[0])+"' AND SubNumber ='"+str(numLink[1])+"' GROUP BY DC_SN")
            items = cursor.fetchall()
            
            for i in items:
                
                i=str(i)[2:12]       
                cursor.execute("SELECT * FROM OUTPUT_POWERS WHERE DC_SN= '"+ str(i) +"' ORDER BY TimeStart DESC, TimeMeasured ASC")
                stats = cursor.fetchall()

                dc_snList.append(str(stats[0][0]))

                volt = float(numLink[2])

                locTemp=[]
                for j in range(3,6):
                    locTemp.append(stats[0][j])
                locationList.append(locTemp)

                xTemp=[]
                for j in range(len(stats)):
                    xTemp.append(stats[j][8])
                x.append(xTemp)

                yTemp=[]
                for j in range(len(stats)):
                    oPowers = stats[j][7].split(',')
                    yTemp.append(oPowers)
                y.append(yTemp)
            results(x,y,dc_snList,locationList,volt)
        else:
            sg.Popup("Error: DC_SN does not exist")       
            
        cursor.close()
        connect.close()
        
    except Exception as e:
        print(f"Error: {str(e)}")

def results(x,y,dc_snList,locationList,volt):
    passList=[]
    failList=[]
    XPList=[]
    YPList=[]
    XFList=[]
    YFList=[]
    locLPList=[]
    locLFList=[]
    
    dBmVal = 12
    spec = 2
    y_min = 0
    y_max = 0

    for i in range(len(dc_snList)):
        counter = 0
        count = 0
        for value in y[i]:
            counter = counter + 1
            for v in value:
                if (float(dBmVal) + float(spec)) > float(v) > (float(dBmVal) - float(spec)):
                    count = count + 1
                else:
                    count = count

        if count == counter * 3:
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

    voltOn = float(volt)
    voltTw = float(volt)/2
    voltTh = 0
    
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
                [sg.Text("Results", font=("Arial", 14, "bold"))],
                [sg.Text("Blue Voltage: " + f"{voltOn:.2f}" + " V", font=("Arial", 12), key='volt1')],
                [sg.Text("Orange Voltage: " + f"{voltTw:.2f}" + " V", font=("Arial", 12), key='volt2')],
                [sg.Text("Green Voltage: " + f"{voltTh:.2f}" + " V", font=("Arial", 12), key='volt3')],
                [sg.Text("Spec: "+ str(dBmVal)+" +/- " + str(spec) + " dBm", font=("Arial", 12))],
                [sg.Text('', size=(10, 1)), sg.Text(PassFailList[0], font=("Arial", 20), key='pfList')],
            ]),
        ],
        [sg.Text('', size=(55, 1)), sg.Button('Change DC_SN'), sg.Button('Exit')],
    ]

    windoW = sg.Window('Graph Display', layouT, location=(20,20), finalize=True,margins=(100, 100))

    graph = windoW['Graph']                      
    fig, ax = plt.subplots()
    
    fL = [float(value) for sublist in YList[0] for value in sublist]
    rL = [float(item) for item in XList[0] for _ in range(3)]

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  
    for i in range(len(rL)):
        color_index = i % 3
        ax.plot(rL[i], fL[i], color=colors[color_index], label='Not fitted', linewidth=1, marker='o',markersize=10)

    for i in range(3):
        ax.plot(rL[i::3], fL[i::3], color=colors[i], linestyle='-')

    ax.grid(True)
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Ppm')
    if (max(fL) - min(fL)> 1):
        ax.set_ylim(min(fL)-5,max(fL)+5)
    else:
        ax.set_ylim(min(fL)-(abs(min(fL))*0.0002),max(fL)+(abs(max(fL))*0.0002))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=5))
    ax.set_title('Output Powers Plot'+' (' +str(dc_snList[0])+')') 
     
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

            fL = [float(value) for sublist in YList[indexY] for value in sublist]
            rL = [float(item) for item in XList[indexY] for _ in range(3)]

            ax.clear()

            colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  
            for i in range(len(rL)):
                color_index = i % 3
                ax.plot(rL[i], fL[i], color=colors[color_index], label='Not fitted', linewidth=1, marker='o',markersize=10)

            for i in range(3):
                ax.plot(rL[i::3], fL[i::3], color=colors[i], linestyle='-')
            
            ax.grid(True)
            ax.set_xlabel('Temperature')
            ax.set_ylabel('Ppm')
            if (max(fL) - min(fL)> 1):
                ax.set_ylim(min(fL)-5,max(fL)+5)
            else:
                ax.set_ylim(min(fL)-(abs(min(fL))*0.0002),max(fL)+(abs(max(fL))*0.0002))
            ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=5))
            ax.set_title('Output Powers Plot'+' (' +str(dc_snList[indexY])+')') 
     
            fig.canvas.draw()
          
            windoW["pfList"].update(PassFailList[indexY],font=("Arial", 20))
            windoW["Sys"].update("Sys Number: "+sys,font=("Arial", 12))
            windoW["Rack"].update("Rack Number: "+rack,font=("Arial", 12))
            windoW["Pos"].update("Pos Number: "+pos,font=("Arial", 12))
    
    windoW.close()



def main():
    try:
        layout = [
            [sg.Text('',size=(5,1)),sg.Text("Output Powers Data Checker", font=("Helvetica", 30, "bold"))],
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

