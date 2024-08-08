"""
Author: Benjamin Wolford
Servant Class that processes all the data from the PISN and converts it into the keystrokes necessary to run the Saunders software
"""
import keyboard as kb
import pyodbc
import sys
import time
import os.path
import csv
import pandas as pd
import mouse as ms
import pyautogui as pg
import re
import PyPDF2
import pdfplumber
import numpy as np
import imagehash as ih
from PIL import Image

def s250B(mhz: float,resonance: str,loadCap: str,mode: str,val: str,unit: str,ohm: str,calTol: str,tpType: str,tpLTemp: str,tpUTemp: str,resist: str,
          resType: str,c0Min: str,c0Max: str,c1Min: str,c1Max: str,qFactor: str,xtraTests: str,dldPpm: str,dldOhm: str,dldLB: str,
          dldUB: str,dldStep: str,pullHzPpm: str,pullPf: str,spurRat: str,spurious_list: str):
    
    #Shifts to 250B window and opens the ~~.qcc file
    kb.press_and_release("alt+tab")
    time.sleep(2)
    kb.press_and_release("alt+f")
    time.sleep(3)
    kb.press_and_release("o")
    time.sleep(3)
    kb.write("~~.qcc")
    time.sleep(3)
    kb.press_and_release("enter")

    #Setup array for the units
    un=["mW","uW","nW","pW","uA","dBm"]
    md=["calculated","measured","dummy","physical"]

    #Deletes all pre-existing Tests
    for i in range(25):
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(0.6)
        ms.click()
        time.sleep(0.2)
        kb.press_and_release("q")
        for j in range(5):
            kb.press_and_release("shift+tab")
        kb.press_and_release("enter")

