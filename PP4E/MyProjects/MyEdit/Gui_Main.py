# -*- coding:utf-8 -*-
"""
########################################################################
主窗口，包含主框架 > 菜单栏 > 文件名栏 > 文本框/YScrollBar > XScrollBar >
状态栏(Save/Cut/Copy/Paste/Find > Quit/Help)
########################################################################
"""

# 导入通用组件

from tkinter import *
import sys, os, glob, subprocess

# 导入Menu和Toolbar所需组件
from makeMenuToolBar import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, askokcancel, showerror
from tkinter.simpledialog import askinteger, askstring
from tkinter.colorchooser import askcolor
import random


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
        self.file_path = 'Welcome! \t|3Wrap: None'
        self.clip_board = []
        self.find_text = ""
        self.text_wrap = True

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
                                       ('Grep...', 0, self.onSearchGrep)]),
                        ('Tools', 0, [('Pick Font...', 0, self.onToolsPickFont),
                                      ('Font List', 0, self.onToolsFontList),
                                      ('Line Wrap', 0, self.onToolsLinewrap),
                                      'separator',
                                      ('Pick Bg...', 5, self.onToolsPickBg),
                                      ('Pick Fg...', 5, self.onToolsPickFg),
                                      ('Color List', 0, self.onToolsColorList),
                                      'separator',
                                      ('Info...', 0, self.onToolsInfo),
                                      ('Clone', 0, self.onToolsClone),
                                      ('Run Code', 0, self.onToolsRunCode)])]

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
        label_path.config(fg='white', bg='black', font=('times', 10, 'normal'))
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
                self.text_main.focus_set()
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
        # 创建窗口
        win = Toplevel(self.main)
        win.title('MyEdit - Change')
        lab_items = ({'text':'Find text:', 'relief':GROOVE, 'width':15},
                     {'text':'Change to:', 'relief':GROOVE, 'width':15})
        row = 0
        for item in lab_items:
            lbl = Label(win, **item)
            lbl.grid(row=row, column=0, sticky=EW)
            row += 1
        txt_find = makeEntryGrid(win, 0)
        txt_change = makeEntryGrid(win, 1)

        btn_find = Button(win, text='Find', relief=RAISED, width=7)
        btn_find.config(command=lambda: self.onSearchChange_findtext(txt_find))
        btn_find.grid(row=0, column=2, sticky=W)
        btn_change = Button(win, text='Apply', relief=RAISED, width=7)
        btn_change.config(command=lambda: self.onSearchChange_changetext(txt_change))
        btn_change.grid(row=1, column=2, sticky=W)

        win.columnconfigure(1, weight=10)
        win.focus_set()
        self.find_text = ''

    # 从输入框获取数据
    def onSearchChange_findtext(self, parent):
        find = parent.get()
        if not find:
            self.onSearchFind()
        else:
            self.onSearchFind(find)

    def onSearchChange_changetext(self, parent):
        text_change = parent.get()
        if text_change and self.find_text:
            #text_change = text_change.rstrip()
            self.text_main.delete(SEL_FIRST, SEL_LAST)
            self.text_main.insert(INSERT, text_change)
            self.onSearchRefind()

    def onSearchGrep(self):
        win = Toplevel(self.main)
        win.title('MyEdit - Grep')
        lab_items = ['Directory root:', 'Filename pattern:', 'Search string', 'Content encoding:']
        row = 0
        for item in lab_items:
            lab = Label(win, text=item, relief=GROOVE, width=15)
            lab.grid(row=row, column=0, sticky=W)
            row += 1
        dir_root_txt = makeEntryGrid(win, 0)
        dir_root_txt.insert(0, '.')
        file_patt_txt = makeEntryGrid(win, 1)
        file_patt_txt.insert(0, '*.py')
        search_str_txt = makeEntryGrid(win, 2)
        content_enc_txt = makeEntryGrid(win, 3)
        content_enc_txt.insert(0, 'utf-8')
        win.columnconfigure(1, weight=10)
        btn_go = Button(win, text='Go', height=1, relief=RAISED, width=10)
        btn_go.config(command=lambda: self.onSearchGrep_func(win, dir_root_txt.get(), file_patt_txt.get(),
                                                             search_str_txt.get(), content_enc_txt.get()))
        btn_go.grid(row=4, column=1, sticky=E)

    def onSearchGrep_func(self, parent, dir_root, file_patt, search_str, cont_coding):
        file_find = []
        file_patt = file_patt or '*'
        dir_to_search = os.path.join(os.path.abspath(dir_root), file_patt)
        if os.path.exists(dir_root):
            if search_str:
                items = glob.glob(dir_to_search)
                for item in items:
                    with open(item, 'r', encoding=cont_coding) as file:
                        file_lines = file.readlines()
                        for line in file_lines:
                            if search_str in line:
                                file_find.append((item, file_lines.index(line), line))
            else:
                showerror('MyEdit', 'Please input search string')
        else:
            showerror('MyEdit', 'Directory not exist')

        if file_find:
            win_res = Toplevel(parent)
            win_res.title('PyEdit - grep matched:"%s"' % search_str)
            scl = Scrollbar(win_res)
            list = Listbox(win_res, width=50, height=20)
            scl.config(command=list.yview)
            list.config(yscrollcommand=scl.set)
            scl.pack(side=RIGHT, fill=Y)
            for result in file_find:
                list.insert(END, '=>%s | @%d [%s]' %(result[0], result[1], result[2]))
            list.pack(side=LEFT, expand=YES, fill=BOTH)
        else:
            showinfo('MyEdit', 'No file find!')

    def onToolsPickFont(self):
        win = Toplevel(self.main)
        lbl_items = ('Family:', 'Size:', 'Style:')
        row = 0
        for item in lbl_items:
            lbl = Label(win, text=item, relief=GROOVE, width=15)
            lbl.grid(row=row, column=0, sticky=EW)
            row += 1
        ent_family = makeEntryGrid(win, 0)
        ent_family.insert(0, 'courier')
        ent_size = makeEntryGrid(win, 1)
        ent_size.insert(0, 12)
        ent_style = makeEntryGrid(win, 2)
        ent_style.insert(0, 'bold italic')
        btn_apply = Button(win, text='Apply', relief=RAISED, width=10)
        btn_apply.config(command=lambda: self.onToolsPickFont_Apply(ent_family.get(),
                                                                    ent_size.get(),
                                                                    ent_style.get()))
        btn_apply.grid(row=3, column=1, sticky=E)
        win.columnconfigure(1, weight=10)

    def onToolsPickFont_Apply(self, family, size, style):
        if family and size and style:
            font = (family, size, style)
            self.text_main.config(font=font)
            self.text_main.update()
        else:
            showerror('MyEdit', 'Please choose the right font!')

    def onToolsFontList(self):
        font_path = ''
        font_list = []
        if sys.platform[:3] == 'win':
            font_path = r'C:\Windows\Fonts'
        elif sys.platform == 'darwin':
            font_path = '/Library/Fonts'
        if font_path:
            font_list = os.listdir(font_path)
        win = Toplevel(self.main)
        frm1 = Frame(win)
        frm1.pack(side=LEFT, fill=Y)
        family = Listbox(frm1, width=15, height=5)
        family.pack(side=TOP, anchor=NW)
        for font in font_list:
            family.insert(END, font[:-4])

        frm2 = Frame(win)
        frm2.pack(side=LEFT, fill=Y)
        lab_size = Label(frm2, text='Size:', width=6, height=1)
        lab_size.grid(row=0, column=0, sticky=NSEW)
        ent_size = Entry(frm2, width=10)
        ent_size.grid(row=0, column=1, sticky=EW)
        ent_size.insert(0, 12)
        lab_style = Label(frm2, text='Style:', width=6, height=1)
        lab_style.grid(row=1, column=0, sticky=NSEW)
        chk_normal = Checkbutton(frm2, text='Normal')
        chk_normal.grid(row=1, column=1, sticky=NSEW)
        chk_bold = Checkbutton(frm2, text='Bold')
        chk_bold.grid(row=2, column=0, sticky=NSEW)
        chk_italic = Checkbutton(frm2, text='Italic')
        chk_italic.grid(row=2, column=1, sticky=NSEW)
        style_var = []
        for chkbtn in (chk_normal, chk_bold, chk_italic):
            var = IntVar()
            chkbtn.config(variable=var)
            style_var.append(var)
        btn_ok = Button(frm2, text='Apply')
        btn_ok.config(command=lambda: self.onToolsFontList_Apply(family.get(family.curselection()), ent_size.get(), style_var))
        btn_ok.grid(row=3, column=0 ,sticky=NSEW)
        btn_cancel = Button(frm2, text='cancel', command=win.destroy)
        btn_cancel.grid(row=3, column=1)

    def onToolsFontList_Apply(self, family, size, styles):
        style = ''
        if styles[0].get():
            style = 'normal'
        else:
            if styles[1].get():
                style += 'bold'
            elif styles[2].get():
                style += 'italic'
        font = (family, size, style)
        self.text_main.config(font = font)
        self.text_main.update()

    def onToolsLinewrap(self):
        if self.text_wrap:
            self.text_main.config(wrap=WORD)
            self.label_path.config(text=self.file_path + '\t|Wrap: Word')
        else:
            self.text_main.config(wrap=NONE)
            self.label_path.config(text=self.file_path + '\t|Wrap: None')
        self.text_main.update()
        self.label_path.update()
        self.text_wrap = not self.text_wrap

    def onToolsPickBg(self):
        bg_color = askcolor()
        if bg_color:
            self.text_main.config(bg=bg_color[1])
            self.text_main.update()

    def onToolsPickFg(self):
        fg_color = askcolor()
        if fg_color:
            self.text_main.config(fg=fg_color[1])
            self.text_main.update()

    def onToolsColorList(self):
        bg_color = random.randrange(256), random.randrange(256), random.randrange(256)
        fg_color = random.randrange(256), random.randrange(256), random.randrange(256)
        self.text_main.config(bg='#%02x%02x%02x'%bg_color, fg='#%02x%02x%02x'%fg_color)
        self.text_main.update()

    def onToolsInfo(self):
        result = []
        index = self.text_main.index(INSERT).split('.')
        for i in index:
            result.append(int(i))
        context = self.text_main.get(0.0, END)
        chars = 0
        for i in context:
            chars += 1
        result.append(chars)
        lines = 0
        for i in context.split('\n'):
            lines += 1
        result.append(lines)
        words = 0
        for i in context.split():
            words += 1
        result.append(words)
        info = """
        Current location

        line: %d
        column: %d

        File text statistics:

        chars: %d
        lines: %d
        words: %d
        """ % tuple(result)
        showinfo('MyEdit Information', info)

    def onToolsClone(self):
        myclass = self.__class__
        myclass()

    def onToolsRunCode(self):
        temp = open('temp', 'wb')
        data = self.text_main.get(0.0, END)
        temp.write(data.encode('utf-8'))
        temp.flush()
        tmp_path = 'python ' + os.path.abspath('temp')
        subprocess.Popen(tmp_path, shell=True)










    ############################
    # 额外信息显示
    ############################

    def help(self):
        showinfo('Help Info', helptext)


