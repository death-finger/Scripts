# -*- coding:utf-8 -*-

from slideShow import SlideShow
from tkinter import *
import sys, os


class MySlideShowPlus(SlideShow):

    def __init__(self, parent=None):
        root = Tk()
        root.title('MySlideShow 1.00')
        root.minsize(width=720, height=480)
        root.maxsize(width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        SlideShow.__init__(self, root)
        self.scl_picConfig()



    def scl_picConfig(self):
        self.scl_var =DoubleVar()
        self.scl_pic.config(variable=self.scl_var, command=self.slideTime)

    def slideTime(self, *args):
        self.msecs = int(self.scl_var.get() * 1000)


    def onNote(self):
        pass

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
            self.adjuster = (97, 27)
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