#---------------------------------------------------------------------------------------
# Sets up all the referencing values, what is measured over temp, and mode

    #Sets what is being Measured over Temp
    time.sleep(1)
    if(resonance =='Series'):    
        ms.move(1569, 360, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
    else:
        for j in range(6):
            kb.press_and_release("shift+tab")
        time.sleep(1)
        kb.press_and_release("right arrow")
    
    #Reset position of pointer back to Reference Fr
    for j in range(6):
        kb.press_and_release("tab")
    
    #Resonance Frequency
    time.sleep(1)
    kb.press_and_release("backspace")
    hz=mhz*1000000
    shz=str(hz) 
    kb.write(shz)
        
    #Mode Changing
    kb.press_and_release("tab")
    time.sleep(1)
    for i in range(20):
        kb.press_and_release("delete")
    kb.write("letsGo:)")
    kb.press_and_release("tab")
    kb.press_and_release("up arrow, up arrow, up arrow")
    num=md.index(mode.lower())
    for i in range(num):
        kb.press_and_release("down arrow")
    time.sleep(1)

    #Reference CL
    if(resonance =='Series'):
        time.sleep(0.1)
    else:
        kb.press_and_release("tab")
        time.sleep(0.5)
        try:
            load=loadCap.split("pf")
            kb.write(load[0])
        except Exception as e:
            print(e) 
        
        
  #Power Applied
    #Value
    kb.press_and_release("tab")
    time.sleep(0.5)
    kb.press_and_release("backspace")
    kb.write(val)
    #Accounts for potential mismatch between value and unit of power applied
    kb.press_and_release("enter")
    time.sleep(0.5)
    kb.press_and_release("enter")
        
    #Type of Power
    kb.press_and_release("tab")
    for i in range(8): 
        kb.press_and_release("up arrow")
        kb.press_and_release("esc")
    num=un.index(unit)
    #Accounts for potential mismatch between value and unit of power applied
    for i in range(num):
        kb.press_and_release("down arrow")
        time.sleep(0.5)
        kb.press_and_release("esc")
        time.sleep(0.5)
    
    #Into How Many Ohms
    kb.press_and_release("tab")
    time.sleep(0.5)
    kb.write(ohm)
    
#---------------------------------------------------------------------------------------
# Sets up the tests that need to be run for the setup file

    #Opens new Measurement Test Window and making either FR or FL
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(2)
    ms.click()
    time.sleep(1)
    if(resonance =='Series'):
        for i in range(12): 
            kb.press_and_release("f")
        kb.press_and_release("tab,tab")
        kb.press_and_release("p")
        kb.press_and_release("tab")
        kb.press_and_release("plus")
        for i in range(6):
            kb.press_and_release("tab")
        kb.press_and_release("up arrow")
        kb.press_and_release("tab")
        
    else:
        for i in range(10): 
            kb.press_and_release("f")
        kb.press_and_release("tab,tab")
        kb.press_and_release("p")
        kb.press_and_release("tab")
        kb.press_and_release("plus")
        kb.press_and_release("tab")
        kb.write("-"+calTol) 
        kb.press_and_release("tab") 
        kb.write(calTol) 
        for i in range(4):
            kb.press_and_release("tab")
        kb.press_and_release("up arrow")
        kb.press_and_release("tab,tab")
        kb.press_and_release("up arrow")
        kb.press_and_release("tab")

            
    for i in range(12): 
        kb.press_and_release("up arrow")
    if mhz > 20:
        kb.press_and_release("tab")
        kb.write("10")
        kb.press_and_release("tab")
        kb.press_and_release("enter")
    else:
        kb.press_and_release("h")
        kb.press_and_release("tab")
        kb.write("-50")
        kb.press_and_release("tab")
        kb.write("50")
        kb.press_and_release("tab")
        kb.write("0.5")
        kb.press_and_release("tab")
        kb.write("0.3")
        kb.press_and_release("tab")
        kb.write("200")
        kb.press_and_release("tab")
        kb.press_and_release("enter")

    #Adding TEMP
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    for i in range(4):
        kb.press_and_release("t")
    for i in range(3): 
        kb.press_and_release("tab")
    kb.press_and_release("plus")
    for i in range(6): 
        kb.press_and_release("shift+tab")
    kb.press_and_release("enter")
    time.sleep(0.1)

    #Adding PWR
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    kb.press_and_release("p")
    kb.press_and_release("tab,tab")
    kb.press_and_release("u")
    kb.press_and_release("tab")
    kb.press_and_release("plus")
    for i in range(6): 
        kb.press_and_release("shift+tab")
    kb.press_and_release("enter")
    time.sleep(0.1)

    
    #Adding R/T
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    for i in range(11): 
        kb.press_and_release("r")
    for i in range(3): 
        kb.press_and_release("tab")
    kb.press_and_release("plus")
    if ("max" in resType):
        kb.press_and_release("tab,tab")
        kb.write(resist)
    elif("min" in resType):
        kb.press_and_release("tab")
        kb.write(resist)
        kb.press_and_release("tab")
    for i in range(4): 
        kb.press_and_release("tab")
    kb.press_and_release("up arrow")
    for i in range(4): 
        kb.press_and_release("tab")
    kb.press_and_release("enter")
    time.sleep(0.1)

    #Adding UTP
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    for i in range(6): 
        kb.press_and_release("t")
    for i in range(3): 
        kb.press_and_release("tab")
    kb.press_and_release("plus")
    kb.press_and_release("tab")
    if("UTP" in tpType): 
        kb.write(tpLTemp)
        kb.press_and_release("tab")
        kb.write(tpUTemp)
    else:
       kb.press_and_release("tab") 
    for i in range(7): 
        kb.press_and_release("tab")
    kb.press_and_release("enter")
    time.sleep(0.1)

    #Adding LTP
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    for i in range(5): 
        kb.press_and_release("t")
    for i in range(3): 
        kb.press_and_release("tab")
    kb.press_and_release("plus")
    kb.press_and_release("tab")
    if("LTP" in tpType): 
        kb.write(tpLTemp)
        kb.press_and_release("tab")
        kb.write(tpUTemp)
    else:
       kb.press_and_release("tab") 
    for i in range(7): 
        kb.press_and_release("tab")
    kb.press_and_release("enter")
    time.sleep(0.1)


    #Adding SPRR
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    for i in range(6): 
        kb.press_and_release("s")
    for i in range(3): 
        kb.press_and_release("tab")
    kb.press_and_release("plus")
    for i in range(6):
        kb.press_and_release("tab")
    for i in range(3):
        kb.press_and_release("down arrow")
    for i in range(7):
        kb.press_and_release("tab")
    kb.press_and_release("enter")
    time.sleep(0.5)
    kb.press_and_release("tab,tab,tab")
    for i in range(8): 
        kb.press_and_release("up arrow")
    for i in range(num):
        kb.press_and_release("down arrow")
    kb.press_and_release("shift+tab")
    time.sleep(0.5)
    kb.write(val)
    kb.press_and_release("tab,tab")
    time.sleep(0.5)
    kb.write(ohm)
    kb.press_and_release("tab,tab")
    time.sleep(0.5)
    kb.press_and_release("h")
    kb.press_and_release("shift+tab")
    time.sleep(0.5)
    lHz=str(hz-50000)
    kb.write(lHz) 
    kb.press_and_release("tab,tab")
    time.sleep(0.5)
    uHz=str(hz+50000)
    kb.write(uHz) 
    for i in range(5):                    
        kb.press_and_release("tab")
    kb.press_and_release("enter")
    time.sleep(0.1)
    for i in range(3): 
        kb.press_and_release("shift+tab")
    kb.press_and_release("enter")

    #Adding Q
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    kb.press_and_release("q")
    for i in range(3): 
        kb.press_and_release("tab")
    kb.press_and_release("plus")
    kb.press_and_release("tab")
    print(qFactor)
    kb.write(qFactor)
    time.sleep(0.1)
    for i in range(8): 
        kb.press_and_release("tab")
    kb.press_and_release("enter")
    time.sleep(0.1)


    #Adding L
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    kb.press_and_release("l")
    kb.press_and_release("tab,tab")
    kb.press_and_release("m")
    kb.press_and_release("tab")
    kb.press_and_release("plus")
    for i in range(6): 
        kb.press_and_release("shift+tab")
    kb.press_and_release("enter")
    time.sleep(0.1)

    #Adding C1
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    kb.press_and_release("c")
    kb.press_and_release("d")
    for i in range(5): 
        kb.press_and_release("c")
    for i in range(3): 
        kb.press_and_release("tab")
    kb.press_and_release("plus")
    if ("fF" in c1Min and "pF" in c1Max):
        kb.press_and_release("tab")
        kb.write(c1Min.replace("fF",""))
        kb.press_and_release("tab")
        kb.write(c1Max.replace("fF",""))
    elif ("fF" in c1Min):
        kb.press_and_release("tab")
        kb.write(c1Min.replace("fF",""))
        kb.press_and_release("tab")
    elif ("fF" in c1Max):
        kb.press_and_release("tab,tab")
        kb.write(c1Max.replace("fF",""))
    else:
        kb.press_and_release("tab,tab")
    for i in range(8): 
        kb.press_and_release("shift+tab")
    kb.press_and_release("enter")
    time.sleep(0.1)

    #Adding C0
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    kb.press_and_release("c")
    kb.press_and_release("d")
    kb.press_and_release("c")
    for i in range(3): 
        kb.press_and_release("tab")
    kb.press_and_release("plus")
    if ("pF" in c0Min and "pF" in c0Max):
        kb.press_and_release("tab")
        kb.write(c0Min.replace("pF",""))
        kb.press_and_release("tab")
        kb.write(c0Max.replace("pF",""))
    elif ("pF" in c1Min):
        kb.press_and_release("tab")
        kb.write(c0Min.replace("pF",""))
        kb.press_and_release("tab")
    elif ("pF" in c1Max):
        kb.press_and_release("tab,tab")
        kb.write(c0Max.replace("pF",""))
    else:
        kb.press_and_release("tab,tab")
    for i in range(8): 
        kb.press_and_release("shift+tab")
    kb.press_and_release("enter")
    time.sleep(0.1)

    #Adding RR
    ms.move(1227, 436, absolute=True, duration=0.2)
    time.sleep(1)
    ms.click()
    time.sleep(1)
    for i in range(8): 
        kb.press_and_release("r")
    for i in range(3): 
        kb.press_and_release("tab")
    kb.press_and_release("plus")
    if ("max" in resType):
        kb.press_and_release("tab,tab")
        kb.write(resist)
    elif("min" in resType):
        kb.press_and_release("tab")
        kb.write(resist)
        kb.press_and_release("tab")
    for i in range(7): 
        kb.press_and_release("tab")
    kb.press_and_release("enter")
    time.sleep(0.1)

#---------------------------------------------------------------------------------------
# Sets up the tests that may or may not need to be run

    #Gets which tests will be run
    test=xtraTests.split(",")

    #Adding DLTF
    if "DLTF" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        kb.press_and_release("d")
        for i in range(3): 
            kb.press_and_release("tab")
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("tab")
        kb.press_and_release("up arrow")
        for i in range(4): 
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        time.sleep(0.1)
                             
    #Adding DFL
    if "DFL" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        pull=pullHzPpm.split(" ")
        pFs=pullPf.split("pF")
        for i in range(5):
            kb.press_and_release("d")
        kb.press_and_release("tab,tab")
        if ("ppm" in pull[1]):
            kb.press_and_release("p")
        else:
            kb.press_and_release("h")
        kb.press_and_release("tab")
        kb.press_and_release("plus")
        kb.press_and_release("tab")
        kb.write(pull[0])
        for i in range(5): 
            kb.press_and_release("tab")
        kb.press_and_release("down arrow")
        kb.press_and_release("tab")
        kb.write(pFs[0].replace(",",""))
        for i in range(8):
            kb.press_and_release("tab")                         
        kb.press_and_release("down arrow")
        for i in range(7):
            kb.press_and_release("shift+tab")
        kb.write(pFs[2].replace(",","")) 
        kb.press_and_release("tab,tab,tab,tab")
        kb.press_and_release("enter")
        time.sleep(0.1)
                             
    #Adding DLD2
    if "DLD2" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        for i in range(7):
            kb.press_and_release("d")
        for i in range(3): 
            kb.press_and_release("tab")
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        time.sleep(0.1)
        for i in range(4):
            kb.press_and_release("tab")                         
        kb.press_and_release("up arrow")
        kb.press_and_release("tab,tab")
        for i in range(5):
            kb.press_and_release("enter")
        for i in range(5):
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        time.sleep(0.1)
        dldL=dldLB.split(" ")
        kb.write(dldL[0])
        kb.press_and_release("tab")
        num=un.index(dldL[1])
        for i in range(5):
            kb.press_and_release("up arrow")                         
        for i in range(num):
            kb.press_and_release("down arrow")
        kb.press_and_release("tab")
        dldU=dldUB.split(" ")
        kb.write(dldU[0])
        kb.press_and_release("tab")
        num=un.index(dldU[1])
        for i in range(5):
            kb.press_and_release("up arrow")                         
        for i in range(num):
            kb.press_and_release("down arrow")                         
        kb.press_and_release("tab")                         
        kb.write(dldStep)
        kb.press_and_release("tab")
        kb.press_and_release("enter")
        for i in range(5):
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        for i in range(4):
            kb.press_and_release("tab")
        kb.press_and_release("enter")                          
                             
    #Adding DLD9
    if "DLD9" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        for i in range(7):
            kb.press_and_release("d")
        for i in range(3): 
            kb.press_and_release("tab")
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        time.sleep(0.1)
        for i in range(4):
            kb.press_and_release("tab")                         
        kb.press_and_release("up arrow")
        kb.press_and_release("tab,tab")
        for i in range(5):
            kb.press_and_release("enter")
        for i in range(5):
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        time.sleep(0.1)
        dldL=dldLB.split(" ")
        kb.write(dldL[0])
        kb.press_and_release("tab")
        num=un.index(dldL[1])
        for i in range(5):
            kb.press_and_release("up arrow")                         
        for i in range(num):
            kb.press_and_release("down arrow")
        kb.press_and_release("tab")
        dldU=dldUB.split(" ")
        kb.write(dldU[0])
        kb.press_and_release("tab")
        num=un.index(dldU[1])
        for i in range(5):
            kb.press_and_release("up arrow")                         
        for i in range(num):
            kb.press_and_release("down arrow")                         
        kb.press_and_release("tab")                         
        kb.write(dldStep)
        kb.press_and_release("tab")
        kb.press_and_release("enter")
        for i in range(5):
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        for i in range(4):
            kb.press_and_release("tab")
        kb.press_and_release("enter")                         
                                
    #Adding FDLD
    if "FDLD" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        if(resonance =='Series'): 
            for i in range(14):
                kb.press_and_release("f")
        else:
            for i in range(16):
                kb.press_and_release("f")
        kb.press_and_release("tab,tab")
        kb.press_and_release("p")
        kb.press_and_release("tab")                         
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        time.sleep(0.1)
        for i in range(4):
            kb.press_and_release("tab")                         
        kb.press_and_release("up arrow")
        kb.press_and_release("tab,tab")
        for i in range(5):
            kb.press_and_release("enter")
        for i in range(5):
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        time.sleep(0.1)
        dldL=dldLB.split(" ")                         
        kb.write(dldL[0])
        kb.press_and_release("tab")
        num=un.index(dldL[1])
        for i in range(5):
            kb.press_and_release("up arrow")                         
        for i in range(num):
            kb.press_and_release("down arrow")
        kb.press_and_release("tab")
        dldU=dldUB.split(" ")
        kb.write(dldU[0])
        kb.press_and_release("tab")
        num=un.index(dldU[1])
        for i in range(5):
            kb.press_and_release("up arrow")                         
        for i in range(num):
            kb.press_and_release("down arrow")                         
        kb.press_and_release("tab")                         
        kb.write(dldStep)
        kb.press_and_release("tab")
        kb.press_and_release("enter")
        for i in range(5):
            kb.press_and_release("tab")
        kb.press_and_release("enter")
        for i in range(4):
            kb.press_and_release("tab")
        kb.press_and_release("enter")
                                
    #Adding SP50
    if "SP50" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        kb.press_and_release("s")
        for i in range(3): 
            kb.press_and_release("tab")
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("tab")
        for i in range(4):
            kb.press_and_release("down arrow")
        for i in range(4): 
            kb.press_and_release("tab")     
        kb.press_and_release("enter")
        time.sleep(0.1)
                                
    #Adding SPUR
    if "SPUR" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        for i in range(7):
            kb.press_and_release("s")
        for i in range(3): 
            kb.press_and_release("tab")
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("tab")
        for i in range(4):
            kb.press_and_release("down arrow")
        for i in range(4): 
            kb.press_and_release("tab")     
        kb.press_and_release("enter")
        time.sleep(0.1)               
                             
    #Adding TS
    if "TS" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        for i in range(3):
            kb.press_and_release("t")
        for i in range(3): 
            kb.press_and_release("tab")
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("shift+tab")
        kb.press_and_release("enter")
        time.sleep(0.1)
                                
    #Adding WCD
    if "WCD" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        kb.press_and_release("w") 
        kb.press_and_release("tab,tab")
        kb.press_and_release("p")                         
        kb.press_and_release("tab")                         
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("tab")
        kb.press_and_release("up arrow")
        for i in range(4): 
            kb.press_and_release("tab")                         
        kb.press_and_release("enter")
        time.sleep(0.1)
                             
    #Adding FTPD
    if "FTPD" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1)
        if(resonance =='Series'): 
            for i in range(11):
                kb.press_and_release("f")
        else:
            for i in range(13):
                kb.press_and_release("f")
        kb.press_and_release("tab,tab")
        kb.press_and_release("p") 
        kb.press_and_release("tab")                         
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("shift+tab")                         
        kb.press_and_release("enter")
        time.sleep(0.1)
    
    #Adding SSDB NEED TO DO!!!!!!!!!!!!!!!!!
    if "SSDB" in test:
        ms.move(1227, 436, absolute=True, duration=0.2)
        time.sleep(1)
        ms.click()
        time.sleep(1) 
        for i in range(9):
            kb.press_and_release("s")
        kb.press_and_release("tab,tab,tab")                        
        kb.press_and_release("plus")
        for i in range(6): 
            kb.press_and_release("shift+tab")                         
        kb.press_and_release("enter")
        time.sleep(0.1)

    
