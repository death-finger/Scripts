# e.g. 11-6

import os
from tkinter import *
from PP4E.GUI.TextEditor.textEditor import *
from slideShow import SlideShow
Size = (300, 550)


class SlideShowPlus(SlideShow):
    def __init__(self, parent, picdir, editclass, msecs=2000, size=Size):
        self.msecs = msecs
        self.editclass = editclass
        SlideShow.__init__(self, parent, picdir, msecs, size)

    def makeWidgets(self):
        self.name = Label(self, text='None', bg='red', relief=RIDGE)
        self.name.pack(fill=X)
        SlideShow.makeWidgets(self)
        Button(self, text='Note', command=self.onNote).pack(fill=X)
        Button(self, text='Help', command=self.onHelp).pack(fill=X)
        s = Scale(label='Speed: msec delay', command=self.onScale,
                  from_=0, to=3000, resolution=50, showvalue=YES,
                  length=400, tickinterval=250, orient=HORIZONTAL)
        s.pack(side=BOTTOM, fill=X)
        s.set(self.msecs)

        self.editorGone = False
