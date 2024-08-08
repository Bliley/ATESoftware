"""
Author:                                                                          
Benjamin Wolford                                                                
                                                                                 
Description:                                                                    
Program that contains the run class                                      
 
"""
 
#***********************************************************************************
#*Imports                                                                          *
#***********************************************************************************
 
#The imagehash library in Python is a module that provides methods for generating and comparing perceptual hashes of images, enabling
#efficient image similarity detection and identification based on their hash values within Python programs.
import imagehash as ih
#Keyboard is a Python library that enables you to interact with the keyboard inputs on your computer, providing functionality to
#monitor and control keyboard events, simulate keystrokes, and create keyboard-based automation tasks within your Python programs.
import keyboard as kb
#The mouse module in Python is a library that provides functions and classes to track and control mouse events, allowing you to
#simulate mouse clicks, movements, and retrieve mouse-related information within your Python programs.
import mouse as ms
#NumPy is a fundamental Python library for scientific computing and numerical operations, providing powerful multidimensional
#array objects, efficient mathematical functions, and tools for working with large datasets and arrays.
import numpy as np
#The os.path module in Python is a submodule of the os module that provides functions for manipulating paths and working with file and directory
#names in a platform-independent way, allowing for path construction, path validation, file extension extraction, and other path-related operations
#within Python programs.
import os.path
#Pandas is a powerful Python library for data manipulation and analysis, providing flexible data structures and intuitive data handling capabilities
import pandas as pd
#The pdfplumber library in Python is a module that allows extracting text, tables, and other data from PDF files, providing functionalities for parsing
#and extracting information from PDF documents within Python programs, enabling tasks such as text extraction, table extraction, and data analysis from PDF files.
import pdfplumber
#The Image module from the PIL (Python Imaging Library) is a powerful Python library that provides functionality for opening, manipulating, and saving
#various image file formats, allowing for image processing tasks such as resizing, cropping, rotating, applying filters, and other image transformations
#within Python programs.
from PIL import Image
#The pyautogui library in Python is a module that provides cross-platform functions for controlling the mouse and keyboard, enabling automation of GUI
#interactions and tasks such as simulating mouse clicks, moving the cursor, typing keystrokes, taking screenshots, and other GUI-related operations within
#Python programs.
import pyautogui as pg
#PyODBC is a Python library that enables communication between Python programs and ODBC (Open Database Connectivity) databases,
#allowing seamless access and interaction with various database systems.
import pyodbc
#The PyPDF2 library in Python is a module that allows working with PDF files, providing functionalities for reading, manipulating, and writing PDF
#documents within Python programs, enabling tasks such as extracting text, merging or splitting PDFs, adding annotations, and performing various
#operations on PDF files.
import PyPDF2
#The re module in Python is a built-in module that provides regular expression (regex) support, allowing for pattern matching and manipulation of
#text strings within Python programs, enabling tasks such as searching for specific patterns, extracting information, replacing text, and performing
#advanced text processing and manipulation using regular expressions.
import re
#Time is a built-in Python module that provides functions for working with time-related operations, including measuring time intervals,
#obtaining the current time, manipulating dates and times, and converting between different time representations, allowing for time-sensitive
#computations and time management within Python programs.
import time
   
#Parameters to connect to local database
server = 'tcp:BTI-PC37\SQLEXPRESS,49170'  #Current local server being used
database = 'AppleCore'  #Local database being used
username = 'ApolloBow1'  #Username for server
password = '8goodfood!'  #Password for server

#Creates an object that acts as the connector to the local database
connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')

#Using the connector object, the cursor method is used to create a cursor object that allows SQL queries and results to be sent and received
cursor = connect.cursor()

try:
    #Sets up a list with the names and paths of the output files
    file="C:/Users/system8/Desktop/R uns/run(Excel Export Setup File Parameters).xls"

    dataframeP = pd.read_excel(file)  #Sets dataframeP equal to a dataframe read in from the Excel Export Setup File Parameters
    rows,columns = dataframeP.shape  #Grabs the number of rows and columns from dataframeP

    for row_index, rown in dataframeP.iterrows():
        for col_index, cell_value in row.items():
            if "A001" in str(cell_value):
                found_location = (row_index, col_index)
                break 

    for i in range(float(row_index),rows):
        row=''  #Sets row equal to ''
        counter=0  #Sets counter equal to 0
        for j in dataframeP.columns:
            if (counter == 0):
                row+="'"+str(dataframeP[j][i])+"', "  #Concatenates the value found to the row string
                position=str(dataframeP[j][i])  #Sets position equal to the value found
                row+="'"+str(dataframeP['Excel Export Setup File Parameters'][14].replace("Run Start: ",""))+"', "  #Concatenates the time started to row  
                row+="'"+str(dataframeP['Excel Export Setup File Parameters'][16].replace("Run Finish: ",""))+"', "  #Concatenates the time ended to row
            elif (counter >= 4):
                if ((counter % 2)==0 and counter < 28):
                    if (float(dataframeP[j][i])>100000):  #Acts as an upper bound for the SQL Insert
                        row+="'N/A', "  #Concatenates N/A to the row
                    else:
                        value="{:10.4f}".format(float(dataframeP[j][i]))  #Sets value equal to the formatted number from dataframeP
                        row+=str(value.strip())+", "  #Removes leading and trailing spaces from value
            counter+=1  #Increments counter by 1

        #Get the corresponding data from another column
        cursor.execute("SELECT DC_SN FROM SAUNDERS WHERE Position = " + pos + " ORDER BY TimeScanned DESC")
        sDcSn=cursor.fetchone()

        #Sets row equal to the string casted sDcSn concatenated with a comma and the current row string
        row=str(sDcSn)+","+row

        #Cursor gets sent a query that will insert the new row with all values into the XTAL_SETUP_PARAMETERS table
        cursor.execute("INSERT INTO XTAL_SETUP_PARAMETERS ([DC_SN],[Position],[TimeStart],[TimeEnd],[FR_FL],[RR],"+
                    "[C0],[C1],[L],[Q],[SPRR],[LTP],[UTP],[R_T],[PWR],[TEMP]"+xtraTests+") VALUES("+row[:-2]+")")

        #Executes the query on the cursor            
        connect.commit()

    #Moves the Excel Export Setup File Parameters to the 30 day repository folder after concatenating the time that the test finished to the name          
    os.rename("C:/Users/system8/Desktop/R uns/run(Excel Export Setup File Parameters).xls", "C:/Users/system8/Desktop/30 day repo/run(Excel Export Setup File Parameters)" +
            dataframeP['Excel Export Setup File Parameters'][16].replace("Run Finish: ","") + ".xls")

except Exception as e:
    print(e)  #Prints the exception

cursor.close()  #Closes the cursor object
connect.close() #Closes the connection with the database
