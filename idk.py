from src.win10toast.win10toast import ToastNotifier
import tkinter as tk
from tkinter import *
import webbrowser

top = tk.Tk()
top.geometry('50x50')
top.title('shop')

url = 'http://www.google.com'

def notify():
   noti.show_toast('Random','Hello World',duration=60, threaded=True,callback_on_click=action) 

def action():
    webbrowser.open_new(url)
    print("Done")
    
noti = ToastNotifier() 
btn = Button(top, text= "Enter", command=notify)
btn.pack()

top.mainloop()