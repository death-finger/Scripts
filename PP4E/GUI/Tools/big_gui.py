# e.g. 10-4

import sys, os
from PP4E.GUI.Tools.guimixin import *
from PP4E.GUI.Tools.guimaker import *

class Hello(GuiMixin, GuiMakerWindowMenu):
    def start(self):
        self.hellos = 0
        self.master.title('GuiMaker Demo')
        self.master.iconname('GuiMaker')
        def spawnme():
            self.spawn('big_gui.py')

        self.menuBar = [
            ('File', 0, [('New...', 0, spawnme),
                         ('Open...', 0, self.fileOpen),
                         ('Quit', 0, self.quit)]),
            ('Edit', 0, [('Cut', -1, self.notdone),
                         ('Paste', -1, self.notdone),
                         'separator',
                         ('Stuff', -1, [('Clone', -1, self.clone),
                                        ('More', -1, self.more)]),
                         ('Delete', -1, lambda: 0),
                         [5]]),
            ('Play', 0, [('Hello', 0, self.greeting),
                         ('Popup...', 0, self.dialog),
                         ('Demos', 0, [('Toplevels', 0, lambda: self.spawn(r'../Tour/toplevel2.py')),
                                       ('Frames', 0, lambda: self.spawn(r'../Tour/demoAll-frm-ridge.py')),
                                       ('Images', 0, lambda: self.spawn(r'../Tour/buttonpics.py')),
                                       ('Alarm', 0, lambda: self.spawn(r'../Tour/alarm.py', wait=False)),
                                       ('Other', -1, self.pickDemo)])])]

        self.toolBar = [
            ('Quit', self.quit, dict(side=RIGHT)),
            ('Hello', self.greeting, dict(side=LEFT)),
            ('Popup', self.dialog, dict(side=LEFT, expand=YES))]

    def makeWidgets(self):
        middle = Label(self, text='Hello maker world!', width=40, height=10,
                       relief=SUNKEN, cursor='pencil', bg='white')
        middle.pack(expand=YES, fill=BOTH)

    def greeting(self):
        self.hellos += 1
        if self.hellos % 3:
            print('hi')
        else:
            self.infobox('Three', 'HELLO!')

    def dialog(self):
        button = self.question('OOPS!',
                               'You typed "rm*" ... continue?',
                               'questhead', ('yes', 'no'))
        [lambda: None, self.quit][button]()

    def fileOpen(self):
        pick = self.selectOpenFile(file='big_gui.py')
        if pick:
            self.browser(pick)

    def more(self):
        new = Toplevel()
        Label(new, text='A new non-modal window').pack()
        Button(new, text='Quit', command=self.quit).pack(side=LEFT)
        Button(new, text='More', command=self.more).pack(side=RIGHT)

    def pickDemo(self):
        pick = self.selectOpenFile(dir='..')
        if pick:
            self.spawn(pick)

if __name__ == '__main__':
    Hello().mainloop()
