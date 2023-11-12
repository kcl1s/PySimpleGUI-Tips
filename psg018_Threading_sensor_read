import PySimpleGUI as sg
import threading
import time

def read_sensor():
    ct = 0  
    while True:
        ct = ct + 1     # or put sensor read code here
        window.write_event_value('sensor_read',str(ct))
        time.sleep(1)

layout=[[sg.Text(key='reading',enable_events=True,font=('Arial', 32))],
        [sg.Exit()]]

window=sg.Window('Sensor Display',layout)

threading.Thread(target=read_sensor, args=(), daemon=True).start()

while True:
    event,values= window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'sensor_read':
        window['reading'].update(values['sensor_read'])
