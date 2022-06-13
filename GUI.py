import os
from tkinter import *

global root
global s
global entry

def eventhandler(event):
    global s
    global root
    s = entry.get()
    root.destroy()


def play():
    global root
    root = Tk()
    global entry
    global s
    entry = Entry(root, bd=4)
    # entry.bind_all('<Control-f>', eventhandler)  # 绑定快捷键Ctrl-f
    entry.pack()
    entry.focus()
    entry.bind("<Return>", eventhandler)
    root.attributes("-topmost", 1)
    root.focus_force()
    os.system("open -a Python")
    root.mainloop()
    return s

