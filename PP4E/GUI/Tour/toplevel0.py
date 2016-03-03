# e.g. 8-3

import sys
from tkinter import Toplevel, Button, Label


win1 = Toplevel()
win2 = Toplevel()

Button(win1, text='Spam1', command=sys.exit).pack()
Button(win2, text='Spam2', command=sys.exit).pack()

Label(text='Popups').pack()
win1.mainloop()