#Creates the Setup Files that get added to the Configuration Menu so the Saunders Machine knows what parameters it must abide by
#crystalA-The number of positions that are in row A
#crystalB-The number of positions that are in row B
#wheel-The type of physical wheel that the crystals will be placed on (40 or 80)
#mhz-The nominal frequency of the crystal in Mega Hz
#RLC-The load capacity of the crystal
#val-The number value of the power supplied
#unit-The unit of the power suppled (val)
#ohm-The number of ohms that the power is supplied into
def configure(crystalA: int, crystalB: int, wheel: int):
    #Shifts back to W-2200 Chamber to ensure window
    kb.press_and_release("alt+tab")
    time.sleep(1)
    #Edit Configuration
    kb.press_and_release("alt+e,o")
    time.sleep(0.5)

    #Sets up wheel
    kb.press_and_release("alt+o")
    time.sleep(0.5)
    kb.press_and_release("tab,tab")
    if wheel == 80:
        for i in range(12):
            kb.press_and_release("up arrow")
        for i in range(12):
            time.sleep(0.5)
            image = pg.screenshot(region=(1327, 448,32, 18))
            image.save("C:\\Users\\system8\\Desktop\\Wheel Pics\\check.png")
            time.sleep(0.5)
            cHash = ih.average_hash(Image.open("C:\\Users\\system8\\Desktop\\Wheel Pics\\check.png"))
            wHash = ih.average_hash(Image.open("C:\\Users\\system8\\Desktop\\Wheel Pics\\80.png"))
            if((cHash-wHash)==0):
                break
            else:
                kb.press_and_release("down arrow")
    else:
        time.sleep(0.5)
        kb.press_and_release("4")
        time.sleep(0.1)
    for i in range(6):
        kb.press_and_release("tab")
    kb.press_and_release("enter")
    time.sleep(1)

    #Delete any prexisting configurations
    for i in range(4):
        kb.press_and_release("tab")
    kb.press_and_release("up arrow")
    kb.press_and_release("tab,tab,tab")
    for i in range(5):
        kb.press_and_release("enter")

    #Get pointer to setup files
    kb.press_and_release("tab,tab,tab,tab")
    time.sleep(0.5)
    kb.write("~")
    time.sleep(0.5)

