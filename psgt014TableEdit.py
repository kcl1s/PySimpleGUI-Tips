import PySimpleGUI as sg

# Folowup to this video https://youtu.be/xZyqYJGjhFs
# https://www.pysimplegui.org/en/latest/call%20reference/#table-element
# To make this useful you need to save the data on exit. See https://youtu.be/BaIKzvZf-qk

td=[]
Headings=['Number','Text String','Combo Choice']

layout=[[sg.Text(Headings[0]),sg.Input(size=5,key=Headings[0])],
        [sg.Text(Headings[1]),sg.Input(size=20,key=Headings[1])],
        [sg.Text(Headings[2]),sg.Combo(['Red','Green','Blue'],key=Headings[2])],
        [sg.Button('Add Row'),sg.Button('Edit Row'),        # New buttons
            sg.Button('Save Edit',disabled=True),sg.Button('Delete Row'),sg.Exit()],
        [sg.Table(td,Headings,key='myTable')]]

window=sg.Window('PSG Tips',layout)

while True:
    event,values= window.read()
    print (values)
    if event == 'Add Row':
        td.append([values[Headings[0]],values[Headings[1]],values[Headings[2]]])
        window['myTable'].update(values=td)
        for i in range(3):    # Loop thru to clear boxes
            window[Headings[i]].update(value='')
#########################  New code added between bars
    if event == 'Edit Row':
        if values['myTable']==[]:
            sg.popup('No Row Selected')
        else:
            editRow=values['myTable'][0]
            sg.popup('Edit Selected Row')
            for i in range(3):  
                window[Headings[i]].update(value=td[editRow][i])
            window['Save Edit'].update(disabled=False)
    if event == 'Save Edit':
        td[editRow]=[values[Headings[0]],values[Headings[1]],values[Headings[2]]]
        window['myTable'].update(values=td)
        for i in range(3):    # Loop thru to clear boxes
            window[Headings[i]].update(value='')
        window['Save Edit'].update(disabled=True)
    if event == 'Delete Row':
        if values['myTable']==[]:
            sg.popup('No Row Selected')
        else:
            if sg.popup_ok_cancel('Can not undo Delete: Continue?') == 'OK':
                del td[values['myTable'][0]]    # Removes the selected row
                window['myTable'].update(values=td)
#########################
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()