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

# 导入Menu和Toolbar所需组件
from makeMenuToolBar import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

helptext = """
Need To Be Implemented!
"""

version = 1.00

# 主体框架

class TextEditorMainFrame:

    menuBar = [('File', 0, [('Open...', 0, askopenfilename),
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
                                      ('Line Warp', 0, lambda: None),
                                      'separator',
                                      ('Pick Bg...', 5, lambda: None),
                                      ('Pick Fg...', 5, lambda: None),
                                      ('Color List', 0, lambda: None),
                                      'separator',
                                      ('Info...', 0, lambda: None),
                                      ('Clone', 0, lambda: None),
                                      ('Run Code', 0, lambda: None)])]

    def __init__(self):
        # 初始化设定
        self.file_path = '/Users/joshuapu/Documents/Scripts/PP4E/MyProjects/MyEdit'
        # 整体窗口
        self.main = Tk()
        self.main.title('MyEdit %.1f' % version)
        # 主菜单
        self.menu = Menu(self.main)
        self.main.config(menu=self.menu)
        self.makeMenu(self.menu)
        # 工具栏
        self.makeTools(self.main)
        # 主体部分, 包含文件路径栏, Text框以及Scrollbar
        self.makeText(self.main)

    def makeMenu(self, parent, helpButton=TRUE):
        for (name, key, items) in self.menuBar:
            menu_main = Menu(parent)
            self.makeMenuItems(menu_main, items)
            parent.add_cascade(label=name, underline=key, menu=menu_main)

        if helpButton:
            parent.add_command(label='Help', underline=0, command=self.help)

    def makeMenuItems(self, menu_name, items):
        for item in items:
            if item == 'separator':
                menu_name.add_separator()
            elif type(item) == list:
                for num in item:
                    #menu_name.entryconfig(num, state=DISABLED)
                    pass
            elif type(item[2]) != list:
                menu_name.add_command(label=item[0],
                                      underline=item[1],
                                      command=item[2])
            else:
                sub_name = Menu(menu_name)
                self.makeMenu(sub_name, item)

    def makeTools(self, parent):
        toolBar = [('Save', lambda: None, LEFT),
                   ('Cut', lambda: None, LEFT),
                   ('Copy', lambda: None, LEFT),
                   ('Paste', lambda: None, LEFT),
                   ('Find', lambda: None, LEFT),
                   ('Help', self.help, RIGHT),
                   ('Quit', sys.exit, RIGHT)]
        frame = Frame(parent)
        frame.pack(side=BOTTOM, fill=X)
        for (text, command, side) in toolBar:
            Button(frame, text=text, command=command).pack(side=side)

    def makeText(self, parent):
        frame_text = Frame(parent)
        frame_text.pack(side=LEFT, expand=YES, fill=BOTH)
        # 文件路径显示
        label_path = Label(frame_text, text=self.file_path)
        label_path.config(fg='white', bg='black', font=('times', 10, 'italic'))
        label_path.pack(side=TOP, fill=X)
        # 主Text窗口
        text_main = Text(frame_text)
        text_main_yscroll = Scrollbar(frame_text, command=text_main.yview, relief=SUNKEN)
        text_main_yscroll.pack(side=RIGHT, fill=Y)
        text_main.config(yscrollcommand=text_main_yscroll.set)
        text_main_xscroll = Scrollbar(frame_text, command=text_main.xview, orient=HORIZONTAL)
        text_main_xscroll.pack(side=BOTTOM, fill=X)
        text_main.config(xscrollcommand=text_main_xscroll.set)
        text_main.config(wrap=NONE)
        text_main.pack(side=TOP, expand=YES, fill=BOTH)




    ############################
    # 菜单按钮功能设定
    ############################
    def onFileOpen(self):
        self.file_path = askopenfilename()


    ############################
    # 额外信息显示
    ############################

    def help(self):
        showinfo('Help Info', helptext)


if __name__ == '__main__':
    TextEditorMainFrame()
    mainloop()