# e.g. 8-11

from tkinter import *
from tkinter.colorchooser import askcolor

def setBgColor():
    color = askcolor()
    context.config(bg=color[1])

root = Tk()
color_button = Button(root, text='Select Color', command=setBgColor)
color_button.pack(side=BOTTOM)
context = Label(root, text='Color Test Here')
context.pack(side=TOP, expand=YES, fill=BOTH)

root.mainloop()
