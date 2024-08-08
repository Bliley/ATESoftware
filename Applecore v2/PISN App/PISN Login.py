import PySimpleGUI as sg
import pyodbc

def connection():
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

    cursor.execute("SELECT * FROM [Test_Results].[AGING]")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    cursor.close()
    connection.close()


def login_window():
    layout = [
        [sg.Text('Enter your password')],
        [sg.Text('Password:'), sg.InputText(key='-PASSWORD-', size=(20, 1), password_char='*')],
        [sg.Button('Login'), sg.Button('Cancel')]
    ]

    window = sg.Window('Login',layout,return_keyboard_events=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
        
        elif event == 'Login' or event == '\r':
            password = values['-PASSWORD-']
            window.close()
            return password

def main():
    sg.theme('DarkBlack')

    try:
        password = login_window()

        if password == 'jerry':
            layout = [
                [sg.Text('Hello Jerry')],
                [sg.Text('These are the PISNs you have to review')],
                [sg.Text('Please select one and accept or reject it')],
                [sg.Button('OK')]
            ]
            window = sg.Window('Login', layout)
            event, values = window.read()
            window.close()

        elif password == 'dragan':
            values = ['Item 1', 'Item 2', 'Item 3'] 
            layout = [
                [sg.Text('Hello Dragan')],
                [sg.Text('These are the PISNs you have to review')],
                [sg.Text('Please select one and accept or reject it')],
                [sg.Listbox(values, size=(30, 5), key='-LISTBOX-')],
                [sg.Button('Select'),sg.Button('Exit')]
            ]
            window = sg.Window('Login', layout)
            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED or event == 'Exit':
                    window.close()
                    break
        
                elif event == 'Select':
                    selected_item = values['-LISTBOX-'][0] if values['-LISTBOX-'] else None
                    window.close()
                    return password

        elif password == 'mac':
            layout = [
                [sg.Text('Hello Mac')],
                [sg.Text('These are the PISNs you have to review')],
                [sg.Text('Please select one and accept or reject it')],
                [sg.Button('OK')]
            ]
            window = sg.Window('Login', layout)
            event, values = window.read()
            window.close()

        else:
            sg.popup('Invalid credentials')
    except:
        print("Cancelled")
          
main()
connection()
