from tkinter import *


class MakeGui:
    menuBar = []
    helpButton = True

    def __init__(self, parent=None):
        self.start()
        self.makeMenuBar(parent, self.menuBar)

    def makeMenuBar(self, parent, menuBar):
        for (name, key, items) in menuBar:
            menu_main = Menu(parent)
            self.makeMenuItems(menu_main, items)
            parent.add_cascade(label=name, underline=key, menu=menu_main)

        if self.helpButton:
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
                self.makeMenuBar(sub_name, item)

    def help(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError


if __name__ == '__main__':
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    from tkinter.messagebox import showinfo

    menuBar = [('File', 0, [('Open...', 0, askopenfilename),
                                     ('Save', 0, lambda: None),
                                     ('Save As...', 5, asksaveasfilename),
                                     ('New', 0, lambda: None),
                                     'separator',
                                     ('Quit', 0, sys.exit),
                                     [1, 3]]),
                        ('Edit', 0, [('Undo', 0, lambda: None),
                                     ('Redo', 0, lambda: None),
                                     'separator',
                                     ('Cut', 0, lambda: None),
                                     ('Copy', 0, lambda: None),
                                     ('Paste', 0, lambda: None),
                                     'separator',
                                     ('Delete', 0, lambda: None),
                                     ('Select All', 7, lambda: None),
                                     [0, 1, 2, 3, 4, 5, 6]]),
                        ('Search', 0, [('Goto...', 0, lambda: None),
                                       ('Find...', 0, lambda: None),
                                       ('Refind', 0, lambda: None),
                                       ('Change...', 0, lambda: None),
                                       ('Grep...', 0, lambda: None),
                                       [0, 1, 2, 3, 4]]),
                        ('Tools', 0, [('Pick Font...', 0, lambda: None),
                                      ('Font List', 0, lambda: None),
                                      'separator',
                                      ('Pick Bg...', 5, lambda: None),
                                      ('Pick Fg...', 5, lambda: None),
                                      ('Color List', 0, lambda: None),
                                      'separator',
                                      ('Info...', 0, lambda: None),
                                      ('Clone', 0, lambda: None),
                                      ('Run Code', 0, lambda: None),
                                      [0, 1, 2, 3, 4, 5, 6, 7]])]

    class Test(MakeGui):
        def start(self):
            self.menuBar = menuBar
        def help(self):
            showinfo('Help Info', 'No help offered!')

    root = Tk()
    top = Menu(root)
    root.config(menu=top)
    Test(top)
    mainloop()
