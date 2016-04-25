# 窗口框架

from tkinter import *

class MainWindow(Tk):
    def __init__(self):
        self.start()
        Tk.__init__(self)
        self.title('MyMailGUI')
        self.makeWidgets()

    def makeWidgets(self):
        frm_main = Frame(self)
        frm_main.pack(side=TOP, anchor=NW, fill=BOTH, expand=YES)
        btn_help = Button(frm_main, text='MyMailGui - a Python/tkinter email client (help)')
        btn_help.config(command=self.help, relief=FLAT, height=1)
        btn_help.pack(side=TOP, anchor=N, fill=X, expand=NO)
        canv_mail = Canvas(frm_main)
        canv_mail.config(bg='gray')
        canv_mail.pack(side=TOP, anchor=N, fill=BOTH, expand=YES)
        self.makeMenus(frm_main)

    def makeMenus(self, parent=None):
        for item, func, side, anc in self.menulist:
            btn = Button(parent, text=item, relief=FLAT, height=1)
            btn.config(command=func)
            btn.pack(side=side, anchor=anc)


    def help(self):
        pass

    def start(self):
        self.menulist = [('Load', None, LEFT, SW),
                    ('Open', None, LEFT, SW),
                    ('Write', None, LEFT, SW),
                    ('View', None, RIGHT, SE),
                    ('Reply', None, RIGHT, SE),
                    ('Fwd', None, RIGHT, SE),
                    ('Save', None, RIGHT, SE),
                    ('Delete', None, RIGHT, SE)]


if __name__ == '__main__':
    MainWindow()
    mainloop()