#---------------------------------------------------------------------------------------
# Crystal A, 40 wheel    

    if(wheel == 40):
    #Open add config
        kb.press_and_release("alt+a")
        time.sleep(0.5)

    #Add Positions to wheel
        kb.press_and_release("up arrow")
        kb.press_and_release("tab")
        for i in range(38):
            kb.press_and_release("up arrow")
        kb.press_and_release("tab")
        kb.press_and_release("up arrow")
        kb.press_and_release("tab")
        for i in range(38):
            kb.press_and_release("down arrow")
        for i in range(39-crystalA):
            kb.press_and_release("up arrow")

    #Starting Serial Number
        kb.press_and_release("tab")
        kb.press_and_release("1")
    #Clicking out of setup
        kb.press_and_release("tab")
        kb.press_and_release("enter")

#---------------------------------------------------------------------------------------
# Crystal B, 40 wheel (relies on if from Crystal A)
        if (crystalB != 0):    
        #Open add config   
            kb.press_and_release("alt+a")
            time.sleep(0.5)

        #Add Positions to wheel 
            kb.press_and_release("down arrow")
            kb.press_and_release("tab")
            for i in range(38):
                kb.press_and_release("up arrow")
            kb.press_and_release("tab")
            kb.press_and_release("down arrow")
            kb.press_and_release("tab")
            for i in range(38):
                kb.press_and_release("down arrow")
            for i in range(39-crystalB):
                kb.press_and_release("up arrow")

        #Starting Serial Number
            kb.press_and_release("tab")
            kb.press_and_release("1")

        #Clicking out of setup
            kb.press_and_release("tab")
            kb.press_and_release("enter")

