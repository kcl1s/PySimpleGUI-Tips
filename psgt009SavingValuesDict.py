import PySimpleGUI as sg

# https://www.pysimplegui.org/en/latest/#user-settings-api
# https://www.pysimplegui.org/en/latest/call%20reference/#window-the-window-object

layout=[[sg.Slider(range=(0,500),k='sl',orientation='horizontal')],
        [sg.Multiline('Type multiline text here',key='mlt', size=(45,5))],
        [sg.LB(['a','b','c'],key='lb',s=(10,3))],
        [sg.Input(key='input')],
        [sg.Combo(['one','two','three'],k='combo'),sg.CB('Test',k='cb'),
            sg.R('first','r1',k='rad1',default=True),sg.R('second','r1',k='rad2')],
        [sg.Button('Update'),sg.Exit()]]

window=sg.Window('PSG Tips',layout,finalize=True)   # must finalize before update

sg.user_settings_filename(path='.')
vDict=sg.user_settings_get_entry('windowDict')
if vDict != None:
    window.fill(vDict)

while True:
    event,values= window.read()
    print (values)
    if event == 'Update':
        sg.user_settings_set_entry('windowDict',values)   
        
    if event in (sg.WIN_CLOSED, 'Exit'):
        sg.user_settings_set_entry('windowDict',values)
        break
window.close()