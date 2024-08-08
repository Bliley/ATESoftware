"""
Author:                                                                          
Benjamin Wolford                                                                
                                                                                 
Description:                                                                    
Program that saves the resulting Crystal Data from a Saunders run to the cloud                                   
 
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
#PyODBC is a Python library that enables communication between Python programs and ODBC (Open Database Connectivity) databases,
#allowing seamless access and interaction with various database systems.
import pyodbc

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
    file="C:/Users/system8/Desktop/R uns/run(Excel Export Crystal Data).xls"
    
    dataframeD = pd.read_excel(file)  #Sets dataframeD equal to a dataframe read in from the Excel Export Crystal Data
    rows,columns = dataframeD.shape  #Grabs the number of rows and columns from dataframeD

    for row_index, rown in dataframeD.iterrows():
        for col_index, cell_value in row.items():
            if "A001" in str(cell_value):
                found_location = (row_index, col_index)
                break 

    for i in range(float(row_index),rows):
        row=''  #Sets row equal to ''
        pos=''  #Sets pos equal to ''
        counter=0  #Sets counter equal to 0
        for j in dataframeD.columns:
            if(counter == 0):
                row+="'"+str(dataframeD[j][i])+"', "  #Concatenates the value found to the row string
                pos=str(dataframeD[j][i])
            elif (counter == 2 or counter == 3 or
                counter == 4 or counter == 5 or
                counter == 6 or counter == 7 or
                counter == 11 or counter == 13):
                if (float(dataframeD[j][i])>100000):  #Acts as an upper bound for the SQL Insert
                    row+="'N/A', "  #Concatenates N/A to the row
                else:                                                                                                                                                                              
                    value="{:10.4f}".format(float(dataframeD[j][i]))  #Sets value equal to the formatted number from dataframeD
                    row+=str(value.strip())+", "  #Removes leading and trailing spaces from value
            counter+=1

            row+="'"+str(dataframeD['Excel Export Crystal Data'][16].replace("Run Start: ",""))+"', "  #Concatenates the time started to row
            row+="'"+str(dataframeD['Excel Export Crystal Data'][18].replace("Run Finish: ",""))  #Concatenates the time ended to row

            #Get the corresponding data from another column
            cursor.execute("SELECT DC_SN FROM SAUNDERS WHERE Position = " + pos + " ORDER BY TimeScanned DESC")
            sDcSn=cursor.fetchone()

            #Sets row equal to the string casted sDcSn concatenated with a comma and the current row string
            row=str(sDcSn)+","+row

            #Cursor gets sent a query that will insert the new row with all values into the XTAL_CRYSTAL_DATA table
            cursor.execute("INSERT INTO XTAL_CRYSTAL_DATA ([DC_SN],[Position],[SetTemp],[TrueTemp],"+
                        "[FrequencyPPM],[fCurveFitPPM],[fErrorPPM],[fRr],[RelativeAngle],[strQCStatusCrystal],[TimeStart],[TimeEnd]) VALUES("+row+")")
        
            #Executes the query on the cursor
            connect.commit()

        #Moves the Excel Export Crystal Data to the 30 day repository folder after concatenating the time that the test finished to the name    
        os.rename("C:/Users/system8/Desktop/R uns/run(Excel Export Crystal Data).xls", "C:/Users/system8/Desktop/30 day repo/run(Excel Export Crystal Data)" +
            dataframeD['Excel Export Crystal Data'][18].replace("Run Finish: ","") + ".xls")

except Exception as e:
    print(e)  #Prints the exception

cursor.close()  #Closes the cursor object
connect.close() #Closes the connection with the database
