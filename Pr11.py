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
        
        if theTime == "21:55:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)

        if theTime == "21:56:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
            
        if theTime == "21:57:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
            
        if theTime == "21:58:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
        
        if theTime == "21:59:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = '',
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)