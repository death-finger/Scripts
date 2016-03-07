# e.g. 8-32

# 通用
from tkinter import *

# demoTable
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

# QuitBtn中的确认退出功能
from tkinter.messagebox import askokcancel



demoTable = {'Color': askcolor,
             'Query': (lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?')),
             'Input': (lambda: askfloat('Enrty', 'Enter credit card number')),
             'Open': askopenfile,
             'Error': (lambda: showerror('Error!', "He's dead, Jim"))}

demoModules = ['DemoDlg', 'DemoCheck', 'DemoRadio', 'DemoScale']
parts = []


# Quit按钮
class QuitBtn(Frame):
        def __init__(self, parent=None):
                Frame.__init__(self, parent)
                self.pack()
                widget = Button(self, text='Quit', command=self.quit)
                widget.pack(side=TOP, expand=YES, fill=BOTH)

        def quit(self):
                ans = askokcancel('Really?','Are you sure to quit?')
                if ans: Frame.quit(self)


class DemoDlg(Frame):
        def __init__(self, parent=None, **options):
                Frame.__init__(self, parent, **options)
                self.pack()
                Label(self, text='Basic demos').pack(side=TOP)
                self.makeWidgets()

        def makeWidgets(self):
                for (val, cmd) in demoTable.items():
                        btn = Button(self, text=val, command=cmd)
                        btn.pack(side=TOP)


class DemoCheck(Frame):
        def __init__(self, parent=None, **options):
                Frame.__init__(self, parent, **options)
                self.pack()
                Label(self, text='Check demos').pack(side=TOP)
                self.vars = []
                for (key, cmd) in demoTable.items():
                        var = IntVar()
                        chk = Checkbutton(self, text=key, command=cmd, variable=var)
                        chk.pack(side=LEFT, anchor='n')
                        self.vars.append(var)
                StateBtn = Button(self, text='State', command=self.state)
                StateBtn.pack(side=LEFT, anchor='n')

        def state(self):
                for var in self.vars:
                        print(var.get(), end=' ')
                print()


class DemoRadio(Frame):
        def __init__(self, parent=None, **options):
                Frame.__init__(self, parent, **options)
                self.pack()
                self.var = StringVar()
                for (val, cmd) in demoTable.items():
                        widget = Radiobutton(self, text=val, command=cmd, variable=self.var, value=val)
                        widget.pack(side=TOP)
                self.var.set(val)
                Button(self, text='State', command=self.state).pack(side=TOP, anchor='s')

        def state(self):
                print(self.var.get())


class DemoScale(Frame):
        def __init__(self, parent=None, **options):
                Frame.__init__(self, parent, **options)
                self.pack()
                Label(self, text='Scale demos').pack(side=TOP)
                self.var = IntVar()
                Scale(self, label='Pick demo number', from_=0, to=len(demoTable)-1,
                      variable=self.var).pack()
                Scale(self, label='Pick demo number', from_=0, to=len(demoTable)-1,
                      variable=self.var, length=200, orient=HORIZONTAL).pack()
                Button(self, text='Run demo', command=self.run_demo).pack(side=LEFT, anchor='sw')
                Button(self, text='State', command=self.state).pack(side=LEFT, anchor='s')

        def run_demo(self):
                num = self.var.get()
                run = list(demoTable.values())[num]
                print('Result:', run())

        def state(self):
                print(self.var.get())


def dumpState():
        for part in parts:
                print(part.__module__ + ':', end=' ')
                if hasattr(part, 'state'):
                        part.state()
                else:
                        print('None')

# 自动创建
def addComponents(root):
        for demo in demoModules:
                part = eval(demo)(root)
                part.pack(side=LEFT, expand=YES, fill=BOTH)
                part.config(bd=2, relief=GROOVE)
                parts.append(part)


# Test
if __name__ == '__main__':
        root = Tk()
        root.title('Frame')
        Label(root, text='Multiple Frame demo', bg='white').pack()
        Button(root, text='States', command=dumpState).pack(side=TOP, expand=YES, fill=X)
        QuitBtn(root).pack(side=TOP, expand=YES, fill=X)
        addComponents(root)

        root.mainloop()