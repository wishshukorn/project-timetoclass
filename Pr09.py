import webbrowser
from win10toast_click import ToastNotifier
import time

page_url = 'https://forms.gle/MBFJDqNV95RxPZ4S7'

def open_url():
    try: 
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

toaster = ToastNotifier()

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == "21:44:30":
        print(current_time)
        break
    else:
        pass

toaster.show_toast("Are you studying now?",
                           "Click to check in",
                           icon_path = '',
                           duration = 5,
                           threaded = True,
                           callback_on_click = open_url)

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == "21:45:30":
        print(current_time)
        break
    else:
        pass

toaster.show_toast("Are you studying now?",
                           "Click to check in",
                           icon_path = '',
                           duration = 5,
                           threaded = True,
                           callback_on_click = open_url)