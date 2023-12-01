import PySimpleGUI as sg

# Folowup to this video https://youtu.be/xZyqYJGjhFs
# https://www.pysimplegui.org/en/latest/call%20reference/#table-element
# To make this useful you need to save the data on exit. See https://youtu.be/BaIKzvZf-qk

td=[]
Headings=['Number','Text String','Combo Choice']

layout=[[sg.Button('Add Row'),sg.Button('Edit Row'),sg.Button('Delete Row'),sg.Exit()],
        [sg.Table(td,Headings,key='myTable')]]

window=sg.Window('PSG Tips',layout)

while True:
    event,values= window.read()
    print (values)
    if event == 'Add Row':
        Nevent, Nvalues  = sg.Window('New Row',  [
                        [sg.Text(Headings[0]),sg.Input(size=5,key=Headings[0])],
                        [sg.Text(Headings[1]),sg.Input(size=20,key=Headings[1])],
                        [sg.Text(Headings[2]),sg.Combo(['Red','Green','Blue'],key=Headings[2])],
                        [sg.Submit(), sg.Cancel()]], background_color= 'pink').read(close=True)
        
        if Nevent == 'Submit':
            td.append([Nvalues[Headings[0]],Nvalues[Headings[1]],Nvalues[Headings[2]]])
            window['myTable'].update(values=td)


    if event == 'Edit Row':
        if values['myTable']==[]:
            sg.popup('No Row Selected')
        else:
            editRow=values['myTable'][0]
            Eevent, Evalues  = sg.Window('Edit Row', [
                        [sg.Text(Headings[0]),sg.Input(td[editRow][0],size=5,key=Headings[0])],
                        [sg.Text(Headings[1]),sg.Input(td[editRow][1],size=20,key=Headings[1])],
                        [sg.Text(Headings[2]),sg.Combo(['Red','Green','Blue'],td[editRow][2],key=Headings[2])],
                        [sg.Submit(), sg.Cancel()]], background_color= '#62c6dd').read(close=True)
            
            if Eevent == 'Submit':
                td[editRow]=[Evalues[Headings[0]],Evalues[Headings[1]],Evalues[Headings[2]]]
                window['myTable'].update(values=td)

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