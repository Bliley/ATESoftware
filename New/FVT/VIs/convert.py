import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import simpledialog, filedialog
import tkinter.font as font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import MaxNLocator,ScalarFormatter
import subprocess
from datetime import datetime

canvas = None
window = Tk()

def load_data(file,pdf):
    global data

    if file:
        data = pd.read_csv(file)
        
        freq = data['Frequency']
        temp = data['Temperature']
        index = (temp - 25).abs().idxmin()
        nom=freq[index]
        if float(temp[len(temp)-1]) < float(temp[0]):
            freq=freq.iloc[::-1]
            temp=temp.iloc[::-1]
        part = data['Unit_Number'][0]
        serial = data['Serial_Number'][0]
        ppb = []

        for j in range(len(freq) - 1, -1, -1):
            numer=(float(freq[j])-nom)
            denom=nom/1000000
            ppb.append(1000 * (numer/denom))

        plot_graph(temp,ppb,part,serial,pdf)

def plot_graph(temp,ppb,part,serial,pdf):
    global canvas
    
    tY_min = min(ppb)
    tY_max = max(ppb)

    if tY_max > 100000 or tY_min < -100000:
        axisLim = 1050000
    else:
        if tY_max > 10000 or tY_min < -10000:
                axisLim = 105000
        else:
            if tY_max > 1000 or tY_min < -1000:
                axisLim = 10500
            else:
                if tY_max > 500 or tY_min < -500:
                    axisLim = 1050
                else:
                    if tY_max > 100 or tY_min < -100:
                        axisLim = 505
                    else:
                        if tY_max > 50 or tY_min < -50:
                            axisLim = 105
                        else:
                            if tY_max > 10 or tY_min < -10:
                                axisLim = 55
                            else:
                                if tY_max > 1 or tY_min < -1:
                                    axisLim = 10.5
                                else:
                                    axisLim = 1.5

    fullRang = "Highest ppb: {:.2f}                                           Lowest ppb: {:.2f}".format(tY_max, tY_min)

    try:
        rangOneIndexS = (temp + 40).abs().idxmin()
        rangOneIndexE = (temp - 85).abs().idxmin()
        oneTempS = temp[rangOneIndexS]
        oneTempE = temp[rangOneIndexE]
        rangOne = ppb[rangOneIndexE: rangOneIndexS + 1]
        maxOne = max(rangOne)
        minOne = min(rangOne)
        diffOne = "{:.2f}".format(maxOne - minOne)
    except Exception as e:
        diffOne = "N/A"

    try:
        rangTwoIndexS = (temp + 20).abs().idxmin()
        rangTwoIndexE = (temp - 70).abs().idxmin()
        twoTempS = temp[rangTwoIndexS]
        twoTempE = temp[rangTwoIndexE]
        rangTwo = ppb[rangTwoIndexE: rangTwoIndexS + 1]
        maxTwo = max(rangTwo)
        minTwo = min(rangTwo)
        diffTwo = "{:.2f}".format(maxTwo - minTwo)
    except Exception as e:
        diffTwo = "N/A"

    try:
        rangThreeIndexS = (temp - 0).abs().idxmin()
        rangThreeIndexE = (temp - 70).abs().idxmin()
        threeTempS = temp[rangThreeIndexS]
        threeTempE = temp[rangThreeIndexE]
        rangThree = ppb[rangThreeIndexE: rangThreeIndexS + 1]
        maxThree = max(rangThree)
        minThree = min(rangThree)
        diffThree = "{:.2f}".format(maxThree - minThree)
    except Exception as e:
        diffThree = "N/A"

    rangRes = "\n                                        -40 -> 85: "+ str(diffOne)+ " ppb\n                                        -20 -> 70: "+ str(diffTwo)+ " ppb\n                                         0 -> 70: " + str(diffThree) + " ppb"

    fig, ax = plt.subplots(figsize=(8, 5), gridspec_kw={'bottom': 0.3, 'top': 0.9})

    ax.plot(temp, ppb,color='red', linewidth=1,marker='o')
    ax.grid(True)
    ax.set_xlabel('Temperature')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=12))
    ax.set_ylabel('Delta ppb')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=12))
    ax.set_ylim(-axisLim, axisLim)

    current_datetime = datetime.now()
    current_date = current_datetime.date()
    
    ax.set_title("Part: " + str(part) + "       SN:" + str(serial) +"       "+ str(current_date))
    
    plt.figtext(0.1, 0.01,fullRang + rangRes, horizontalalignment='left', fontsize=12)

    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

    plt.savefig(pdf+".pdf")

