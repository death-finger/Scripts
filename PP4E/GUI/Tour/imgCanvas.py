# e.g. 8-38

from tkinter import *


gifdir = '../gifs/'
win = Tk()
img = PhotoImage(file=gifdir + 'ora-lp4e.gif')
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2,image=img, anchor=NW)
win.mainloop()
