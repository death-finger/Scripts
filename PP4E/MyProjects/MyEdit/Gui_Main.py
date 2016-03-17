# -*- coding:utf-8 -*-
"""
########################################################################
主窗口，包含主框架 > 菜单栏 > 文件名栏 > 文本框/YScrollBar > XScrollBar >
状态栏(Save/Cut/Copy/Paste/Find > Quit/Help)
########################################################################
"""

# 导入通用组件

from tkinter import *
import sys, os

# 导入Menu和Toolbar所需组件
from makeMenuToolBar import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, askokcancel
from tkinter.simpledialog import askinteger, askstring


# 附加信息

version = 1.00

helptext = """
MyEditor version %.2f

Programmed by Joshua.
On reference to PyEdit 2.1 from Mark Lutz.

Reference:
Programming Python 4th Edition
Mark Lutz(Published by O'Reilly)
All rights reserved: Mark Lutz, 2011
978-0-596-15810-1
""" % version


# 主体框架

class TextEditorMainFrame:
    def __init__(self):
        # 初始化设定
        self.file_path = 'Welcome!'
        self.clip_board = []
        self.find_text = ""

        self.toolBar = [('Save', self.onFileSave, LEFT),
                        ('Cut', self.onEditCut, LEFT),
                        ('Copy', self.onEditCopy, LEFT),
                        ('Paste', self.onEditPaste, LEFT),
                        ('Find', self.onSearchFind, LEFT),
                        ('Help', self.help, RIGHT),
                        ('Quit', sys.exit, RIGHT)]

        self.menuBar = [('File', 0, [('Open...', 0, self.onFileOpen),
                                     ('Save', 0, self.onFileSave),
                                     ('Save As...', 5, self.onFileSaveAs),
                                     ('New', 0, self.onFileNew),
                                     'separator',
                                     ('Quit', 0, sys.exit)]),
                        ('Edit', 0, [('Undo', 0, self.onEditUndo),
                                     ('Redo', 0, self.onEditRedo),
                                     'separator',
                                     ('Cut', 0, self.onEditCut),
                                     ('Copy', 0, self.onEditCopy),
                                     ('Paste', 0, self.onEditPaste),
                                     'separator',
                                     ('Delete', 0, self.onEditDelete),
                                     ('Select All', 7, self.onEditSelectAll)]),
                        ('Search', 0, [('Goto...', 0, self.onSearchGoto),
                                       ('Find...', 0, self.onSearchFind),
                                       ('Refind', 0, self.onSearchRefind),
                                       ('Change...', 0, self.onSearchChange),
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
        # 切换到此窗口
        self.main.focus_set()

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
        frame = Frame(parent)
        frame.pack(side=BOTTOM, fill=X)
        for (text, command, side) in self.toolBar:
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
        text_main.config(wrap=NONE, autoseparators=True, undo=True, maxundo=50)
        text_main.pack(side=TOP, expand=YES, fill=BOTH)
        self.frame_text = frame_text
        self.label_path = label_path
        self.text_main = text_main




    ############################
    # 菜单按钮功能设定
    ############################
    def onFileOpen(self):
        select_path = askopenfilename()
        if not select_path:
            return
        elif select_path == self.file_path:
            if not (self.text_main.edit_modified() and
                    askokcancel('MyEdit',
                                'You have modified this file, discard changes and reopen it?')):
                return
        else:
            self.file_path = select_path
            self.label_path.config(text=self.file_path)
            self.label_path.update()
            self.text_main.delete(0.0, END)
            self.file_work = open(self.file_path, 'r')
            self.text_main.insert(0.0, self.file_work.read())
            self.file_work.close()
            self.text_main.edit_reset()

    def onFileSave(self):
        text_to_write = self.text_main.get(0.0, END)
        file_work = open(self.file_path, 'w')
        file_work.write(text_to_write)
        file_work.close()

    def onFileSaveAs(self):
        text_to_write = self.text_main.get(0.0, END)
        file_name = asksaveasfilename()
        with open(file_name, 'w') as file:
            file.write(text_to_write)

    def onFileNew(self):
        if self.text_main.edit_modified():
            if askokcancel('MyEdit', 'Discard all changes?'):
                self.text_main.delete(0.0, END)
                self.text_main.edit_reset()

    def onEditUndo(self):
        self.text_main.edit_undo()

    def onEditRedo(self):
        self.text_main.edit_redo()

    def onEditCut(self):
        try:
            text_select = self.text_main.get(SEL_FIRST, SEL_LAST)
            self.text_main.delete(SEL_FIRST, SEL_LAST)
            self.clip_board = [0, text_select]
        except TclError:
            pass

    def onEditPaste(self):
        try:
            if self.clip_board[0] == 0:
                self.text_main.insert(INSERT, self.clip_board[1])
                self.clip_board = []
            elif self.clip_board[0] == 1:
                self.text_main.insert(INSERT, self.clip_board[1])
        except IndexError:
            pass

    def onEditCopy(self):
        try:
            text_select = self.text_main.get(SEL_FIRST, SEL_LAST)
            self.clip_board = [1, text_select]
        except TclError:
            pass

    def onEditDelete(self):
        try:
            self.text_main.delete(SEL_FIRST, SEL_LAST)
        except TclError:
            pass

    def onEditSelectAll(self):
        self.text_main.tag_add(SEL, 0.0, END)

    def onSearchGoto(self):
        line_num = askinteger('MyEdit', 'Enter line number:')
        self.text_main.tag_remove(SEL, '0.0', END)
        self.text_main.mark_set(INSERT, '%d.0' % line_num)
        self.text_main.see(INSERT)
        self.text_main.tag_add(SEL, '%d.0' % line_num, '%d.end' % line_num)

    def onSearchFind(self, text=None):
        self.find_text = text or askstring('MyEdit', 'Input the context:')
        if self.find_text:
            result = self.text_main.search(self.find_text, INSERT, END)
            if result:
                self.text_main.tag_remove(SEL, '0.0', END)
                self.text_main.mark_set(INSERT, result + '+%dc' % len(self.find_text))
                self.text_main.tag_add(SEL, result, result + '+%dc' % len(self.find_text))
                self.text_main.see(INSERT)

    def onSearchRefind(self):
        if self.find_text:
            self.onSearchFind(text=self.find_text)
        else:
            self.onSearchFind()

    def onSearchChange(self):
        win = Toplevel(self.main)
        win.title('MyEdit - Change')
        items = [('Find text:', 'Find', lambda: None),
                 ('Change to:', 'Apply', lambda: None)]
        for item in items:
            frm = Frame(win)
            frm.pack(side=TOP, fill=X, anchor=N)
            lbl = Label(frm, text=item[0], height=1)
            lbl.pack(side=LEFT, anchor=NW)
            btn = Button(frm, text=item[1], command=item[2], height=1)
            btn.pack(side=RIGHT, anchor=NE)
            txt = Text(frm, height=1, width=20)
            txt.pack(side=LEFT, anchor=N, fill=X)

    ############################
    # 额外信息显示
    ############################

    def help(self):
        showinfo('Help Info', helptext)







if __name__ == '__main__':
    TextEditorMainFrame()
    mainloop()