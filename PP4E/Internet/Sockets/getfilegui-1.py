# e.g. 12-18

import sys, os
from tkinter import *
from tkinter.messagebox import showinfo


def onReturnKey():
    cmdline = ('python getfile.py -mode client -file %s -port %s -host %s' %
               (content['File'].get(),
                content['Port'].get(),
                content['Server'].get()))
    os.system(cmdline)
    showinfo('getfilegui-1', 'Download Complete')


box = Tk()
labels = ['Server', 'Port', 'File']
content = {}
for label in labels:
    row = Frame(box)
    row.pack(fill=X)
    Label(row, text=label, width=6).pack(side=LEFT)
    entry = Entry(row)
    entry.pack(side=RIGHT, expand=YES, fill=X)
    content[label] = entry

box.title('getfilegui-1')
box.bind('<Return>', lambda event: onReturnKey())
mainloop()