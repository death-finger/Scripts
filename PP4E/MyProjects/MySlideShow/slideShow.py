# -*- coding:utf-8 -*-

import os, sys, glob
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno
from PIL import Image
from PIL.ImageTk import PhotoImage

class SlideShow(Frame):
    init_btns = []
    init_start = []
    start_stu = True
    dir = ''
    img_save = []
    img_obj = None
    img_onScreen = 0

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(side=TOP , expand=YES, fill=BOTH)
        self.start()
        self.canv_lab, self.lab_path, self.canv = self.makeCanvas()
        self.scl_pic, self.btn_start = self.makeWidgets()
        self.makeThumbs()

        self.test()

######################################################
# Main Frame
######################################################

    def makeWidgets(self):
        labfrm = LabelFrame(self, text='Menu', labelanchor=SW)
        labfrm.pack(side=TOP, anchor=N)
        row=1
        for item in self.init_btns:
            if type(item) == type(()):
                btn = Button(labfrm, text=item[0], command=item[1], relief=GROOVE)
                btn.config(width=4, height=1)
                btn.grid(row=row, column=0, sticky=W)
                row += 1
        btn_start = Button(labfrm, text=self.init_start[0][0], width=4, height=1,
                           relief=GROOVE, command=self.init_start[0][1])
        btn_start.grid(row=0, column=0, sticky=W)
        if self.init_btns[-1] == 'Scale':
            scl = Scale(labfrm, from_=0, to=3, length=150, resolution=0.1)
            scl.config(font=('times', 8, 'normal'))
            scl.grid(row=0, column=1, rowspan=row+1)
            return scl, btn_start
        return None, btn_start

    def makeCanvas(self):
        lab = Label(self, text='Welcome to SlideShow', relief=FLAT, bg='#CBCBCB')
        lab.pack(side=TOP, anchor=N, expand=YES, fill=X)
        canv = Canvas(self)
        canv.pack(side=LEFT, anchor=N, expand=YES, fill=BOTH)
        canv_lab = Label(canv, relief=FLAT)
        canv.create_window(0, 0, anchor=NW, window=canv_lab)
        canv_lab.pack(side=TOP, anchor=NW, fill=BOTH)
        return canv_lab, lab, canv

    def makeThumbs(self):
        Scale(self, from_=0, to=len(self.img_save), resolution=0).pack(side=RIGHT, fill=Y)


######################################################
# Button Actions
######################################################

    def onStart(self):
        self.btn_start.config(text=self.init_start[1][0], command=self.init_start[1][1])
        self.btn_start.update()
        self.loop = True
        self.onStartShow()

    def onStop(self):
        self.btn_start.config(text=self.init_start[0][0], command=self.init_start[0][1])
        self.btn_start.update()
        self.onStopShow()

    def onOpen(self):
        file_path = askdirectory()
        if file_path:
            self.img_onScreen = 0
            self.img_save = []
            self.onOpenScan()
            if self.img_save:
                self.onDraw()
            else:
                return
        else:
            return

    def onQuit(self):
        if askyesno('MySlideShow', 'Confirm to quit?'):
            self.onStop()
            self.quit()

    def test(self):
        pass

######################################################
# Functions
######################################################

    def onOpenScan(self):
        if self.dir:
            files = glob.glob(os.path.join(self.dir, '*'))
            for file in files:
                try:
                    img = Image.open(file)
                except:
                    print('Skipping => ', file)
                else:
                    print('Catch: ', file)
                    self.img_save.append((file, img))

    def onDraw(self):
        try:
            img = Image.open(self.img_save[self.img_onScreen][0])
            size_canv = (int(self.winfo_width()-self.adjuster[0]), int(self.winfo_height()-self.adjuster[1]))
            if size_canv[0]-1 <= 0 or size_canv[1]-1 <= 0:
                size_canv = 720, 480
            scale = img.size[0]/size_canv[0]
            size = size_canv[0], int(img.size[1] / scale)
            img_resize = img.resize(size, Image.ANTIALIAS)
            img_obj = PhotoImage(img_resize)
            self.img_obj = img_obj
            self.canv_lab.config(image=img_obj)
            self.canv_lab.update()
            self.img_onScreen += 1
        except IndexError:
            self.img_onScreen = 0
            self.onDraw()

    def onStartShow(self, msecs=250):
        if self.loop:
            self.onDraw()
            try:
                msecs = self.msecs
            except:
                msecs = msecs
            self.task = self.canv.after(msecs, self.onStartShow)

    def onStopShow(self):
        self.loop = False




######################################################
# Initializing
######################################################

    def start(self):
        self.init_btns = [('Open', None),
                          ('Quit', None),
                          ('Help', None),
                          ]
        self.init_start = [('Start', self.onStart), ('Stop', self.onStop)]
        if sys.platform[:3] != 'win':
            self.adjuster = (72, 26)
        else:
            self.adjuster = (51, 27)


if __name__ == '__main__':
    class Test(SlideShow):
        def start(self):
            self.init_btns = [('Open', self.onOpen),('Quit', self.onQuit),('Help', None)]
            self.init_start = [('Start', self.onStart), ('Stop', self.onStop)]
            for path in ('/Users/joshuapu/Documents/wallpaper',
                         r'D:\Theme\wallpaper',
                         'G:\WallPaper'):
                if os.path.exists(path):
                    self.dir = path
            if sys.platform[:3] != 'win':
                self.adjuster = (72, 26)
            else:
                self.adjuster = (51, 27)

        def onQuit(self):
            self.quit()

        def test(self):
            #pass
            self.onOpenScan()
            self.onDraw()

    root = Tk()
    root.minsize(width=720, height=480)
    root.maxsize(width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    Test(root)
    mainloop()