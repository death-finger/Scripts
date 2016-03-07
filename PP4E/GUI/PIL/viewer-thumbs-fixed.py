# e.g. 8-48

import sys, math
from tkinter import *
from PIL.ImageTk import PhotoImage
from viewer_thumbs import makeThumbs, ViewOne


def viewer(imgdir, kind=Toplevel, cols=None):
    win = kind()
    win.title('Viewer: ' + imgdir)
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = math.ceil(math.sqrt(len(thumbs)))
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        row = Frame(win)
        row.pack(fill=BOTH)
        for (imgfile, imgobj) in thumbsrow:
            size = max(imgobj.size)
            photo = PhotoImage(imgobj)
            handler = lambda savefile=imgfile: ViewOne(imgdir,savefile)
            link = Button(row, image=photo)
            link.config(command=handler, width=size, height=size)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)
    Button(win, text='Quit', command=win.quit()).pack(side=TOP, fill=X)
    return win, savephotos

if __name__ == '__main__':
    imgdir = 'images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()