#---------------------------------------------------------------------------------------
# Crystal A, 80 wheel 

    elif(wheel == 80):
    #Open add config   
        kb.press_and_release("alt+a")
        time.sleep(0.5)

    #Add Positions to wheel
        kb.press_and_release("up arrow")
        kb.press_and_release("tab")
        for i in range(77):
            kb.press_and_release("up arrow")
        kb.press_and_release("tab")
        kb.press_and_release("up arrow")
        kb.press_and_release("tab")
        for i in range(77):
            kb.press_and_release("down arrow")
        for i in range(78-crystalA):
            kb.press_and_release("up arrow")

    #Starting Serial Number
        kb.press_and_release("tab")
        kb.press_and_release("1")

    #Clicking out of setup
        kb.press_and_release("tab")
        kb.press_and_release("enter")


#---------------------------------------------------------------------------------------
# Crystal B, 80 wheel (relies on if from Crystal A)
        if (crystalB != 0):
        #Open add config   
            kb.press_and_release("alt+a")
            time.sleep(0.5)
        #Add Positions to wheel
            kb.press_and_release("down arrow")
            kb.press_and_release("tab")
            for i in range(77):
                kb.press_and_release("up arrow")
            kb.press_and_release("tab")
            kb.press_and_release("down arrow")
            kb.press_and_release("tab")
            for i in range(77):
                kb.press_and_release("down arrow")
            for i in range(78-crystalB):
                kb.press_and_release("up arrow")

        #Starting Serial Number
            kb.press_and_release("tab")
            kb.press_and_release("1")

        #Clicking out of setup
            kb.press_and_release("tab")
            kb.press_and_release("enter")

#---------------------------------------------------------------------------------------
# If Crystal is not 40 or 80, send error            
    else:
        print("ERROR")
    #Exit out of Configuration Setup
    kb.press_and_release("enter")
    time.sleep(0.5)
    kb.press_and_release("enter")


