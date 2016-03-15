from tkinter import *
from tkinter.scrolledtext import ScrolledText
cp_list = []


class MainFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)




class MyClipboardFunc(Toplevel):
    global cp_list
    def __init__(self, parent=None):
        Toplevel.__init__(self, parent)
        self.frm = Frame(self)
        self.frm.pack()
        self.scrltxt = ScrolledText(self.frm, width=50, height=15)
        self.scrltxt.pack(side=TOP, fill=BOTH, expand=YES)
        btn_add = Button(self.frm, text='Add', command=self.onAdd)
        btn_add.pack(side=BOTTOM, anchor=NW)
        btn_back = Button(self.frm, text='Back', command=self.onBack)
        btn_back.pack(side=BOTTOM, anchor=NE)

    def onAdd(self):
        text = self.scrltxt.get(SEL_FIRST, SEL_LAST)
        seq = len(cp_list)
        if not text in cp_list:
            cp_list.append((seq, text))

    def onBack(self):
        print(cp_list)
        self.destroy()


class Quitter(Frame):
    def __init__(self):


if __name__ == '__main__':
    root = Tk()
    Button(root, text='popup', command=lambda: MyClipboardFunc(root)).pack()
    mainloop()