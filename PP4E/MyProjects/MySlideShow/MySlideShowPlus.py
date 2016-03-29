# -*- coding:utf-8 -*-

from slideShow import SlideShow
import os, sys, glob
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno
from PIL import Image
from PIL.ImageTk import PhotoImage


class MySlideShowPlus(SlideShow):

    note_status = False
    pic_thumbs = []
    img_obj_thumbs = []

    def __init__(self):
        SlideShow.__init__(self)
        self.scl_picConfig()
        self.scl_thumb = self.makeSclThumbs()
        self.canv_thumb = self.makeCanvThumbs()

##############################
# Main Frame
##############################

    def scl_picConfig(self):
        self.scl_var =DoubleVar()
        self.scl_pic.config(variable=self.scl_var, command=self.slideTime)


    def makeSclThumbs(self):
        scl_thumbs = Scrollbar(self.frm_right, relief=FLAT)
        scl_thumbs.grid(row=1, column=2, sticky=NS)
        return scl_thumbs

    def makeCanvThumbs(self):
        canv = Canvas(self.frm_right, width=10)
        canv.grid(row=1, column=0, columnspan=2, sticky=NSEW)
        return canv

    def makeText(self):
        text = Text(self, height=3, relief=GROOVE)
        text.pack(side=BOTTOM, expand=YES, fill=BOTH)
        return text

##############################
# Menu
##############################

    def onNote(self):
        self.note_status = not self.note_status
        if self.note_status:
            self.note = self.makeText()
        else:
            self.note.forget()
            self.update()


    def onOpen(self):
        file_path = askdirectory()
        if file_path:
            self.img_onScreen = 0
            self.img_save = []
            self.onOpenScan()
            if self.img_save:
                self.onDraw()
                self.drawCanvThumb()
            else:
                return
        else:
            return


##############################
# Func
##############################

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
            self.pic_thumbs = self.makeThumbs()

    def drawCanvThumb(self):
        self.img_obj_thumbs = []
        self.canv_thumb.config(scrollregion=(0,0,40,40*len(self.pic_thumbs)),
                               yscrollcommand=self.scl_thumb.set)
        self.scl_thumb.config(command=self.canv_thumb.yview)
        row = 0
        for file, img in self.pic_thumbs:
            img_obj = PhotoImage(img)
            self.canv.create_image(0,row*40, anchor=NW, image=img_obj)
            self.img_obj_thumbs.append(img_obj)
            row += 1
        self.canv_thumb.update()

    def onStartShow(self, msecs=250):
        if self.loop:
            self.onDraw()
            if self.note_status:
                self.onNoteFunc()
            try:
                msecs = self.msecs
            except:
                msecs = msecs
            self.task = self.canv.after(msecs, self.onStartShow)

    def onNoteFunc(self):
        txt_path = os.path.join(self.dir, '.note/')
        if not os.path.exists(txt_path):
            os.mkdir(txt_path)
        txt_file = os.path.join(txt_path, self.img_save[self.img_onScreen][0])
        if os.path.exists(txt_file):
            txt = open(txt_file).read()
            self.note.insert(0.0, txt)
        else:
            pass

    def makeThumbs(self, size=(40, 40)):
        files = os.listdir(self.dir)
        dir_path = self.dir
        thumb_path = os.path.join(dir_path, 'thumbs')
        img_obj = []
        if not os.path.exists(thumb_path):
            os.mkdir(thumb_path)
        for file in files:
            if not os.path.exists(os.path.join(thumb_path, file)):
                try:
                    img = Image.open(os.path.join(dir_path, file))
                    img.thumbnail(size, Image.ANTIALIAS)
                    img.save(os.path.join(thumb_path, file))
                    print('Creating thumbs => %s' % file)
                except:
                    print('Skipfile => %s' % file)
                else:
                    img_obj.append((file, img))
            else:
                img = Image.open(os.path.join(thumb_path, file))
                img_obj.append((file, img))
                print('Exist thumbs => %s' %file)
        return img_obj


###########################################
# Initial

    def slideTime(self, *args):
        self.msecs = int(self.scl_var.get() * 1000)

    def start(self):
        self.init_btns = [('Note', self.onNote),
                          ('Open', self.onOpen),
                          ('Quit', self.onQuit),
                          ('Help', None),
                          'Scale']
        self.init_start = [('Start', self.onStart), ('Stop', self.onStop)]
        self.adjuster = (111, 26)


if __name__ == '__main__':
    class Test(MySlideShowPlus):
        def start(self):
            self.init_btns = [('Note', self.onNote),
                              ('Open', self.onOpen),
                              ('Quit', self.onQuit),
                              ('Help', None),
                              'Scale']
            self.init_start = [('Start', self.onStart), ('Stop', self.onStop)]
            self.adjuster = (111, 26)
            for path in ('/Users/joshuapu/Documents/wallpaper',
                         r'D:\Theme\wallpaper',
                         'G:\WallPaper'):
                if os.path.exists(path):
                    self.dir = path

        def onQuit(self):
            self.onStop()
            self.quit()

        def test(self):
            self.onOpenScan()
            self.onDraw()

    Test().mainloop()