import PySimpleGUI as sg

# https://www.pysimplegui.org/en/latest/call%20reference/?#pre-defined-buttons-use-in-your-layout
# https://pillow.readthedocs.io/en/stable/reference/Image.html#
# parsing image files with glob module
#   for infile in glob.glob("*.jpg"):
# parsing image files with os module 
#   image_array = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.PNG')]
# File browser elements let you browse the file structure on your machine. 
# These just return the filename(s) as a string. You supply the open or save code.
# -FileBrowse - returns one file path as a str
# -FilesBrowse - returns a multi file path delimited str
# -FolderBrowse - returns a folder path str 
# -FileSaveAs - returns a file path str, warning popup if you choose an existing file

layout=[[sg.Input(size=80,key='fileB',enable_events=True),sg.FileBrowse(button_text='Browse All'),
                    sg.FileBrowse(button_text='Browse Images',target ='fileB',file_types =(('JPG','JPG'),('PNG','PNG')))],
        [sg.Input(size=80,key='filesB',enable_events=True),
                    sg.FilesBrowse(button_text = "Multi Browse",files_delimiter = '\n')],
        [sg.Multiline(size=(80,5),key='ml')],
        [sg.Input(size=80,key='folderB',enable_events=True),sg.FolderBrowse(button_text = "Folder Browse")],
        [sg.Input(size=80,key='fileSaveAs',enable_events=True),sg.FileSaveAs(),sg.Save()],    # Or pseudonym SaveAs()
        [sg.Exit()]]

window=sg.Window('PSGT File Elements',layout)

while True:
    event,values= window.read()
    #print(event, values)
    if event == 'fileB':
        print(values['fileB'])
    if event == 'filesB':
        window['ml'].update(values['filesB'])
        print(values['filesB'])
        fileList=values['filesB'].split('\n')
        print(fileList)
    if event == 'folderB':
        print(values['folderB'])
    if event == 'fileSaveAs':
        print(values['fileSaveAs'])
    if event == 'Save':
        print('Only A Button Press')
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()