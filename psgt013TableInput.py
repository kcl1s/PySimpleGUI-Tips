import PySimpleGUI as sg

td=[]
Headings=['Number','Text String','Combo Choice']

layout=[[sg.Text(Headings[0]),sg.Input(size=5,key=Headings[0])],
        [sg.Text(Headings[1]),sg.Input(size=20,key=Headings[1])],
        [sg.Text(Headings[2]),sg.Combo(['Red','Green','Blue'],key=Headings[2])],
        [sg.Button('Add Table Row'),sg.Exit()],
        [sg.Table(td,Headings,key='myTable')]]

window=sg.Window('PSG Tips',layout)

while True:
    event,values= window.read()
    print (values)
    if event == 'Add Table Row':
        td.append([values[Headings[0]],values[Headings[1]],values[Headings[2]]])
        window['myTable'].update(values=td)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()