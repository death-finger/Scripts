# e.g. 8-39

from sys import argv
from tkinter import *


gifdir = '../gifs/'
filename = argv[1] if len(argv) > 1 else 'ora-lp4e.gif'

win = Tk()
img = PhotoImage(file=gifdir + filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
