import PySimpleGUI as sg
import pyodbc

def submit(values):
    x=[]
    y=[]
    dc_snList=[]
    try:
        server = 'tcp:BTI-PC37\\SQLEXPRESS,49170' 
        database = 'AppleCore'
        username = 'ApolloBow1'
        password = '8goodfood!'  

        connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes')
        cursor = connect.cursor()
    except Exception as e:
        print(f"Error: {str(e)}")

def window_creation():
    sg.theme('DarkBlack')

    tab1 = [
        [sg.Column([
            [sg.Text('Crystal Part/Blank Data', font=('Helvetica', 16), justification='left')],
            [sg.Text('Bliley Part Number:',size=(15, 1)), sg.InputText(key='bliley_part_number',size=(20,1))],
            [sg.Text('Customer Part #',size=(15, 1)), sg.InputText(key='customer_part_number',size=(20, 1))],
            [sg.Text('Revision:',size=(15, 1)), sg.InputText(key='revision',size=(20, 1))],
            [sg.Text('Current Rev. Level:',size=(15, 1)), sg.InputText(key='curr_rev_lev',size=(20, 1))],
            [sg.Text('Latest ECN#',size=(15, 1)), sg.InputText(key='latest_ecn',size=(20, 1))],
            [sg.Text('Frequency:',size=(15, 1)), sg.InputText(key='frequency',size=(20, 1))],
            [sg.Text('Overtone:',size=(15, 1)), sg.InputText(key='overtone',size=(20, 1))],
            [sg.Text('Package Type:',size=(15, 1)), sg.InputText(key='package_type',size=(20, 1))],
        ], element_justification='left'),
        sg.Column([
            [sg.Text('Blank Part #:',size=(15, 1)), sg.InputText(key='blank_part_number',size=(20, 1))],
            [sg.Text('Cut Type:',size=(15, 1)), sg.InputText(key='cut_type',size=(20, 1))],
            [sg.Text('Quartz Type:',size=(15, 1)), sg.InputText(key='quartz_type',size=(20, 1))],
            [sg.Text('Blank Diameter:',size=(15, 1)), sg.InputText(key='blank_diameter',size=(20, 1))],
            [sg.Text('Blank Thickness:',size=(15, 1)), sg.InputText(key='blank_thickness',size=(20, 1))],
            [sg.Text('Blank Final Freq:',size=(15, 1)), sg.InputText(key='blank_final_freq',size=(20, 1))],
            [sg.Text('Baseplate Groups:',size=(15, 1)), sg.InputText(key='base_grp',size=(20, 1)),sg.Text('kHz',size=(15, 1))],
        ], element_justification='left',pad=((0, 0), (0,17)))],
    ]

    tab2 = [
        [sg.Column([
            [sg.Text('Manufacturing Requirements', font=('Helvetica', 16), justification='left')],
            [sg.Text('Baseplate:',size=(15, 1)), sg.InputText(key='baseplate',size=(20, 1))],
            [sg.Text('Setup File:',size=(15, 1)), sg.InputText(key='setup_file',size=(20, 1))],
            [sg.Text('Baseplate Mask:',size=(15, 1)), sg.InputText(key='baseplate_mask',size=(20, 1))],
            [sg.Text('Chrome:',size=(15, 1)), sg.InputText(key='chrome',size=(20, 1))],
            [sg.Text('Electrode Metal:',size=(15, 1)), sg.InputText(key='electrode_metal',size=(20, 1))],
            [sg.Text('Crystal Holder:',size=(15, 1)), sg.InputText(key='crystal_holder',size=(20, 1))],
            [sg.Text('Cut Off Leads:',size=(15, 1)), sg.InputText(key='cut_off_leads',size=(20, 1))],
            [sg.Text('Mounting Orientation:',size=(15, 1)), sg.InputText(key='mounting_orientation',size=(20, 1))],
            [sg.Text('Cement Type:',size=(15, 1)), sg.InputText(key='cement_type',size=(20, 1))],
        ], element_justification='left'),
        sg.Column([
            [sg.Text('Bake Profile:',size=(15, 1)), sg.InputText(key='bake_profile',size=(20, 1))],
            [sg.Text('Vacuum Bake:',size=(15, 1)), sg.InputText(key='vacuum_bake',size=(20, 1))],
            [sg.Text('Visual Inspection:',size=(15, 1)), sg.InputText(key='visual_inspection',size=(20, 1))],
            [sg.Text('Overdrive:',size=(15, 1)), sg.InputText(key='overdrive',size=(20, 1))],
            [sg.Text('Plater and Temperature:',size=(15, 1)), sg.InputText(key='plater_temperature',size=(20, 1))],
            [sg.Text('Target and Tolerance:',size=(15, 1)), sg.InputText(key='target_tolerance',size=(20, 1))],
            [sg.Text('Crystal Cap:',size=(15, 1)), sg.InputText(key='crystal_cap',size=(20, 1))],
            [sg.Text('Seal per:',size=(15, 1)), sg.InputText(key='seal_per',size=(20, 1))],
        ], element_justification='left',pad=((0, 0), (7,0)))],
    ]

    tab3 = [
        [sg.Column([
            [sg.Text('Crystal Test Specs', font=('Helvetica', 16), justification='left')],
            [sg.Text('Frequency/OT/Cut:', size=(15, 1)), sg.InputText(key='frequency_ot_cut', size=(20, 1))],
            [sg.Text('Resonance:', size=(15, 1)), sg.InputText(key='resonance', size=(20, 1))],
            [sg.Text('Load Capacity:', size=(15, 1)), sg.InputText(key='load_capacity', size=(20, 1))],
            [sg.Text('Mode:', size=(15, 1)), sg.InputText(key='mode', size=(20, 1))],
            [sg.Text('Drive Level:', size=(15, 1)), sg.InputText(key='drive_level', size=(20, 1))],
            [sg.Text('Drive Level Into [Ohms]:', size=(15, 1)), sg.InputText(key='drive_level_ohms', size=(20, 1))],
            [sg.Text('Operating Temp Range:', size=(15, 1)), sg.InputText(key='operating_temp_range', size=(20, 1))],
            [sg.Text('Calibration Tolerance:', size=(15, 1)), sg.InputText(key='calibration_tolerance', size=(20, 1))],
            [sg.Text('Calibration Temp:', size=(15, 1)), sg.InputText(key='calibration_temp', size=(20, 1))],
            [sg.Text('Temperature Stability Tolerance:', size=(15, 1)),
             sg.InputText(key='temperature_stability_tolerance', size=(20, 1))],
            [sg.Text('Temperature Stability Range:', size=(15, 1)),
             sg.InputText(key='temperature_stability_range', size=(20, 1))],
        ], element_justification='left'),
         sg.Column([
             [sg.Text('TP Type:', size=(15, 1)), sg.InputText(key='tp_type', size=(20, 1))],
             [sg.Text('TP Range:', size=(15, 1)), sg.InputText(key='tp_range', size=(20, 1))],
             [sg.Text('Resistance R [Ω]:', size=(15, 1)), sg.InputText(key='resistance_ohms', size=(20, 1))],
             [sg.Text('Resistance R Type:', size=(15, 1)), sg.InputText(key='resistance_type', size=(20, 1))],
             [sg.Text('C0 [pF] Min:', size=(15, 1)),sg.InputText(key='c0_min', size=(20, 1))],
             [sg.Text('C0 [pF] Max:', size=(15, 1)),sg.InputText(key='c0_max', size=(20, 1))],
             [sg.Text('C1 [fF] Min:', size=(15, 1)),sg.InputText(key='c1_min', size=(20, 1))],
             [sg.Text('C1 [fF] Max:', size=(15, 1)),sg.InputText(key='c1_max', size=(20, 1))],
             [sg.Text('Quality Factor Q [k]:', size=(15, 1)), sg.InputText(key='quality_factor', size=(20, 1))],
             [sg.Text('FvT Test Range:', size=(15, 1)), sg.InputText(key='fvt_test_range', size=(20, 1))],
             [sg.Text('FvT Test Step Size:', size=(15, 1)), sg.InputText(key='fvt_test_step_size', size=(20, 1))],
         ], element_justification='left', pad=((0, 0), (7, 0)))],
    ]


    # Create a layout for the window with tabs
    layout = [
        [sg.TabGroup([
            [sg.Tab('Crystal Part/Blank Data', tab1)],
            [sg.Tab('Manufacturing Requirements', tab2)],
            [sg.Tab('Crystal Test Specs', tab3)],
        ])],
        [sg.Button('Submit', pad=((250, 0),(0,0))), sg.Button('Exit', pad=((10, 0),(0,0)))],
    ]

    window = sg.Window('PISN Creation', layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Submit':
            submit(values)

    window.close()

window_creation()
