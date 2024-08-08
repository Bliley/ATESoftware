"""
Author:                                                                          
Benjamin Wolford                                                                
                                                                                 
Description:                                                                    
Program that saves the resulting Curvefit Summary from a Saunders run to the cloud                                         
 
"""
 
#***********************************************************************************
#*Imports                                                                          *
#***********************************************************************************
 
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
    file= "C:/Users/bwolford/Desktop/R uns/run(Crystal CurveFit Summary).pdf"
    
        read=PyPDF2.PdfReader(open(file,'rb'))  #Creates a PdfReader object of the PyPDF2 library from the Crystal Curvefit Summary  
        pArray =  np.array([])  #Creates an empty numpy array
        dataframeC = pd.DataFrame(pArray) #Builds an empty pandas dataframe from the empty array

        #Creates a list with the xy boundaries for the 3 rectangle snips that will be taken for each position in the Crystal Curvefit Summary
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
            if(i == (len(read.pages)-1)):
                size = pdf.pages[i]
            else:
                size=9

            for j in range(size*3):
                #Open the cropped PDF file
                with pdfplumber.open(file) as pdf:
                    #Access the first page
                    page = pdf.pages[i]

                    #Define the coordinates of the rectangular region to extract
                    x1 = xyList[j][0]  #X coordinate of the upper left corner of the region
                    y1 = xyList[j][1]  #Y coordinate of the upper left corner of the region

                    x2 = xyList[j][2]  #X coordinate of the lower right corner of the region
                    y2 = xyList[j][3]  #Y coordinate of the lower right corner of the region

                    #Extract the text from the specified region
                    region_text = page.within_bbox((x1, y1, x2, y2)).extract_text()

                    #Print the extracted text
                    if (j%3 == 0):
                        posData=re.split("\n|: | R|< <",region_text)  #Splits the data at various strings
                        posData[6]="Relative Angle"  #Fixes the title by readding the R back
                        posDataTitle=posData[0::2]  #Sets posDataTitle equal to every other element in posData starting at 0
                        posDataVal=posData[1::2]  #Sets posDataVal equal to every other element in posData starting at 1
                    else:
                        posData=re.split("\n|: ",region_text)  #Splits the data at various strings
                        posDataTitle=posData[::2]  #Sets posDataTitle equal to every other element in posData starting at 0
                        posDataVal=posData[1::2]  #Sets posDataVal equal to every other element in posData starting at 1
                    pArray=np.column_stack((posDataTitle,posDataVal))  #Adds posDataTitle and posDataVal to pArray as two new columns
                    #Converts pArray to a list and then a pandas dataframe which is concatenated to the empty dataframeC
                    dataframeC=pd.concat([dataframeC, pd.DataFrame(pArray.tolist())], ignore_index=True)  

        pos=9*len(read.pages)  #Calculates the number of positions to be read on each page
        for j in range(pos):
            row=""  #Sets row equal to an empty string
            for j in range(20):
                if(j==0):
                    row+="'"+str(dataframeC[0][i*20])+"', "  #Concatenates in the Crystal Position on the wheel
                elif(j==3):
                    row+="'"+str(dataframeC[1][(i*20)+j].replace("'",""))+"', "  #Concatenates the Relative Angle to row
                elif (j>1 and j!=3):                                                                                                                                                                        
                    if(j!=19):
                        row+="'"+str(dataframeC[1][(i*20)+j])+"', "  #Adds all the data recorded from the crystal run
                    else:
                        times = page.within_bbox((400, 90, 600, 130)).extract_text()  #Cuts out another region from the pdf with the time start and finish
                        times = re.split("\n",times)  #Splits the region into a list with two values
                        row+="'"+str(times[0].replace("Run Start: ",""))+"', "  #Concatenates the time started to row
                        row+="'"+str(times[1].replace("Run Finish: ",""))+"'"  #Concatenates the time ended to row

            #Get the corresponding data from another column
            cursor.execute("SELECT DC_SN FROM SAUNDERS WHERE Position = " + pos + " ORDER BY TimeScanned DESC")
            sDcSn = cursor.fetchone()

            #Sets row equal to the string casted sDcSn concatenated with a comma and the current row string
            row=str(sDcSn)+","+row

            #Cursor gets sent a query that will insert the new row with all values into the XTAL_CURVEFIT table
            cursor.execute("INSERT INTO XTAL_CURVEFIT ([DC_SN],[Position],[Cut],[RelativeAngle],"+
                            "[ReferenceFrequency],[A0],[A1],[A2],[A3],[A4],[WCD],[WCT],[TP1],[TP2],"+
                            "[TP3],[InflT1],[InflT2],[MaxR],[MinR],[DeltaR],[TimeStart],[TimeMeasured]) VALUES("+row+")")
        
            #Executes the query on the cursor
            connect.commit()
    
    #Moves the Crystal Curvefit Summary to the 30 day repository folder after concatenating the time that the test finished to the name
    os.rename("C:/Users/system8/Desktop/R uns/run(Crystal Curvefit Summary).xls", "C:/Users/system8/Desktop/30 day repo/run(Crystal Curvefit Summary)" +
            times[1].replace("Run Finish: ","") + ".xls")


except Exception as e:
    print(e)  #Prints the exception

cursor.close()  #Closes the cursor object
connect.close() #Closes the connection with the database
