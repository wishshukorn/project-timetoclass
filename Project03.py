import time
import pygame
import webbrowser
from win10toast_click import ToastNotifier

page_url = 'https://forms.gle/MBFJDqNV95RxPZ4S7'

def open_url():
    try: 
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')
    
toaster = ToastNotifier()

pygame.init()
clock = pygame.time.Clock()
while True:
        clock.tick(1)
        theTime=time.strftime("%H:%M:%S", time.localtime())
        print (theTime)
    
        if theTime == "20:20:00":
            toaster.show_toast("Start the first period at 08:30, are you studying now?",
                       "Click here to check in",
                       icon_path = None,
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)