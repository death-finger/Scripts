# e.g. 7-21

from sys import exit
from tkinter import *
from gui6 import Hello


parent = Frame(None)
parent.pack()
Hello(parent).pack(side=RIGHT)
Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
