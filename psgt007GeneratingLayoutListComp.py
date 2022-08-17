import PySimpleGUI as sg

# https://www.pysimplegui.org/en/latest/#generated-layouts-for-sure-want-to-read-if-you-have-5-repeating-elementsrows
layout=[[sg.Text('My Beers')]]
layout+=[[sg.Text(i+1),sg.Input(key=('beers',i))] for i in range(8)]
layout+=[[sg.Button('Update'),sg.Exit()]]

window=sg.Window('PSG Tips',layout)

while True:
    event,values= window.read()
    print (values)
    if event == 'Update':
        myBeers=[values[('beers',i)] for i in range(8)]
        print(myBeers)
        pass    
        
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()