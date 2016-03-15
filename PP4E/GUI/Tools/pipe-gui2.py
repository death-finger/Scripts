# e.g. 10-28

from tkinter import *
from PP4E.GUI.Tools.guiStreams import redirectedGuiShellCmd


def launch():
    redirectedGuiShellCmd('python -u pipe-nongui.py')

window = Tk()
Button(window, text='GO!', command=launch).pack()
window.mainloop()