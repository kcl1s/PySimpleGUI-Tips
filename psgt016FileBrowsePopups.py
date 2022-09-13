import PySimpleGUI as sg
from pydub import AudioSegment
from glob import glob

# pydub Module - https://github.com/jiaaro/pydub
# ffmpeg install how to - https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
# glob Module - https://docs.python.org/3/library/glob.html
# https://www.pysimplegui.org/en/latest/#popup_get_file use for file browse, multifile browse and file save as
# https://www.pysimplegui.org/en/latest/#popup_get_folder use for folder browse


layout=[[sg.Input(key='folder',enable_events=True),sg.FolderBrowse()],
        [sg.Exit()]]

window=sg.Window('Merge MP3s',layout)

while True:
    event,values= window.read()
    print(event, values)
    if event == 'folder':
        i=0
        book = AudioSegment.empty()
        chapters = [mp3_file for mp3_file in glob(values['folder']+"/*.mp3")]
        for chapter in chapters:
                i+=1
                print (i)
                book+=AudioSegment.from_mp3(chapter)
        saveFile= sg.popup_get_file('Merge Complete! Please Choose a Save Location',save_as=True)
        book.export(saveFile, format='MP3')
        print(book.duration_seconds)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break   
window.close()