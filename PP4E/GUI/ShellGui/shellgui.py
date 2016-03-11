#!/usr/local/bin/python
"""
e.g. 10-5
##########################################################################
工具启动器, 使用guimaker模板, guimixin标准quit对话框; 本程序只是一个类库, 要显示
图形界面, 请运行mytools脚本
##########################################################################
"""

from tkinter import *
from PP4E.GUI.Tools.guimixin import GuiMixin
from PP4E.GUI.Tools.guimaker import *


class ShellGui(GuiMixin, GuiMakerWindowMenu):
    def start(self):
        self.setMenuBar()
        self.setToolBar()
        self.master.title('Shell Tools Listbox')
        self.master.iconname('Shell Tools')

    def handleList(self, event):
        label = self.listbox.get(ACTIVE)
        self.runCommand(label)

    def makeWidgets(self):
        sbar = Scrollbar(self)
        list = Listbox(self, bg='white')
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        for (label, action) in self.fetchCommands():
            list.insert(END, label)
        list.bind('<Double-1>', self.handleList)
        self.listbox = list

    def forToolBar(self, label):
        return True

    def setToolBar(self):
        self.toolBar = []
        for (label, action) in self.fetchCommands():
            if self.forToolBar(label):
                self.toolBar.append(('Quit', self.quit, dict(side=RIGHT)))

    def setMenuBar(self):
        toolEntries = []
        self.menuBar = [('File', 0, [('Quit', 0, self.quit),
                                     ('Tools', 0, toolEntries)])]
        for (label, action) in self.fetchCommands():
            toolEntries.append(label, -1, action)


##########################################################################
# 针对特定模板类型的子类而设计, 后者又针对特定应用工具集的子类而设计
##########################################################################

class ListMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu

    def runCommand(self, cmd):
        for (label, action) in self.myMenu:
            if label == cmd:
                action()


class DictMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu.items()

    def runCommand(self):
        self.myMenu[cmd]()

