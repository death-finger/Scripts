# e.g. 8-19

from tkinter import *
from entry2 import makeform, fetch, fields

"""
def Dialog():
    win = Toplevel()
    ents = makeform(win, fields)
    btn = Button(win, text='OK', command=(lambda: fetch(ents))).pack(side=BOTTOM)
    win.bind('<Return>', fetch(ents))


root = Tk()
dialog_btn = Button(root, text='Dialog', command=Dialog)
dialog_btn.pack()
root.mainloop()
"""

def show(entries, popup):
    fetch(entries)
    popup.destroy()

def ask():
    popup = Toplevel()
    ents = makeform(popup, fields)
    btn = Button(popup, text='OK', command=(lambda: show(ents, popup))).pack(side=BOTTOM)
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()

root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
