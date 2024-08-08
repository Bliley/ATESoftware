import PySimpleGUI as sg

def submit(values):
    # Add your submission logic here
    print("Submitted:", values)

def window_creation():
    sg.theme('DarkBlack')

    tab1 = [
        [sg.Column([
            [sg.Text('Crystal Part/Blank Data', font=('Helvetica', 16), justification='left')],
            [sg.Text('Bliley Part Number:',size=(15, 1)), sg.InputText(key='bliley_part_number',size=(20,1))],
            [sg.Text('Revision Level:',size=(15, 1)), sg.InputText(key='revision_level',size=(20, 1))],
            [sg.Text('Latest ECN#',size=(15, 1)), sg.InputText(key='latest_ecn',size=(20, 1))],
            [sg.Text('Frequency:',size=(15, 1)), sg.InputText(key='frequency',size=(20, 1))],
            [sg.Text('Overtone:',size=(15, 1)), sg.InputText(key='overtone',size=(20, 1))],
            [sg.Text('Customer Part #',size=(15, 1)), sg.InputText(key='customer_part_number',size=(20, 1))],
            [sg.Text('Package Type:',size=(15, 1)), sg.InputText(key='package_type',size=(20, 1))],
            [sg.Text('To be used on:',size=(15, 1)), sg.InputText(key='to_be_used_on',size=(20, 1))],
        ], element_justification='left'),
        sg.Column([
            [sg.Text('Blank Part #:',size=(15, 1)), sg.InputText(key='blank_part_number',size=(20, 1))],
            [sg.Text('Cut/Quartz Type:',size=(15, 1)), sg.InputText(key='cut_quartz_type',size=(20, 1))],
            [sg.Text('Blank Diameter:',size=(15, 1)), sg.InputText(key='blank_diameter',size=(20, 1))],
            [sg.Text('Blank Thickness:',size=(15, 1)), sg.InputText(key='blank_thickness',size=(20, 1))],
            [sg.Text('Blank Final Freq:',size=(15, 1)), sg.InputText(key='blank_final_freq',size=(20, 1))],
            [sg.Text('Freq for Sorting:',size=(15, 1)), sg.InputText(key='freq_for_sorting',size=(20, 1))],
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
            [sg.Text('Baseplate Amount:',size=(15, 1)), sg.InputText(key='baseplate_amount',size=(20, 1))],
            [sg.Text('Mount & Cement:',size=(15, 1)), sg.InputText(key='mount_cement',size=(20, 1))],
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
            [sg.Text('Calibration:',size=(15, 1)), sg.InputText(key='calibration',size=(20, 1))],
            [sg.Text('Calibration Method:',size=(15, 1)), sg.InputText(key='calibration_method',size=(20, 1))],
            [sg.Text('Plater and Temperature:',size=(15, 1)), sg.InputText(key='plater_temperature',size=(20, 1))],
            [sg.Text('Target and Tolerance:',size=(15, 1)), sg.InputText(key='target_tolerance',size=(20, 1))],
            [sg.Text('Crystal Cap:',size=(15, 1)), sg.InputText(key='crystal_cap',size=(20, 1))],
            [sg.Text('Seal per:',size=(15, 1)), sg.InputText(key='seal_per',size=(20, 1))],
        ], element_justification='left',pad=((0, 0), (7,0)))],
    ]

    tab3 = [
        [sg.Column([
            [sg.Text('Crystal Test Specs', font=('Helvetica', 16), justification='left')],
            [sg.Text('Frequency/OT/Cut:',size=(15, 1)), sg.InputText(key='baseplate',size=(20, 1))],
            [sg.Text('Resonance:',size=(15, 1)), sg.InputText(key='setup_file',size=(20, 1))],
            [sg.Text('Load Capacity :',size=(15, 1)), sg.InputText(key='baseplate_mask',size=(20, 1))],
            [sg.Text('Mode :',size=(15, 1)), sg.InputText(key='chrome',size=(20, 1))],
            [sg.Text('Drive Level:',size=(15, 1)), sg.InputText(key='electrode_metal',size=(20, 1))],
            [sg.Text('Drive Level Into [Ohms]:',size=(15, 1)), sg.InputText(key='baseplate_amount',size=(20, 1))],
            [sg.Text('Operating Temp Range:',size=(15, 1)), sg.InputText(key='mount_cement',size=(20, 1))],
            [sg.Text('Calibration Tolerance:',size=(15, 1)), sg.InputText(key='crystal_holder',size=(20, 1))],
            [sg.Text('Calibration Temp:',size=(15, 1)), sg.InputText(key='cut_off_leads',size=(20, 1))],
            [sg.Text('Temperature Stability Tolerance:',size=(15, 1)), sg.InputText(key='mounting_orientation',size=(20, 1))],
            [sg.Text('Temperature Stability Range:',size=(15, 1)), sg.InputText(key='cement_type',size=(20, 1))],
        ], element_justification='left'),
        sg.Column([
            [sg.Text('TP Type:',size=(15, 1)), sg.InputText(key='bake_profile',size=(20, 1))],
            [sg.Text('TP Range:',size=(15, 1)), sg.InputText(key='vacuum_bake',size=(20, 1))],
            [sg.Text('Resistance R [Ω]:',size=(15, 1)), sg.InputText(key='visual_inspection',size=(20, 1))],
            [sg.Text('Resistance R Type:',size=(15, 1)), sg.InputText(key='overdrive',size=(20, 1))],
            [sg.Text('Shunt Capacitance C0 [pF] Min:',size=(15, 1)), sg.InputText(key='calibration',size=(20, 1))],
            [sg.Text('Shunt Capacitance C0 [pF] Nom:',size=(15, 1)), sg.InputText(key='calibration_method',size=(20, 1))],
            [sg.Text('Shunt Capacitance C0 [pF] Max:',size=(15, 1)), sg.InputText(key='plater_temperature',size=(20, 1))],
            [sg.Text('Motional Capacitance C1 [pF] Min:',size=(15, 1)), sg.InputText(key='calibration',size=(20, 1))],
            [sg.Text('Motional Capacitance C1 [pF] Nom:',size=(15, 1)), sg.InputText(key='calibration_method',size=(20, 1))],
            [sg.Text('Motional Capacitance C1 [pF] Max:',size=(15, 1)), sg.InputText(key='plater_temperature',size=(20, 1))],
            [sg.Text('Quality Factor Q [k]:',size=(15, 1)), sg.InputText(key='target_tolerance',size=(20, 1))],
            [sg.Text('FvT Test Range:',size=(15, 1)), sg.InputText(key='crystal_cap',size=(20, 1))],
            [sg.Text('FvT Test Step Size:',size=(15, 1)), sg.InputText(key='seal_per',size=(20, 1))],
            [sg.Text('Xmission Drift:',size=(15, 1)), sg.InputText(key='seal_per',size=(20, 1))],
        ], element_justification='left',pad=((0, 0), (7,0)))],
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
