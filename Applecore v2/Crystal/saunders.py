"""
Author: Benjamin Wolford
Master Class makes a GUI that gets the size of the wheel and the positions in each row and proceeds to run the Saunders software 
"""
import subprocess
import pyodbc
import math
import sys
import numpy as np
import pandas as pd
import PySimpleGUI as sg
import keyboard as kb
import time
import os
import pynput as pp
import shareplum as sp
import requests_ntlm as rn
import psutil
from datetime import datetime
from run import *

#-----------------------------------------------------------------------------------------------------------------------------------
#Global Variables 

#Starts/Stops Input to Mouse
mouse_listener = pp.mouse.Listener(suppress=True)

#Starts/Stops Input to Keyboard
keyboard_listener = pp.keyboard.Listener(suppress=True)

#Acts as location for excel files when read into python through pandas
dataframe = [""]
   
#-----------------------------------------------------------------------------------------------------------------------------------
#Functions



def dcsnFormat(text: str):
   period="."
   index=text.find(period)
   if (index != 4):
      return False
   else:
      dcSN=text.split(".")
      dc=dcSN[0]
      sn=dcSN[1]
      if (len(dc) == 4 and dc.isnumeric() and len(sn) == 5):
         return True
      else:
         return False

#Grabs the excel file for the PISN associated with the work order
#psin-Name of the file associated with the work order
def pisnGrabber(pisn: str):
   #Site and Credentials for login
   sharePoint = 'https://blileytechnoligies.sharepoint.com/'
   credU = 'bwolford@bliley.com'
   credP = '4HmH7ql^$6'

   #auth = rn.HttpNtlmAuth(credU,credP)
   #site = sp.Site(sharePoint,auth=auth)

   #folder=site.Folder('Shared%20Documents/Forms/AllItems.aspx?viewpath=%2FShared%20Documents%2FForms%2FAllItems%2Easpx&id=%2FShared%20Documents%2FXTuple%20Integration%2F_Project%20Rey%2FXtuple%20Router%20and%20BOMS%2FPISNs&viewid=f70112e5-64e0-4452-b960-a45e548d209d')

   #file=pisn+'.xlsx'
   
   #fileLocation='C:/Users/system8/Desktop/PISNs/'+file
   #with open(fileLocation,'wb') as f:
      #folder.download(file,f)
   #Going to sharepoint site with PISN #MAKE SURE TO FIX BACK TO SHAREPOINT
   global dataframe
   dataframe = pd.read_excel(r"C:\Users\system8\Desktop\Saunders\QC100LPLNH.G000_PISN.xlsx")
   #os.remove(fileLocation)

