import PySimpleGUI as sg

# https://www.pysimplegui.org/en/latest/cookbook/#keys

a=5
layout=[[sg.Text('testing Keys')],
        [sg.Input(key='-in-')],
        [sg.Input(key=('reading',a))],
        [sg.Exit()]]

window=sg.Window('PSG Tips',layout)

while True:
    event,values= window.read()
    print (values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()