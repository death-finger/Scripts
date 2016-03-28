# -*- coding:utf-8 -*-

from slideShow import SlideShow
from tkinter import *
import sys


class MySlideShowPlus(SlideShow):

    def __init__(self, parent=None):
        root = Tk()
        root.title('MySlideShow 1.00')
        root.minsize(width=720, height=480)
        root.maxsize(width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        SlideShow.__init__(root)
        self.scl_pic.config(command=lambda: None)



    def onNote(self):
        pass

    def start(self):
        self.init_btns = [('Note', self.onNote),
                          ('Open', self.onOpen),
                          ('Quit', self.onQuit),
                          ('Help', None),
                          'Scale']
        self.init_start = [('Start', self.onStart), ('Stop', self.onStop)]
        self.dir = '/Users/joshuapu/Documents/wallpaper' if sys.platform[:3] != 'win' else r'D:\Theme\wallpaper'
        self.adjuster = (111, 26)


if __name__ == '__main__':
    class Test(MySlideShowPlus):
        def test(self):
            self.onOpenScan()
            self.onDraw()

    Test().mainloop()