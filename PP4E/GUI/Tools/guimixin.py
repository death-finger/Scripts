# e.g. 10-2

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from PP4E.GUI.Tour.scrolledtext import ScrolledText
from PP4E.launchmodes import PortableLauncher, System


class GuiMixin:
    def infobox(self, title, text, *args):
        return showinfo(title, text)

    def errorbox(self, text):
        showerror('Error!', text)

    def question(self, title, text, *args):
        return askyesno(title, text)

    def notdone(self):
        showerror('Not Implemented', 'Option not available yet...')

    def quit(self):
        ans = self.question('Verify Quit', 'Are you sure to quit?')
        if ans: Frame.quit(self)

    # Need to be customized
    def help(self):
        self.infobox('RTFM', 'See figure 1...')

    def selectOpenFile(self, file='', dir='.'):
        return askopenfilename(initialdir=dir, initialfile=file)

    def selectSaveFile(self, file='', dir='.'):
        return asksaveasfilename(initialdir=dir, initialfile=file)

    def clone(self, args=()):
        new = Toplevel()
        myclass = self.__class__
        myclass(new, *args)

    def spawn(self, pycmdline, wait=FALSE):
        if not wait:
            PortableLauncher(pycmdline, pycmdline)()
        else:
            System(pycmdline, pycmdline)()

    def browser(self, filename):
        new = Toplevel()
        view = ScrolledText(new, file=filename)
        view.text.config(height=30, width=85)
        view.text.config(font=('courier', 12, 'normal'))
        new.title('Text viewer')
        new.iconname('browser')


if __name__ == '__main__':
    class TestMixin(GuiMixin, Frame):
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            self.pack()
            Button(self, text='quit', command=self.quit).pack(fill=X)
            Button(self, text='help', command=self.help).pack(fill=X)
            Button(self, text='clone', command=self.clone).pack(fill=X)
            Button(self, text='spawn', command=self.spawn).pack(fill=X)
        def other(self):
            self.spawn('guimixin.py')

    TestMixin().mainloop()