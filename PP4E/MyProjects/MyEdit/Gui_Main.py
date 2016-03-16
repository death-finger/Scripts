# -*- coding:utf-8 -*-
"""
########################################################################
主窗口，包含主框架 > 菜单栏 > 文件名栏 > 文本框/YScrollBar > XScrollBar >
状态栏(Save/Cut/Copy/Paste/Find > Quit/Help)
########################################################################
"""

# 导入通用组件

from tkinter import *
import os, sys


# 主体框架

# 导入文本框组件
from tkinter.scrolledtext import ScrolledText

class TextEditorMainFrame:
    def __init__(self):
        # 初始化设定
        self.version_set()
        self.file_path = '/Users/joshuapu/Documents/Scripts/PP4E/MyProjects/MyEdit'
        # 主窗口
        self.main = Tk()
        self.main.title('MyEdit %.1f' % self.version)
        # 主菜单
        self.menu = Menu(self.main)
        self.main.config(menu=self.menu)
        makeMenu(self.menu)
        # 主体部分, 包含文件路径栏, Text框以及Scrollbar
        self.makeFrame(self.main)

    def makeFrame(self, parent):
        frame_main = Frame(parent)
        frame_main.pack(expand=YES, fill=BOTH)
        # 文件路径显示
        label_path = Label(frame_main, text=self.file_path)
        label_path.config(fg='white', bg='black', font=('times', 10, 'italic'))
        label_path.pack(side=TOP, fill=X)
        # 主Text窗口
        text_main = Text(frame_main)
        text_main_yscroll = Scrollbar(frame_main, command=text_main.yview, relief=SUNKEN)
        text_main_yscroll.pack(side=RIGHT, fill=X)
        text_main.config(yscrollcommand=text_main_yscroll.set)
        text_main_xscroll = Scrollbar(frame_main, command=text_main.xview, orient=HORIZONTAL)
        text_main_xscroll.pack(side=BOTTOM, fill=X)
        text_main.config(xscrollcommand=text_main_xscroll.set)
        text_main.pack(side=TOP, expand=YES, fill=BOTH)

    ############################
    # 菜单按钮功能设定
    ############################
    def onFileOpen(self):
        self.file_path = askopenfilename()


    ############################
    # 额外信息显示
    ############################
    def version_set(self):
        self.version = 1.00

# 导入菜单制作工具

from makeGuiTool import MakeGui
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo


class makeMenu(MakeGui):
    def start(self):
        self.menuBar = [('File', 0, [('Open...', 0, askopenfilename),
                                     ('Save', 0, lambda: None),
                                     ('Save As...', 5, asksaveasfilename),
                                     ('New', 0, lambda: None),
                                     'separator',
                                     ('Quit', 0, sys.exit)]),
                        ('Edit', 0, [('Undo', 0, lambda: None),
                                     ('Redo', 0, lambda: None),
                                     'separator',
                                     ('Cut', 0, lambda: None),
                                     ('Copy', 0, lambda: None),
                                     ('Paste', 0, lambda: None),
                                     'separator',
                                     ('Delete', 0, lambda: None),
                                     ('Select All', 7, lambda: None)]),
                        ('Search', 0, [('Goto...', 0, lambda: None),
                                       ('Find...', 0, lambda: None),
                                       ('Refind', 0, lambda: None),
                                       ('Change...', 0, lambda: None),
                                       ('Grep...', 0, lambda: None)]),
                        ('Tools', 0, [('Pick Font...', 0, lambda: None),
                                      ('Font List', 0, lambda: None),
                                      'separator',
                                      ('Pick Bg...', 5, lambda: None),
                                      ('Pick Fg...', 5, lambda: None),
                                      ('Color List', 0, lambda: None),
                                      'separator',
                                      ('Info...', 0, lambda: None),
                                      ('Clone', 0, lambda: None),
                                      ('Run Code', 0, lambda: None)])]

    def help(self):
        showinfo("Help Info", 'No help for now...')



if __name__ == '__main__':
    TextEditorMainFrame()
    mainloop()