# 主体框架中,构建弹出窗口的Text框
class makeEntryGrid(Entry):
    def __init__(self, parent, row, column=1, sticky=EW):
        Entry.__init__(self, parent)
        self.grid(row=row,column=column, sticky=sticky)


if __name__ == '__main__':
    class Test(TextEditorMainFrame):
        def __init__(self):
            TextEditorMainFrame.__init__(self)
            if os.path.exists(r'G:\PythonScripts\PP4E-Examples-1.4\Examples\PP4E\launchmodes.py'):
                self.file_path = r'G:\PythonScripts\PP4E-Examples-1.4\Examples\PP4E\launchmodes.py'
            elif os.path.exists('/Users/joshuapu/Documents/Scripts/PP4E/launchmodes.py'):
                self.file_path = '/Users/joshuapu/Documents/Scripts/PP4E/launchmodes.py'
            else:
                self.file_path = r'C:\Users\joshuap\Desktop\Scripts\PP4E\launchmodes.py'
            self.opentest()
        def opentest(self):
            self.label_path.config(text=self.file_path+'\t|Wrap: None')
            self.label_path.update()
            self.text_main.delete(0.0, END)
            self.file_work = open(self.file_path, 'r')
            self.text_main.insert(0.0, self.file_work.read())
            self.file_work.close()
            self.text_main.edit_reset()
    Test()
    mainloop()