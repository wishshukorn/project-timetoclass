import PySimpleGUI as sg

#sg.theme('DarkAmber')   # Add a touch of color

options = ['Option a','Option b','Option c']

# All the stuff inside your window.
layout = [ 
            [sg.Text('Select one->'), sg.Listbox(options,select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,size=(20,len(options)))],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

# Create the Window
window = sg.Window('Make your choice', layout)

# Event Loop to process "events" and get the "values" of the input
while True:
    event, values = window.read()
    print( f"event={event}" )
    if event is None or event == 'Ok' or event == 'Cancel': # if user closes window or clicks cancel
        break
        
# close  the window        
window.close()

if event == "Cancel":
    print( "You cancelled" )
else:
    print('You entered ', values[0])
    sg.popup( f"You selected {values[0]}" )