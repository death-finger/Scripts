from tkinter import *

class PopupSearchInput(Toplevel):
    def __init__(self, parent, title, lbltext):
        Toplevel.__init__(self, parent)
        self.title(title)
        frm = Frame(self)
        frm.pack(expand=YES, fill=BOTH)
        lbl = Label(frm, text=lbltext)
        lbl.config(padx=5)
        lbl.pack(side=TOP)
        text = Text(frm)
        text.config(padx=5, height=5)
        text.pack(side=TOP)
        ok_btn = Button(self, text='OK')
        ok_btn.config(padx=5, pady=1)
        ok_btn.pack(side=LEFT)
        cancel_btn = Button(self, text='Cancel')
        cancel_btn.config(pady=1)
        cancel_btn.pack(side=LEFT)
        self.focus_set()
        self.grab_set()
        self.wait_window()

if __name__ == '__main__':
    root = Tk()
    Button(root, text='popup', command=(lambda: PopupSearchInput(root, title='PyEdit', lbltext='Hahahahaha'))).pack()
    root.mainloop()