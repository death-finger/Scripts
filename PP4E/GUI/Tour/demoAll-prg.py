# e.g. 8-34

from tkinter import *
from PP4E.launchmodes import PortableLauncher
import os, sys


demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

for demo in demoModules:
    pid = os.fork()
    filepath = './' + demo + '.py'
    if pid == 0:
        os.execvp('python3.5', (filepath, ))

root = Tk()
root.title('Progress')
Label(root, text='Multiple program demo: command lines', bg='white').pack()
root.mainloop()
