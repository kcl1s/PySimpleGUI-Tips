import cv2
import PySimpleGUI as sg

width=640
height=480

sg.theme('DarkBlue5')
Icam= sg.Image(filename='',size=(width,height),pad=0,enable_events= True, k='Icam')
layout= [[Icam],
        [sg.Exit(font=16,size=6)]]
window=sg.Window('cv Cam Demo', layout,grab_anywhere_using_control = True,finalize=True)

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)   #change first arg to get your cam Usually 0,1 or 2
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)

while True:
    event, values = window.read(10)
    ignore,  frame = cam.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    window['Icam'].update(data=cv2.imencode('.ppm', frame)[1].tobytes())
    
cam.release()
window.close()