#Extracts all the necessary information from datafram and opens the Saunders Chamber 1 software
#crystalA-The number of positions that are in row A
#crystalB-The number of positions that are in row B
#wheel-The type of physical wheel that the crystals will be placed on (40 or 80)
def sW22002(crystalA: int, crystalB: int, wheel: str, dcSnArray):

   try:
      #Blocks the Keyboard and Mouse from input while running code   
      #mouse_listener.start()
      #keyboard_listener.start()

      #Creates variable that is used to ensure data is grabbed from PISN correctly
      err=0
      
      #Getting Frequency in Mhz
      try:
         freq=dataframe["Unnamed: 1"][3]
         freOver=freq.split(" ")
         mhz=float(freOver[0])
      except Exception as e:
         sg.Popup("Error in grabbing Frequency")
         print(e)
         err+=1
         
      #Getting Resonance/Load Capacity/Mode
      try:
         if("Resonance" in dataframe["Crystal Test Specs"][1]):
            resonance=str(dataframe["Unnamed: 7"][1])
         else:
            err+=1
         
         if("Load Capacity" in dataframe["Crystal Test Specs"][2]):
            loadCap=str(dataframe["Unnamed: 7"][2])
         else:
            err+=1

         if("Mode" in dataframe["Crystal Test Specs"][3]):
            mode=str(dataframe["Unnamed: 7"][3])
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing Resonance, Load Capacity, or Mode")
         print(e)
         err+=1

      #Getting val, unit, and Ohm
      try:
         if("Drive Level" in dataframe["Crystal Test Specs"][4]):
            dL=str(dataframe["Unnamed: 7"][4])
            driLev=dL.split(" ")
            val=driLev[0]
            unit=driLev[1].replace("µ","u")
         else:
            err+=1

         if("Drive Level Into [Ohms]" in dataframe["Crystal Test Specs"][5]):
            dI=str(dataframe["Unnamed: 7"][5])
            driInto=dI.split(" ")
            ohm=driInto[0]
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing Drive Level Information")
         print(e)
         err+=1

      #Getting the Calibration temp and tolerance
      try:
         if("Calibration Tolerance" in dataframe["Crystal Test Specs"][7]):
            calT=str(dataframe["Unnamed: 7"][7])
            calTol=calT.split(" ")[0]
         else:
            err+=1

         if("Calibration Temp" in dataframe["Crystal Test Specs"][8]):
            caliT=str(dataframe["Unnamed: 7"][8])
            caliTemp=caliT.split(" ")[0]
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing Calibration Information")
         print(e)
         err+=1


      #Getting the Turning Point Type and Range
      try:
         if("TP Type" in dataframe["Crystal Test Specs"][11]):
            tp=str(dataframe["Unnamed: 7"][11])
            tpType=tp.split(" ")[0]
         else:
            err+=1

         if("TP Range" in dataframe["Crystal Test Specs"][12]):
            tp=str(dataframe["Unnamed: 7"][12])
            tpRange=tp.split(" ")
            tpLTemp=tpRange[0].replace("+","")
            tpUTemp=tpRange[3].replace("+","")
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing Turning Point Information")
         print(e)
         err+=1

      #Getting Resistance
      try:
         if("Resistance R [Ω]" in dataframe["Crystal Test Specs"][13]):
            res=str(dataframe["Unnamed: 7"][13])
            resA=res.split(" ")
            resist=int(resA[0])
            resist=resA[0]
         else:
            err+=1

         if("Resistance R Type" in dataframe["Crystal Test Specs"][14]):
            resType=dataframe["Unnamed: 7"][14]
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing Resistance Information")
         print(e)
         err+=1

      #Getting c0 Information
      try:
         if("Shunt Capacitance C0 [pF] Min" in dataframe["Crystal Test Specs"][15]):
            c0=str(dataframe["Unnamed: 7"][15])
            c0Min=c0.split(" ")[0]
         else:
            err+=1

         if("Shunt Capacitance C0 [pF] Max" in dataframe["Crystal Test Specs"][17]):
            c0=str(dataframe["Unnamed: 7"][17])
            c0Max=c0.split(" ")[0]
         else:
            err+=1
      
      except Exception as e:
         sg.Popup("Error in grabbing C0 Information")
         print(e)
         err+=1

      #Getting c1 Information
      try:
         if("Motional Capacitance C1 [fF] Min" in dataframe["Crystal Test Specs"][18]):
            c1=str(dataframe["Unnamed: 7"][18])
            c1Min=c1.split(" ")[0]
         else:
            err+=1

         if("Motional Capacitance C1 [fF] Max" in dataframe["Crystal Test Specs"][20]):
            c1=str(dataframe["Unnamed: 7"][20])
            c1Max=c1.split(" ")[0]
         else:
            err+=1
      
      except Exception as e:
         sg.Popup("Error in grabbing C1 Information")
         print(e)
         err+=1

      #Getting Q factor
      try:
         if("Quality Factor Q [k]" in dataframe["Crystal Test Specs"][21]):
            q=str(dataframe["Unnamed: 7"][21])
            qFactor=q.split(" ")[0]
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing Q Factor Information")
         print(e)
         err+=1

      #Getting lTemp, uTemp, and step
      try:
         if("FvT Test Range" in dataframe["Crystal Test Specs"][22]):
            temps=str(dataframe["Unnamed: 7"][22])
            fvt=temps.split(" ")
            lTemp=fvt[0].replace("+","")
            uTemp=fvt[3].replace("+","")
         else:
            err+=1

         if("FvT Test Step Size" in dataframe["Crystal Test Specs"][23]):
            steps=str(dataframe["Unnamed: 7"][23])
            fvtStep=steps.split(" ")
            step=fvtStep[0].replace("+","")
         else:
            err+=1
      
      except Exception as e:
         sg.Popup("Error in grabbing Temperature Information")
         print(e)
         err+=1

      #Getting the Extra Test that will be run on the crystal
      try:
         if("Extra Tests (Comma Separated)" in dataframe["Crystal Test Specs"][25]):
            xtraTests=str(dataframe["Unnamed: 7"][25])
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing Extra Tests Information")
         print(e)
         err+=1
      
      #Getting DLD variables for the sweep
      try:
         if("DLD Test Limit [ppm]" in dataframe["Crystal Test Specs"][26]):
            dldPPM=str(dataframe["Unnamed: 7"][26])
         else:
            err+=1
         
         if("DLD Test Limit [ohm]" in dataframe["Crystal Test Specs"][27]):
            dldOhm=str(dataframe["Unnamed: 7"][27])
         else:
            err+=1

         if("DLD Lower Bound" in dataframe["Crystal Test Specs"][28]):
            dldLB=str(dataframe["Unnamed: 7"][28])
         else:
            err+=1

         if("DLD Upper Bound" in dataframe["Crystal Test Specs"][29]):
            dldUB=str(dataframe["Unnamed: 7"][29])
         else:
            err+=1
         
         if("DLD Steps" in dataframe["Crystal Test Specs"][30]):
            dldStep=str(dataframe["Unnamed: 7"][30])
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing DLD Information")
         print(e)
         err+=1

      #Getting Pullability variables for the sweep
      try:
         if("Pullabilty [pF]" in dataframe["Crystal Test Specs"][31]):
            pullPf=str(dataframe["Unnamed: 7"][31])
         else:
            err+=1
            
         if("Pullabilty [Hz/ppm]" in dataframe["Crystal Test Specs"][32]):
            pullHzPpm=str(dataframe["Unnamed: 7"][32])
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing Extra Tests Information")
         print(e)
         err+=1
         
      #Getting Spur Ratio
      try:
         if("Spur ratio" in dataframe["Crystal Test Specs"][33]):
            spurRat=str(dataframe["Unnamed: 7"][33])
         else:
            err+=1

      except Exception as e:
         sg.Popup("Error in grabbing Extra Tests Information")
         print(e)
         err+=1

      #Getting Spurious Mode(s)
      try:
         spurious_list = []

         if "Spurious Mode" in dataframe["Crystal Test Specs"][34]:
            spurious_list.append(str(dataframe["Unnamed: 7"][34]))
         else:
            err += 1

         i = 35

         while i < len(dataframe["Crystal Test Specs"]):
            while "Spurious Mode" in dataframe["Crystal Test Specs"][i]:
               spurious_list.append(str(dataframe["Unnamed: 7"][i]))
               i += 1

      except Exception as e:
               sg.Popup("Error in grabbing Spurious Mode Information")
               print(e)
               err+=1

   except Exception as e:
      sg.Popup("Error collecting PISN information")
      print(e)
      err+=1

   finally:
      run=0
      if(err == 0):
         try:
            os.startfile("C:\\Users\\system8\\Desktop\\W-2200 Chamber 2.lnk")
            #Runs Functions to setup Saunders software
            time.sleep(10)
            s250B(mhz,resonance,loadCap,mode,val,unit,ohm,calTol,tpType,tpLTemp,
                  tpUTemp,resist,resType,c0Min,c0Max,c1Min,c1Max,qFactor,
                  xtraTests,dldPPM,dldOhm,dldLB,dldUB,dldStep,pullHzPpm,pullPf,spurRat,
                  spurious_list)
            time.sleep(1)
            #configure(crystalA,crystalB,wheel)
            time.sleep(1)
            #temp(caliTemp,lTemp, uTemp, step)
            time.sleep(1)
            #sPrint()
            time.sleep(1)
            #sRun()
            time.sleep(1)

         except Exception as e:
            sg.Popup("Error running Saunders program")
            print(e)
            run+=1

         if(run == 0):
            try:
               waitUntilReadCSV(30,crystalA, crystalB, xtraTests,dcSnArray)

            except Exception as e:
               sg.Popup("Error sending data up to the local database")
               print(e)

      else:
         sg.Popup("Error collecting PISN information")

