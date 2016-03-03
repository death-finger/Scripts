# e.g. 7-25

from tkinter import *
from gui7 import HelloPackage


frm = Frame()
frm.pack()
Label(frm, text='hello').pack()

part = HelloPackage(frm)
part.top.pack(side=RIGHT)
frm.mainloop()
