# e.g. 10-10

from glob import glob
from tkinter import *
from packer import pack
from formrows import makeFormRow


def packDialog():
    win = Toplevel()
    win.title('Enter Pack Parameters')
    var1 = makeFormRow(win, label='Output file')
    var2 = makeFormRow(win, label='Files to pack', extend=True)
    Button(win, text='OK', command=win.destroy).pack()
    win.grab_set()
    win.focus_set()
    win.wait_window()
    return var1.get(), var2.get()

def runPackDialog():
    output, patterns = packDialog()
    if output != "" and patterns != "":
        patterns = patterns.split()
        filenames = []
        for sublist in map(glob, patterns):
            filenames += sublist
        print('Packer:', output, filenames)
        pack(ofile=output, ifiles=filenames)


if __name__ == '__main__':
    root = Tk()
    Button(root, text='popup', command=runPackDialog).pack(fill=X)
    Button(root, text='bye', command=root.quit).pack(fill=X)
    root.mainloop()