#Creates the steps that the Saunders machine must take in terms of temperature
#bTemp-The bottom temperature that the saunders machine begins at
#uTemp-The upper temperature that the saunders machine ends at
#step-The increment that the machine should take each time it changes temperature 
def temp(caliTemp: str,lTemp: str, uTemp: str, step: str):
    #Edit Temperature Table
    kb.press_and_release("alt+e,t")
    time.sleep(0.5)
#----------------------------------------------------------------------------   
    #Open Set Temperature
    kb.press_and_release("tab,tab,tab,tab")
    kb.press_and_release("up arrow")
    kb.press_and_release("tab,tab")
    kb.press_and_release("enter,enter,enter,enter,enter")
    kb.press_and_release("tab,tab,tab") 
    kb.press_and_release("up arrow")
    kb.press_and_release("alt+a")
    time.sleep(1)

    #Set Lower Temperature
    kb.press_and_release("ctrl+a")
    kb.write(caliTemp)

    #soak time in mins
    kb.press_and_release("tab,tab")
    kb.write("10")

    #Measure Type
    kb.press_and_release("tab")
    kb.press_and_release("down arrow, down arrow, down arrow")
    kb.press_and_release("up arrow")

    #Exit out of Set
    kb.press_and_release("tab")
    kb.press_and_release("enter")

#----------------------------------------------------------------------------

    #Set Lower Temperature
    kb.press_and_release("ctrl+a")
    kb.write(lTemp)
    
    #soak time in mins
    kb.press_and_release("tab,tab")
    kb.write("10")

    #Measure Type
    kb.press_and_release("tab")
    kb.press_and_release("up arrow, up arrow, up arrow")

    #Exit out of Set
    kb.press_and_release("tab")
    kb.press_and_release("enter")

#---------------------------------------------------------------------------- 

    #Open Step temperature
    kb.press_and_release("alt+a")
    time.sleep(1)

    #Set Upper Temperature
    kb.press_and_release("shift+tab")
    kb.press_and_release("down arrow")
    kb.press_and_release("tab")
    kb.write(uTemp)

    #Set Step
    kb.press_and_release("tab")
    kb.write(step)

    #Soak Time
    kb.press_and_release("tab,tab")
    kb.press_and_release("3")

    #Measure Type
    kb.press_and_release("tab")
    kb.press_and_release("up arrow, up arrow, up arrow")

    #Exit out of Set
    kb.press_and_release("tab")
    kb.press_and_release("enter")

#---------------------------------------------------------------------------- 

    #Open Set Temperature
    kb.press_and_release("up arrow")
    kb.press_and_release("alt+a")
    time.sleep(1)

    #Soak Time
    kb.press_and_release("tab,tab")
    kb.press_and_release("1")

    #Measure Type
    kb.press_and_release("tab")
    kb.press_and_release("down arrow, down arrow, down arrow")

    #Exit out of set
    kb.press_and_release("tab")
    kb.press_and_release("enter")

#Exit out of Temperature Table
    kb.press_and_release("tab,tab")
    kb.press_and_release("enter")


#Sets up how the data in the Saunders machine will be printed out 
def sPrint():
    #Edit Printout Selection
    kb.press_and_release("alt+e,p")
    time.sleep(0.5)

    #Delete the existing reports from selections
    kb.press_and_release("tab,tab,tab,tab")
    kb.press_and_release("up arrow")
    kb.press_and_release("tab,tab")
    kb.press_and_release("enter,enter,enter,enter,enter")

    #Get to the Reports Section
    kb.press_and_release("tab,tab,tab,tab")
    kb.press_and_release("up arrow")
#----------------------------------------------------------------------------
#All Printouts setup 
    for u in range(2):

    #Get to the bottom of Reports
        for i in range(12):
            kb.press_and_release("down arrow")
        time.sleep(0.5)

    #Go up the necessary amount to get to the report type
        for i in range(u):    
            kb.press_and_release("up arrow")
        kb.press_and_release("alt+a")
        time.sleep(0.5)

    #Operates differently depending on report type
        kb.press_and_release("tab,tab,tab,tab,tab,tab")
        kb.press_and_release("down arrow,down arrow,down arrow")

    #Gets to Print or Export Option
        kb.press_and_release("tab,tab,tab,tab")
        kb.press_and_release("down arrow")

    #Get to excel file type
        kb.press_and_release("tab")
        kb.press_and_release("e")
        time.sleep(0.5)

    #Sets up files to be output to correct folder
        kb.press_and_release("tab")
        kb.press_and_release("enter")
        time.sleep(5)
        kb.press_and_release("alt+tab")
        time.sleep(0.5)
        kb.press_and_release("alt+tab")
        time.sleep(0.5)
        kb.press_and_release("r+u")
        time.sleep(5)
        kb.press_and_release("enter")
        time.sleep(0.5)

    #Add all positions to output
        kb.press_and_release("tab")
        kb.press_and_release("plus")
        time.sleep(0.5)

    #Export File With FileType
        for i in range(7):
            kb.press_and_release("tab")
        kb.press_and_release("down")
        kb.press_and_release("tab")
        kb.press_and_release("enter")
    kb.press_and_release("enter")
    

