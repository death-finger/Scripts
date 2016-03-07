# e.g. 8-31

from tkinter import *


root = Tk()
scl = Scale(root, from_=0, to=1000, tickinterval=0, resolution=1)
scl.pack(expand=YES, fill=Y)

def report():
    print(scl.get())

Button(root, text='State', command=report).pack(side=RIGHT)
root.mainloop()
