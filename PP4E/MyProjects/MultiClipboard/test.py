from tkinter import *


class Test(Frame):
    def __init__(self, parent=None):
        self.frm = Frame(self, parent)
        self.frm.pack()
        self.btn = Button(self.frm, text='quit', command=self.root.quit)
        self.btn.pack()


if __name__ == '__main__':
    Test().mainloop()