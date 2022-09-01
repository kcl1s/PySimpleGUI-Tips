import PySimpleGUI as sg

# https://www.pysimplegui.org/en/latest/call%20reference/#table-element
# To make this useful you need to save the data on exit. See https://youtu.be/BaIKzvZf-qk

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
        for i in range(3):    # Loop thru to clear boxes
            window[Headings[i]].update(value='')
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()