#Runs the Program 
def sRun():
    kb.press_and_release("alt+r")
    kb.press_and_release("enter")
    time.sleep(2)
    kb.press_and_release("delete")
    kb.press_and_release("r+u+n")
    kb.press_and_release("enter")
    kb.press_and_release("left arrow")
    kb.press_and_release("enter")
    time.sleep(3)
    #If the run is adjusted at all, it needs to re-save the run file
    #Should not affect run if it is the exact same as previous one
    kb.press_and_release("tab,tab")
    kb.press_and_release("b+c+w")
    kb.press_and_release("tab,tab,tab,tab,tab")
    kb.press_and_release("enter")
    
#Waits until the the necessary files exist in the specified location is over to do anything
#period-The amount of time between when the function checks if the file exists
def waitUntilReadCSV(period: int, crystalA: int, crystalB: int, xtraTests: str,dcSnArray):
  files=fileExist()
  while files==False:
    if fileExist():
        readCSV(crystalA, crystalB, xtraTests,dcSnArray)
        files=True
    time.sleep(period)

#Identifies when the program outputs the csv files to the path
def fileExist():
    if (os.path.isfile("C:/Users/system8/Desktop/R uns/run(Excel Export Setup File Parameters).xls") and 
        os.path.isfile("C:/Users/system8/Desktop/R uns/run(Excel Export Crystal Data).xls")):
        return True 
    return False

