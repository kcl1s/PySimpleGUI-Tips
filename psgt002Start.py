import PySimpleGUI as sg

# simple demo of persistant window with popup
# https://www.pysimplegui.org/en/latest/cookbook/#getting-started-copy-these-design-patterns

layout=[[sg.Text('Please enter 2 numbers to multiply')],
        [sg.Input(key='firstNum'),sg.Text(' X '),sg.Input(key='secondNum')],
        [sg.Button('Calculate'),sg.Exit()]]

window=sg.Window('PSG Tips',layout)

while True:
    event,values= window.read()
    if event == 'Calculate':
        answer = float(values['firstNum']) * float(values['secondNum'])
        sg.popup('The answer is '+str(answer))
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()