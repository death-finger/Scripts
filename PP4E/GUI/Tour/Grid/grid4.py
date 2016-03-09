# e.g. 9-23

from tkinter import *

for i in range(5):
    for j in range(4):
        lab = Label(text='%d.%d' %(i, j), relief=RIDGE)
        lab.grid(row=i, column=j, sticky=NSEW)


mainloop()
