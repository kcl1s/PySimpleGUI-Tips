import PySimpleGUI as sg

# https://www.pysimplegui.org/en/latest/#updating-elements-changing-elements-values-in-an-active-window

sampleText='unremarkable sample text'

layout=[[sg.Text('This is some text',key='t')],
        [sg.Input(key='i')],
        [sg.Button('Update Text'),sg.Exit()]]

window=sg.Window('PSG Tips',layout)

while True:
    event,values= window.read()
    print (values)
    if event == 'Update Text':

        window['t'].update(sampleText)
        
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()