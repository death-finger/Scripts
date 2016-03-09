# e.g. 9-15

import sys, math, os
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askokcancel
from PIL.ImageTk import PhotoImage
from PIL import Image


class Viewer(Frame):
    def __init__(self, parent=None, imgdir='images', cols=10):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.thumbs = []
        self.saveimages = []
        self.imgdir = imgdir
        self.cols = cols
        Button(self, text='Quit', command=self.FuncQuit).pack(side=BOTTOM, fill=X)
        self.makeThumbs()
        self.makeCanvas()
        self.makeButtons(self.canvas)


    def makeThumbs(self):
        self.imgdir = askdirectory() or self.imgdir
        thumbsdir = os.path.join(self.imgdir, 'thumbs')
        if not os.path.exists(thumbsdir):
            os.mkdir(thumbsdir)
        imgfiles = os.listdir(self.imgdir)
        for imgfile in imgfiles:
            imgpath = os.path.join(self.imgdir, imgfile)
            thumbpath = os.path.join(thumbsdir, imgfile)
            if os.path.exists(os.path.join(thumbpath, imgfile)):
                thumbobj = PhotoImage(file=os.path.join(thumbpath, imgfile))
                self.thumbs.append((imgfile, thumbobj))
            else:
                try:
                    imgobj = Image.open(imgpath)
                    imgobj.thumbnail((128, 128), Image.ANTIALIAS)
                    imgobj.save(thumbpath)
                    self.thumbs.append((imgfile, imgobj))
                except:
                    print('Skipping =>', imgpath, sys.exc_info())

    def makeCanvas(self):
        length = (len(self.thumbs) // self.cols + 1) * 128
        width = self.cols * 128
        self.canvas = Canvas(self)
        self.canvas.config(width=768, height=512, bg='white')
        self.canvas.config(scrollregion=(0, 0, width, length))
        self.yscroll = Scrollbar(self)
        self.xscroll = Scrollbar(self, )
        self.yscroll.config(command=self.canvas.yview)
        self.xscroll.config(command=self.canvas.xview, orient=HORIZONTAL)
        self.canvas.config(yscrollcommand=self.yscroll.set, xscrollcommand=self.xscroll.set)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.xscroll.pack(side=BOTTOM, fill=X)
        self.canvas.pack(side=LEFT, anchor=NW, expand=YES, fill=BOTH)

    def makeButtons(self, parent):
        rowpos = 0
        while self.thumbs:
            thumbs, self.thumbs = self.thumbs[:self.cols], self.thumbs[self.cols:]
            colpos = 0
            for (imgfile, imgobject) in thumbs:
                img = PhotoImage(imgobject)
                btn = Button(self.canvas, image=img, command=(lambda imgfile=imgfile: self.OnPress(imgfile)))
                btn.config(width=128, height=128)
                btn.pack(side=LEFT, expand=YES)
                self.canvas.create_window(colpos, rowpos, anchor=NW, window=btn, width=128, height=128)
                colpos += 128
                self.saveimages.append(img)
            rowpos += 128

    def FuncQuit(self):
        ans = askokcancel('Quit Confirm', 'Really?')
        if ans:
            self.quit()

    def OnPress(self, imgfile):
        win = Toplevel(self)
        imgpath = os.path.join(self.imgdir, imgfile)
        imgobj = PhotoImage(file=imgpath)
        win.title('Viewer:'+ imgpath)
        Label(win, image=imgobj).pack(side=LEFT, expand=YES)
        self.saveimages.append(imgobj)
        win.focus_set()
        win.grab_set()
        win.wait_window()


if __name__ == '__main__':
    Viewer().mainloop()