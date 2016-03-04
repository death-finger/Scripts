# e.g. 8-25

from tkinter import *
from dialogTable import demos
from quitter import Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Radio demos').pack(side=TOP)
        self.var = StringVar()
        for key in demos:
            Radiobutton(self, text=key, command=self.onPress,
                        variable=self.var, value=key).pack(anchor=NW)
        self.var.set(key)   # 选中最后一个以开始
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)

    def onPress(self):
        pick = self.var.get()
        print('You pressed', pick)
        print('Result:', demos[pick]())

    def report(self):
        print(self.var.get())

class MyDemo(Demo):
    def __init__(self, parent=None, **options):
        Demo.__init__(self, parent, **options)
        msglab = Label(self, text=self.onPress).pack(side=RIGHT)


if __name__ == '__main__':
#    Demo().mainloop()
    MyDemo().mainloop()