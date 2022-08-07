import webbrowser
from win10toast_click import ToastNotifier
import pygame
import time

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
        
        if theTime == "22:20:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)

        if theTime == "22:21:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
            
        if theTime == "22:22:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
            
        if theTime == "22:23:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
        
        if theTime == "22:24:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)