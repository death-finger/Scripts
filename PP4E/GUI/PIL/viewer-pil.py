# e.g. 8-43

import os, sys
from tkinter import *
from PIL import ImageTk


imgdir = 'images'
imgfile= 'florida-2009-1.jpg' if len(sys.argv) == 1 else sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
imgobject = ImageTk.PhotoImage(file=imgpath)
Label(win, image=imgobject).pack(fill=BOTH)
win.mainloop()
