import PySimpleGUI as sg

# https://www.pysimplegui.org/en/latest/#column-element-frame-tab-container-elements

sg.theme('DarkRed1')

beerCol=[[sg.Input(size=30)]for i in range(10)]
amenitiesFrame=[[sg.Checkbox('Bar Seating'),sg.Spin([i for i in range(1,50)]),sg.Text('Seats')],
                [sg.Checkbox('Table Seating'),sg.Spin([i for i in range(1,50)]),sg.Text('Seats')],
                [sg.Text('Food')],
                [sg.Radio('None','f')],
                [sg.Radio('On Site','f')],
                [sg.Radio('Food Truck','f')],
                [sg.Radio('Food Truck Sometimes','f')],
                [sg.Text('Overall Impression'),sg.Combo(['Good','Average','Poor'])]]

tab1Layout=[[sg.Text('Brewery Name'),sg.Input(size=40)],            
        [sg.Text('Location Address'),sg.Multiline('',size=(25,2))],
        [sg.Text('Date of Visit'),sg.Input(size=20),sg.CalendarButton('Calendar',format = "%B %d, %Y")],
        [sg.Column(beerCol),sg.Frame('Amenities',amenitiesFrame)]]
        

tab2Layout=[[sg.Image(r'C:/Users/lohme\Documents/Python/tall-tales-outdoor-bar.png',subsample=2)]]

Layout=[[sg.TabGroup([[sg.Tab('Details',tab1Layout),sg.Tab('Photo',tab2Layout)]])],
        [sg.Exit()]]

window = sg.Window('Micro Brewery Reviews', Layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.Close()