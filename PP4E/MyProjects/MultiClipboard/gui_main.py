# -*- coding:utf-8 -*-
"""
主窗口GUI框架
"""

from tkinter import *
from tkinter.messagebox import askyesno, showerror, showinfo


class GuiMainWindow(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent, width='500', height='500')
        self.pack(expand=YES, fill=BOTH)
        self.btnfrm = Frame(self)
        self.btnfrm.pack(side=TOP)
        self.makeButtons(self.btnfrm)
        self.tabfrm = Frame(self, width='50', height='512')
        self.tabfrm.pack(side=LEFT, fill=Y)
        self.makeTabs(self.tabfrm)

    def makeButtons(self, parent):
        self.btn_quit = self.makeQuitBtn(parent)
        self.makeConfBtn(parent)
        self.makeFloatWinBtn(parent)
        self.makeWatchBtn(parent)
        self.makeOrdPasteBtn(parent)
        self.makeHelpBtn(parent)
        self.makePurchaseBtn(parent)
        self.btn_info = self.makeInfoBtn(parent)

    def makeQuitBtn(self, parent):
        btn = Button(parent, text='退出', command=self.quit)
        btn.pack(side=LEFT)
        return btn

    def makeConfBtn(self, parent):
        Button(parent, text='设置', command=self.notdone).pack(side=LEFT)

    def makeFloatWinBtn(self, parent):
        Button(parent, text='浮动窗', command=self.notdone).pack(side=LEFT)

    def makeWatchBtn(self, parent):
        Button(parent, text='监视', command=self.notdone).pack(side=LEFT)

    def makeOrdPasteBtn(self, parent):
        Button(parent, text='顺序', command=self.notdone).pack(side=LEFT)

    def makeHelpBtn(self, parent):
        Button(parent, text='帮助', command=self.notdone).pack(side=LEFT)

    def makePurchaseBtn(self, parent):
        Button(parent, text='购买', command=self.notdone).pack(side=LEFT)

    def makeInfoBtn(self, parent):
        btn = Button(parent, text='关于', command=self.showInfoBtn)
        btn.pack(side=LEFT)
        return btn

    def showInfoBtn(self):
        showinfo('关于此程序', '此程序由Joshua Pu开发，仅供测试使用。')

    def makeTabs(self, parent):
        self.tab_btn_up = self.tabBtnUp(parent)
        self.tab_btn_down = self.tabBtnDown(parent)
        self.tab_tab_dft = self.tabTabDefalt(parent)

    def tabBtnUp(self, parent):
        btn = Label(parent, text='⬆')
        btn.config(width=1, height=1)
        btn.pack(side=TOP)
        return btn

    def tabBtnDown(self, parent):
        btn = Label(parent, text='⬇')
        btn.config(width=1, height=1)
        btn.pack(side=BOTTOM)
        return btn

    def tabTabDefalt(self, parent):
        btn = Label(parent, text='活\n动\n列\n表', width=1, height=5)
        btn.pack(side=TOP)
        return btn

    def notdone(self):
        showerror('Sorry', 'This function still not implemented...')



if __name__ == '__main__':
    GuiMainWindow().mainloop()