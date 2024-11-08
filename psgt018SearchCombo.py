
# Code to simulate a searchable combo box. Useful if large list of choices

# Click on a main window 'input' starts a modal popup stlye window
# Each main window (searchable) input require a bind command to create an event when you click
# Popup requires selection from list or Cancel to close
# Popup selection is returned from function and updates the main input box
# Popup window positioned based on mouse location when input on main window is clicked 
# Popup window has no titlebar is modal and has a white background
# Popup list is sorted as well as filtered by startswith based on popup input entry
#
import PySimpleGUI as sg

def scb(title, list, mloc):
    mx,my=mloc
    my=my+12
    SClayout = [[sg.Input(key='-SCB_IN-', enable_events=True)],
        [sg.Listbox(sorted(list), size=(45, 5), key='-SCB_LIST-', enable_events=True)],
        [sg.Cancel(), sg.Button('Add New Choice')]]
    SCwindow = sg.Window(title, SClayout, location= (mx,my), no_titlebar=True, modal=True, 
                         background_color='white', finalize=True)
    SCwindow['-SCB_IN-'].set_focus()
    while True:
        event, values = SCwindow.read()
        if event in [sg.WIN_CLOSED, 'Cancel']:
            break
        if event == '-SCB_IN-':
            search_term = values['-SCB_IN-'].lower()
            filtered_values = [v for v in list if v.lower().startswith(search_term.lower())]
            SCwindow['-SCB_LIST-'].update(sorted(filtered_values))
        if event == '-SCB_LIST-':
            SCwindow.close()
            return values['-SCB_LIST-'][0]
    SCwindow.close()

pl = ['Tom Bush', 'Tim Snow', 'Terri Lynn', 'Sam Smith', 'Sally Jo', 'Sonny Day']
al = ['Payroll Tax', 'Payroll', 'Property Tax', 'Repairs', 'Utilities', 'Phone']
#print(scb())

layout = [[sg.Text('Payee'), sg.Input('', s= 20, key='-PAYEE-', readonly=True),
          sg.Text('Account'), sg.Input('', s= 20, key='-ACC-', readonly=True)]
          ,[sg.Exit()]]

window = sg.Window('Test', layout, use_default_focus = False, finalize=True)
window['-PAYEE-'].bind('<Button-1>', 'f')
window['-ACC-'].bind('<Button-1>', 'f')

while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, 'Exit']:
        break
    if event == '-PAYEE-f':
        tpayee = scb('Payee', pl, window.mouse_location() )
        window['-PAYEE-'].update(tpayee)
    if event == '-ACC-f':
        tacc = scb('account', al, window.mouse_location())
        window['-ACC-'].Update(tacc)

window.close()
          
