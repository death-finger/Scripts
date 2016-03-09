# e.g. 9-15

import sys, math
from tkinter import *
from PIL.ImageTk import PhotoImage
from viewer_thumbs import makeThumbs, ViewOne


def viewer(imgdir, kind=Toplevel, numcols=None, height=300, width=300):
    win = kind()
    win.title('Simple viewer: ' + imgdir)
    quit = Button(win, text='Quit', command=win.quit, bg='beige')
    quit.pack(side=BOTTOM, fill=X)

    canvas = Canvas(win, borderwidth=0)
    vbar = Scrollbar(win)
    hbar = Scrollbar(win, orient=HORIZONTAL)

    vbar.pack(side=RIGHT, fill=Y)
    hbar.pack(side=BOTTOM, fill=X)
    canvas.pack(side=TOP, fill=BOTH, expand=YES)

    vbar.config(command=canvas.yview)
    hbar.config(command=canvas.xview)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.config(height=height, width=width)

    thumbs = makeThumbs(imgdir)
    numthumbs = len(thumbs)
    if not numcols:
        numcols = int(math.ceil(math.sqrt(numthumbs)))
    numrows = int(math.ceil(numthumbs/numcols))

    linksize = max(thumbs[0][1].size)
    fullsize = (0, 0, linksize * numcols, linksize * numrows)
    canvas.config(scrollregion=fullsize)

    rowpos = 0
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:numcols], thumbs[numcols:]
        colpos=0
        for imgfile, imgobj in thumbsrow:
            photo = PhotoImage(imgobj)
            link = Button(canvas, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler, width=linksize, height=linksize)
            link.pack(side=LEFT, expand=YES)
            canvas.create_window(colpos, rowpos, anchor=NW, window=link,
                                 width=linksize, height=linksize)
            colpos += linksize
            savephotos.append(photo)
        rowpos += linksize
    return win, savephotos


if __name__ == '__main__':
    imgdir = 'images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()

