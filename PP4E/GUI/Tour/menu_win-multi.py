# e.g. 9-2

from menu_win import makemenu
from tkinter import *


root = Tk()
for i in range(3):
    win = Toplevel(root)
    makemenu(win)
    Label(win, bg='black', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text='Bye', command=root.quit).pack()
root.mainloop()
