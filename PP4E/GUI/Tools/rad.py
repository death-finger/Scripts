# e.g. 10-14

from tkinter import *
import radactions
from importlib import reload


class Hello(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        Button(self, text='message1', command=self.message1).pack(side=LEFT)
        Button(self, text='message2', command=self.message2).pack(side=RIGHT)

    def message1(self):
        reload(radactions)
        radactions.message1()

    def message2(self):
        reload(radactions)
        radactions.message2(self)

    def method1(self):
        print('exposed method...')

Hello().mainloop()
