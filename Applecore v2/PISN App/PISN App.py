import PySimpleGUI as sg
import subprocess
import pyodbc

def main():
    server = "tcp:blileysql.database.windows.net"
    database = "applecore"
    user = "bwolford@bliley.com"
    password = "PbL@$3Bx"
    driver = "{ODBC Driver 18 for SQL Server}"

    connection_string = (
        'Driver={ODBC Driver 18 for SQL Server};'
        'Server=tcp:blileysql.database.windows.net,1433;'
        'Database=applecore;'
        'Uid=bwolford@bliley.com;'
        'Pwd=PbL@$3Bx;'
        'Encrypt=yes;'
        'TrustServerCertificate=no;'
        'Connection Timeout=30;'
        'Authentication=ActiveDirectoryPassword'
    )
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    
    sg.theme('DarkBlack')
    
    layout = [
    [sg.Text('', size=(10, 2)),sg.Text('PISN App', font=('Helvetica', 20), justification='center')],
    [sg.Text('', size=(11, 2)),sg.Frame('New PISN', layout=[
        [sg.Button('Create', size=(6, 1), font=('Helvetica', 14))]
    ], title_location='n')],
    [sg.Frame('Review Existing PISNs', layout=[
        [sg.Text('Enter Password', font=('Helvetica', 16), justification='center')],
        [sg.InputText(key='-INPUT-', password_char='*', size=(20, 1), font=('Helvetica', 14)), sg.Button('Enter', font=('Helvetica', 14))]
    ], title_location='n')],
]
    
    window = sg.Window('PISN App', layout,return_keyboard_events=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        elif event == 'Create':
            try:
                window.Hide()
                process = subprocess.Popen(['python', 'C:/Users/BWolford/Desktop/PISN App/PISN Creation.py'], shell=True)
                process.wait()
                window.UnHide()

            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
                print("Return code:", e.returncode)
                
        elif event == 'Enter' or event == '\r':
            password = values['-INPUT-']
            try:
                window.Hide()
                if password == 'jerry':
                    layout2 = [
                        [sg.Text('Hello Jerry')],
                        [sg.Text('These are the PISNs you have to review')],
                        [sg.Text('Please select one and accept or reject it')],
                        [sg.Button('OK')]
                    ]
                    window2 = sg.Window('Login', layout2)
                    event, values = window2.read()
                    window2.close()

                elif password == 'dragan':
                    values = ['Item 1', 'Item 2', 'Item 3'] 
                    layout3 = [
                        [sg.Text('Hello Dragan')],
                        [sg.Text('These are the PISNs you have to review')],
                        [sg.Text('Please select one and accept or reject it')],
                        [sg.Listbox(values, size=(30, 5), key='-LISTBOX-')],
                        [sg.Button('Select'),sg.Button('Exit')]
                    ]
                    window3 = sg.Window('Login', layout3)
                    while True:
                        event, values = window3.read()

                        if event == sg.WIN_CLOSED or event == 'Exit':
                            window3.close()
                            break
                
                        elif event == 'Select':
                            selected_item = values['-LISTBOX-'][0] if values['-LISTBOX-'] else None
                            window3.close()
                            return password

                elif password == 'mac':
                    layout4 = [
                        [sg.Text('Hello Mac')],
                        [sg.Text('These are the PISNs you have to review')],
                        [sg.Text('Please select one and accept or reject it')],
                        [sg.Button('OK')]
                    ]
                    window4 = sg.Window('Login', layout4)
                    event, values = window4.read()
                    window4.close()

                else:
                    sg.popup('Invalid credentials')
                    
                window.UnHide()    
            except:
                print("Cancelled")

    window.close()

main()
