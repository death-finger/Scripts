# -*- coding:utf-8 -*-
"""
########################################################################
主窗口，包含主框架 > 菜单栏 > 文件名栏 > 文本框/YScrollBar > XScrollBar >
状态栏(Save/Cut/Copy/Paste/Find > Quit/Help)
########################################################################
"""

from tkinter import *
from tkinter.ttk import *


class MyMenu(Menu):
    def __init__(self, parent=None):
        top = Menu(parent)
        parent.config(menu=top)
        self.makeMenu(top)

    def makeMenu(self, parent):
        # File Menu
        file = Menu(parent, tearoff=True)
        file.add_command(label='Open', command=self.notdone, underline=0)
        file.add_command(label='Save', command=self.notdone, underline=0)
        file.add_command(label='Save As', command=self.notdone, underline=5)
        file.add_command(label='New', command=self.notdone, underline=0)
        file.add_separator()
        file.add_command(label='Quit', command=self.notdone, underline=0)
        parent.add_cascade(label='File', menu=file, underline=0)

        # Edit Menu
        edit = Menu(parent, tearoff=True)
        edit.add_command(label='Undo', command=self.notdone, underline=0)
        edit.add_command(label='Redo', command=self.notdone, underline=0)
        edit.add_separator()
        edit.add_command(label='Cut', command=self.notdone, underline=0)
        edit.add_command(label='Copy', command=self.notdone, underline=0)
        edit.add_command(label='Paste', command=self.notdone, underline=0)
        edit.add_separator()
        edit.add_command(label='Delete', command=self.notdone, underline=0)
        edit.add_command(label='Select All', command=self.notdone, underline=0)
        parent.add_cascade(label='Edit', menu=edit, underline=0)



    def notdone(self):
        pass



if __name__ == '__main__':
    root = Tk()
    MyMenu(root)
    root.mainloop()