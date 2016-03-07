# e.g. 8-37

from tkinter import *


gifdir = "../gifs/"
win = Tk()
igm = PhotoImage(file=gifdir + 'ora-pp.gif')
Button(win, image=igm).pack()
win.mainloop()