def readCSV(crystalA: int, crystalB: int, xtraTests: str,dcSnArray):
    #Parameters to connect to local database
    server = 'tcp:BTI-PC37\SQLEXPRESS,49170' 
    database = 'AppleCore'
    username = 'ApolloBow1'
    password = '8goodfood!'  

    #Connecting to local database
    connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')
    cursor = connect.cursor()
    try:
        files=["C:/Users/system8/Desktop/R uns/run(Excel Export Setup File Parameters).xls",
               "C:/Users/system8/Desktop/R uns/run(Excel Export Crystal Data).xls",
               "C:/Users/bwolford/Desktop/30 day repo/run.pdf"]
        dataframeP = pd.read_excel(files[0])
        topPA=crystalA+22
        bottomPB=topPA+3
        topPB=bottomPB+crystalB
        for i in range(dcSnArray.shape[0]):
            # Get the string from the 0th column
            ogS = dcSnArray[i, 0]
            
            # Insert two zeroes between the characters
            moS = ''
            for j in range(len(ogS)):
                moS += ogS[j]
                if j < len(ogS) - 1:
                    moS += '00'
            
            # Update the value in the 0th column
            dcSnArray[i, 0] = moS

        for i in range(bottomPB,topPB):
            row=""
            counter=0
            for j in dataframeP.columns:
                if (counter == 0):
                    row+="'"+str(dataframeP[j][i])+"', "
                    position=str(dataframeP[j][i])
                    row+="'"+str(dataframeP['Excel Export Setup File Parameters'][14].replace("Run Start: ",""))+"', "
                    row+="'"+str(dataframeP['Excel Export Setup File Parameters'][16].replace("Run Finish: ",""))+"', "
                elif (counter >= 4):
                    if ((counter % 2)==0 and counter < 28):
                        if (float(dataframeP[j][i])>100000):
                            row+="'N/A', "
                        else:
                            value="{:10.4f}".format(float(dataframeP[j][i]))
                            row+=str(value.strip())+", "
                counter+=1

            # Find the indices where the target value is present in the search column
            index = np.where(dcSnArray[:, 0] == position)[0]

            # Get the corresponding data from another column
            sDcSn= dcSnArray[index, 1]

            row=str(sDcSn)+","+row

            cursor.execute("INSERT INTO XTAL_SETUP_PARAMETERS ([DC_SN],[Position],[TimeStart],[TimeEnd],[FR_FL],[RR],"+
                           "[C0],[C1],[L],[Q],[SPRR],[LTP],[UTP],[R_T],[PWR],[TEMP]"+xtraTests+") VALUES("+row[:-2]+")")
            connect.commit()
            
        for index,row in enumerate(dcSnArray):
               if row[2] != '':
                  cursor.execute("SELECT COUNT(*) FROM DC_SN WHERE Crystal_DC_SN = ?", (row[0],))
                  row_count = cursor.fetchone()[0]

                  # If the condition value exists, update another column with the predetermined value
                  if row_count > 0:
                     cursor.execute("UPDATE DC_SN SET Saunders_DC_SN = ? WHERE Crystal_DC_SN = ?", (row[2], row[0]))
                     connect.commit()
            
        dataframeD = pd.read_excel(files[1])
        rows,columns = dataframeD.shape
        for i in range(24,rows):
            row=""
            counter=0
            for j in dataframeD.columns:
                if(counter == 0):
                    row+="'"+str(dataframeD[j][i])+"', "
                elif (counter == 2 or counter == 3 or
                      counter == 4 or counter == 5 or
                      counter == 6 or counter == 7 or 
                      counter == 11 or counter == 13):
                    if (float(dataframeD[j][i])>100000):
                        row+="'N/A', "
                    else:                                                                                                                                                                               
                        value="{:10.4f}".format(float(dataframeD[j][i]))
                        row+=str(value.strip())+", "
                counter+=1

            row+="'"+str(dataframeD['Excel Export Crystal Data'][16].replace("Run Start: ",""))+"', "
            row+="'"+str(dataframeD['Excel Export Crystal Data'][18].replace("Run Finish: ",""))

            # Find the indices where the target value is present in the search column
            index = np.where(dcSnArray[:, 0] == position)[0]

            # Get the corresponding data from another column
            sDcSn= dcSnArray[index, 1]

            row=str(sDcSn)+","+row

            cursor.execute("INSERT INTO XTAL_CRYSTAL_DATA ([DC_SN],[Position],[SetTemp],[TrueTemp],"+
                           "[FrequencyPPM],[fCurveFitPPM],[fErrorPPM],[fRr],[RelativeAngle],[strQCStatusCrystal],[TimeStart],[TimeEnd]) VALUES("+row+")")
            connect.commit()

        read=PyPDF2.PdfReader(open(files[2],'rb'))
        pArray =  np.array([])
        dataframeC = pd.DataFrame(pArray)
        xyList=[[25,130,220,200],[25,195,125,300],[125,195,220,300],
                [215,130,405,200],[215,195,315,300],[315,195,405,300],
                [400,130,600,200],[400,195,500,300],[500,195,600,300],
                [25,300,220,352],[25,352,125,460],[125,352,220,460],
                [215,300,405,352],[215,352,315,460],[315,352,405,460],
                [400,300,600,352],[400,352,500,460],[500,352,600,460],
                [25,460,220,505],[25,505,125,650],[125,505,220,650],
                [215,460,405,505],[215,505,315,650],[315,505,405,650],
                [400,460,600,505],[400,505,500,650],[500,505,600,650],]
        for i in range(len(read.pages)):
            size=9 #Need to change to whatever is gotten from the 
            for j in range(size*3):
                # Open the cropped PDF file
                with pdfplumber.open(files[2]) as pdf:
                    # Access the first page
                    page = pdf.pages[i]
                    # Define the coordinates of the rectangular region to extract
                    x1 = xyList[j][0]  
                    y1 = xyList[j][1] 

                    x2 = xyList[j][2]   
                    y2 = xyList[j][3]  

                    # Extract the text from the specified region
                    region_text = page.within_bbox((x1, y1, x2, y2)).extract_text()

                    # Print the extracted text
                    if (j%3 == 0):
                        posData=re.split("\n|: | R|< <",region_text)
                        posData[6]="Relative Angle"
                        posDataTitle=posData[0::2]
                        posDataVal=posData[1::2]
                    else:
                        posData=re.split("\n|: ",region_text)
                        posDataTitle=posData[::2]
                        posDataVal=posData[1::2]
                    pArray=np.column_stack((posDataTitle,posDataVal))
                    dataframeC=pd.concat([dataframeC, pd.DataFrame(pArray.tolist())], ignore_index=True)

        rows,columns = dataframeC.shape
        pos=9*len(read.pages)
        for i in range(pos):
            row=""
            for j in range(20):
                if(j==0):
                   row+="'"+str(dataframeC[0][i*20])+"', "
                elif(j==3):
                    row+="'"+str(dataframeC[1][(i*20)+j].replace("'",""))+"', "
                elif (j>1 and j!=3):                                                                                                                                                                        
                    row+="'"+str(dataframeC[1][(i*20)+j])+"', "
                    if(j==19):
                        times = page.within_bbox((400, 90, 600, 130)).extract_text()
                        times = re.split("\n",times)
                        row+="'"+str(times[0].replace("Run Start: ",""))+"', "
                        row+="'"+str(times[1].replace("Run Finish: ",""))+"'"

            # Find the indices where the target value is present in the search column
            index = np.where(dcSnArray[:, 0] == position)[0]

            # Get the corresponding data from another column
            sDcSn= dcSnArray[index, 1]

            row=str(sDcSn)+","+row

            cursor.execute("INSERT INTO XTAL_CURVEFIT ([DC_SN],[Position],[Cut],[RelativeAngle],"+
                               "[ReferenceFrequency],[A0],[A1],[A2],[A3],[A4],[WCD],[WCT],[TP1],[TP2],"+
                               "[TP3],[InflT1],[InflT2],[MaxR],[MinR],[DeltaR],[TimeStart],[TimeMeasured]) VALUES("+row+")")
            connect.commit()

            cursor.close()
            connect.close() 
        os.rename("C:/Users/system8/Desktop/R uns/run(Crystal Curvefit Summary).xls", "C:/Users/system8/Desktop/30 day repo/run(Crystal Curvefit Summary)" +
                  times[1].replace("Run Finish: ","") + ".xls")  
        os.rename("C:/Users/system8/Desktop/R uns/run(Excel Export Setup File Parameters).xls", "C:/Users/system8/Desktop/30 day repo/run(Excel Export Setup File Parameters)" +
                  dataframeP['Excel Export Setup File Parameters'][16].replace("Run Finish: ","") + ".xls")    
        os.rename("C:/Users/system8/Desktop/R uns/run(Excel Export Crystal Data).xls", "C:/Users/system8/Desktop/30 day repo/run(Excel Export Crystal Data)" +
                  dataframeD['Excel Export Crystal Data'][18].replace("Run Finish: ","") + ".xls")
    except Exception as e:
        print(e)
