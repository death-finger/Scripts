import getfile
from tkinter import *
from tkinter.messagebox import showinfo


def onSubmit():
    getfile.client(content['Server'].get(),
                   int(content['Port'].get()),
                   content['File'].get())
    showinfo('getfilegui-2', 'Download complete')

box = Tk()
labels = ['Server', 'Port', 'File']
rownum = 0
content = {}
for label in labels:
    Label(box, text=label).grid(row=rownum, column=0)
    entry = Entry(box)
    entry.grid(row=rownum, column=1, sticky=EW)
    content[label] = entry
    rownum += 1

box.columnconfigure(0, weight=0)
box.columnconfigure(1, weight=1)
Button(text='Submit', command=onSubmit).grid(row=rownum, column=0, columnspan=2)

box.title('getfilegui-2')
box.bind('<Return>', lambda event: onSubmit())
mainloop()