#-----------------------------------------------------------------------------------------------------------------------------------
#GUI

#Create Theme
sg.theme('DarkAmber')

#Create Layout
layout = [[sg.Text("Saunders Data Acquisition")],[sg.Text("Please scan the work order into the text box")],[sg.Text("Work Order #")],
          [sg.InputText(key='workOrder')],[sg.Text("Wheel",key='wheel')],
          [sg.Slider(range=(40, 80),default_value=40,resolution=40, orientation='h', size=(5,10), key="slide")],[sg.Button("setup")],
          [sg.Button("W220 Chamber 2",key='chamber',visible=False)],[sg.Button("EXIT")]]

# Create the window
window = sg.Window("Saunders Data Acquisition", layout,margins=(300,300))

# Create an event loop that dictates the GUI
while True:
   event, values = window.read()

   if event == "setup":
      wO=values['workOrder']
      program = "2200.exe" #Need to change this to the correct program name

      # Check if the program is already running
      running = any(program.lower() == p.name().lower() for p in psutil.process_iter())
      runQ='Yes'
      
      if running:
         runQ=sg.popup_yes_no("There is an instance of W2200 running on this computer,"+
                  " make sure it isn't chamber 2. If it is chamber 2, click No "+
                  "and close the saunders software before restarting",title="Warning")
      if runQ=='Yes':
         try:
            pisnGrabber(wO)
            print(dataframe)
         except Exception as e:
            print(e)
         if isinstance(dataframe, pd.core.generic.NDFrame):
            wheel=values['slide'] 
            correctWheel=sg.popup_yes_no("You've decided on a wheel size of " + str(values['slide']) + ". Is this correct?",title="Wheel Size")
            if(correctWheel=="Yes"):
               sg.Popup("Please press the W220 Chamber 2 to start",title="Start")
               window['chamber'].update(visible=True)
               window['setup'].update(visible=False)
               window['slide'].update(visible=False)
               window['wheel'].update(visible=False)
            elif(correctWheel=="No"):
               sg.Popup("Please Adjust Wheel Size",title="Wheel Size")
            else:
               sg.Popup("PISN Was unable to be found, check with Engineer (Ben preferably)",title="Error")
         else:
            sg.Popup("PISN Was unable to be found, check with Engineer (Ben preferably)2",title="Error")

         
   numOfCrystal=1
   if (event == "chamber"):
      wheel=values['slide']
      rows, cols = (156, 2)
      dcSnArray=np.array([[""]*cols]*rows,dtype='U10')
      start = sg.popup_yes_no("Is this the right amount of Crystals for your work order: "+str(numOfCrystal),  title="Crystal Number")
      if(start=="Yes"):
         if (wheel == 80):
            if (numOfCrystal>156):
               crystalA=78
               crystalB=78
            elif(numOfCrystal>78):
               crystalA=78
               crystalB=numOfCrystal-78
            else:
               crystalA=numOfCrystal
               crystalB=0
         else:
            if (numOfCrystal>78):
               crystalA=39
               crystalB=39
            elif (numOfCrystal>39):
               crystalA=39
               crystalB=numOfCrystal-39
            else:
               crystalA=numOfCrystal
               crystalB=0
         counter=1
         for i in range(crystalA):
            pos="A"+str(counter)
            text = sg.popup_get_text('Scan crystal and put in position '+pos, title=pos)
            if text is None:
               break
            elif dcsnFormat(text): 
               dcSnArray[i][0]=text
               dcSnArray[i][1]=pos
               counter+=1
            else:
               text=None
               sg.Popup('Please make sure you enter the DC_SN correctly', title="error")     
         counter=1
         for i in range(crystalB):
            pos="B"+str(counter)
            text = sg.popup_get_text('Scan crystal and put in position'+pos, title=pos)
            if text is None:
               break
            elif dcsnFormat(text):
               dcSnArray[i+crystalA][0]=text
               dcSnArray[i+crystalA][1]=pos
               counter+=1
            else:
               text=None
               sg.Popup('Please make sure you enter the DC_SN correctly', title="error")
      
         posi=""
         correct="Yes"
         if text is not None:
            correct = sg.popup_yes_no("Do all your positions have the correct DC_SNs?",  title="Corrections")
            
         while(correct=="No"):
            prompt='Which position is wrong? (Example: A1,A2,...)'
            contains=False
            while(contains != True and posi is not None):
               posi=sg.popup_get_text(prompt, title="Incorrect Position")
               contains = np.any(dcSnArray[:,1] == posi)
               prompt="Position does not exist, please enter viable position, or cancel which restarts code"
               if posi is None:
                  break
            if posi is None:
                  break
            counter=0
            size=dcSnArray.shape
            for i in dcSnArray[:,1]:
               if(posi==i):
                  dcSnArray[counter,0]=sg.popup_get_text('Please scan correct DC_SN for '+posi, title="Incorrect Position")
               elif(counter==size):
                  sg.Popup("Could not find position on current wheel, please enter one that exists",title="Error")
               counter+=1
            correct = sg.popup_yes_no("Are all your fixtures now correct with their positions and corresponding DC_SNs?",  title="Corrections")
         
         year = str(datetime.now().strftime('%y'))
         week = str(datetime.now().isocalendar()[1])
         yrWk=year+week

         #Parameters to connect to local database
         server = 'tcp:BTI-PC37\SQLEXPRESS,49170' 
         database = 'AppleCore'
         username = 'ApolloBow1'
         password = '8goodfood!'  

         #Connecting to local database
         connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')
         cursor = connect.cursor()

         cursor.execute("SELECT * " + 
               "FROM DC_SN WITH (TABLOCKX) " +
               "WHERE Crystal_DC_SN LIKE '%" + yrWk + "%' " +
               "OR Saunders_DC_SN LIKE '%" + yrWk + "%' " +
               "OR Osc_DC_SN LIKE '%" + yrWk + "%'")
         sql=cursor.fetchall()
         dfSQL = pd.DataFrame(sql)
         if dfSQL.empty:
            maxVal=yrWk+".00000"
         else:
            checkCol = [col for col in dfSQL.columns if col != 'Unnamed: 2']
            maxVal = 0  
            for col in checkCol:
               for index, value in dfSQL[col].items():
                  for i in value:
                     if str(i) > str(maxVal) and i != None:
                        maxVal = i
         print(maxVal)
         dcSnSplit=str(maxVal).split(".")
         newNum=int(dcSnSplit[1])+1
         dcSnVal=np.array([])
         dcSnCount=0
 
         for row in dcSnArray:
            if row[0] == '' and row[1] == '':
               dcSnVal = np.append(dcSnVal, '')
            else:
               for i in range(4):
                  if len(str(newNum))!=5:
                     newNum="0"+str(newNum)
               newDcSn=dcSnSplit[0]+"."+str(newNum)
               dcSnVal = np.append(dcSnVal, newDcSn)
               newNum=int(newNum) + 1
         dcSnArray = np.append(dcSnArray, dcSnVal[:, np.newaxis], axis=1)
         dNW=0
         #Checks if all DC_SNs exist
         for index,row in enumerate(dcSnArray):
            if row[2] != '':
               cursor.execute("SELECT COUNT(*) FROM DC_SN WHERE Crystal_DC_SN = ? AND Saunders_DC_SN IS NULL", (row[0],))
               row_count = cursor.fetchone()[0]
               if not row_count > 0:
                  dNW+=1
         #If all DC_SNs exist then the newly calculated ones are added to the database
         if dNW != 0:
            sg.Popup("Not all crystal DC_SNs could be found, make sure to input all the DC_SNs correctly or if you did, check with engineer",title="Error")

         cursor.close()
         connect.close() 

         if posi is not None and text is not None and dNW==0:
            try:
               sW22002(crystalA, crystalB, wheel,dcSnArray)
               #Enable mouse and keyboard events
               mouse_listener.stop()
               keyboard_listener.stop()
            except Exception as e:
               sg.Popup("Function isn't working properly check with Engineer (Ben preferably)",title="Error")
               print(e)
               #Enable mouse and keyboard events
               mouse_listener.stop()
               keyboard_listener.stop() 
               time.sleep(1)

      else:
         sg.Popup("Please ensure you have the correct Work Order",title="Halt Program")

    #End program if user closes window or presses the OK button
   if event == "EXIT" or event == sg.WIN_CLOSED:
      break
window.close()
