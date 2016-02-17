from tkinter import *
from tkinter102 import MyGui


# Apply to main window
mainwin = Tk()
Label(mainwin,text=__name__).pack()

# pop-up window
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()

