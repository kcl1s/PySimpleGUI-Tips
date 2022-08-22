# demo of updatable combo box
# the combo has to have the focus when you press enter
# This uses the bind_return_key event and can NOT have enable_events=True!!!!!
# Duplicate enties not allowed- Great for dictionary keys
# Might work best as a popup to edit list and make regular combo readonly

# https://www.pysimplegui.org/en/latest/call%20reference/#combo-element
# https://www.pysimplegui.org/en/latest/#user-settings-api

import PySimpleGUI as sg
nam=[]  #['Bob','Sue','Tom']
layout=[[sg.Text('To Add- Type entry and press Enter')],
        [sg.Text('To Remove- Select entry and press Enter   ')],
        [sg.Combo(nam,k='c',bind_return_key=True,s=10)],
        [sg.Exit()]]

window= sg.Window('Edit Combo Choices',layout,finalize=True)

sg.user_settings_filename(path='.')
cList=sg.user_settings_get_entry('combo list')
if cList != None:
    nam=cList
    window['c'].update(values=nam)

while True:
    event, values = window.read()
    if event=='c':
        print (values['c'])
        if values['c'] not in nam:
            nam.append(values['c']) 
            window['c'].update(values=nam,value=values['c'])         
        else:   # Leave this out if you only want to add items
            nam.remove(values['c'])
            window['c'].update(values=nam,value='')
        print (nam)
    if event in (sg.WIN_CLOSED, 'Exit'):
        sg.user_settings_set_entry('combo list',nam)
        break
window.close() 
