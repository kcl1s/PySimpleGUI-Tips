import PySimpleGUI as sg

# https://www.pysimplegui.org/en/latest/#user-settings-api

layout=[[sg.Text('My Beers')]]
layout+=[[sg.Text(i+1),sg.Input(key=('beers',i))] for i in range(8)]
layout+=[[sg.Button('Update'),sg.Exit()]]

window=sg.Window('PSG Tips',layout,finalize=True)   # must finalize before update
#######################
sg.user_settings_filename(path='.')
myBeers=sg.user_settings_get_entry('beer list')
if myBeers != None:
    for x in range(8):
        window[('beers',x)].update(myBeers[x])
#######################
while True:
    event,values= window.read()
    print (values)
    if event == 'Update':
        myBeers=[values[('beers',i)] for i in range(8)]
        print(myBeers)
        pass    
        
    if event in (sg.WIN_CLOSED, 'Exit'):
#######################
        myBeers=[values[('beers',i)] for i in range(8)]
        sg.user_settings_set_entry('beer list',myBeers)
#######################
        break
window.close()