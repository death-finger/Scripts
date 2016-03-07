# e.g. 8-36

from tkinter import *


class CheckBar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return [var.get() for var in self.vars]


class RadioBar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.var = StringVar()
        for pick in picks:
            rad = Radiobutton(self, text=pick, variable=self.var, value=pick)
            rad.pack(side=side, anchor=anchor, expand=YES)
        self.var.set(pick)

    def state(self):
        return self.var.get()


if __name__ == '__main__':
    root = Tk()
    lng = CheckBar(root, ['Python', 'C#', 'Java', 'C++'])
    gui = RadioBar(root, ['win', 'x11', 'mac'], side=TOP, anchor=NW)
    tgl = CheckBar(root, ['All'])

    gui.pack(side=LEFT, fill=Y)
    lng.pack(side=TOP, fill=X)
    tgl.pack(side=LEFT)
    lng.config(relief=GROOVE, bd=2)
    gui.config(relief=RIDGE, bd=2)

    def allstates():
        print(gui.state(), lng.state(), tgl.state())

    from quitter import Quitter
    Quitter(root).pack(side=RIGHT)
    Button(root, text='Peek', command=allstates).pack(side=RIGHT)
    root.mainloop()
