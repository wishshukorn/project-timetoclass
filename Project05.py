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
        
        if theTime == "19:05:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = None,
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)

        if theTime == "19:06:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = None,
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
            
        if theTime == "19:07:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = None,
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
            
        if theTime == "19:08:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = None,
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
        
        if theTime == "19:09:00":
            toaster.show_toast("Are you studying now?",
                               "Click to check in",
                               icon_path = None,
                               duration = 5,
                               threaded = True,
                               callback_on_click = open_url)
