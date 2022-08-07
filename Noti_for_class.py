import time,pygame
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
   
        if theTime == "08:35:00":
            toaster.show_toast("Start the first period at xx:xx, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:36:00":
            toaster.show_toast("Start the first period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:37:00":
            toaster.show_toast("Start the second period at xx:xx, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:38:00":
            toaster.show_toast("Start the second period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)     
        if theTime == "08:39:00":
            toaster.show_toast("Start the third period at xx:xx, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:40:00":
            toaster.show_toast("Start the third period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:41:00":
            toaster.show_toast("Start the fifth period at xx:xx, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:42:00":
            toaster.show_toast("Start the fifth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:43:00":
            toaster.show_toast("Start the sixth period at xx:xx, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:44:00":
            toaster.show_toast("Start the sixth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:45:00":
            toaster.show_toast("Start the seventh period at xx:xx, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:46:00":
            toaster.show_toast("Start the seventh period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:47:00":
            toaster.show_toast("Start the eighth period at xx:xx, are you studying now?",
                       "Click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:48:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:49:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:50:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:51:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:52:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:53:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:54:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:55:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:56:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:57:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:58:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "08:59:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:00:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:01:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:02:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:03:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:04:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:05:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:06:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:07:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:08:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:09:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)
        if theTime == "09:10:00":
            toaster.show_toast("Start the eighth period at xx:xx, have you checked in?",
                       "If you havn't, click here to check in",
                       icon_path = '',
                       duration = 10,
                       threaded = True,
                       callback_on_click = open_url)