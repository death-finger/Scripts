from tkinter import *
from tkinter.ttk import *

class makeGui():
    menuBar = []
    def __init__(self, parent=None):
        self.makeMenuBar(parent, self.menuBar)

    def makeMenuBar(self, parent, menulist):
        for (name, key, items) in menulist:
            name = Menu(parent)
            self.makeMenuItems(name, items)
            parent.add_cascade(label=name, underline=key, menu=name)

    def makeMenuItems(self, name, items):
        for item in items:
            if item == 'separator':
                name.add_separator()
            elif type(item) == list:
                for num in item:
                    name.entryconfig(num, status=DISABLED)
            elif  type(item[2]) != list:
                name.add_command(label=item[0],
                                 underline=item[1],
                                 command=item[2])
            else:
                sub_name = Menu(name)
                self.makeMenuBar(sub_name, item)

    def start(self):
        raise NotImplementedError


if __name__ == '__main__':
    menuBar = [('File', 0, [('Open', 0, lambda: 0), ('Quit', 0, sys.exit)]),
               ('Edit', 0, [('Cut', 0, lambda: 0), ('Paste', 0, lambda: 0)])]

    class Test(makeGui):
        def start(self):
            self.menuBar = menuBar

    root = Tk()
    Test(root)
    mainloop()