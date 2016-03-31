from tkinter import *
import time
countdown = 5

root = Tk()
frm = Frame(root)
frm.pack(side=TOP, expand=YES, fill=BOTH)
lab = Label(frm)
lab.pack()

def timer():
    global countdown
    if countdown >= 0:
        lab.config(text=countdown)
        countdown -= 1
        lab.update()
        root.after(1000, timer)
    else:
        lab.config(text='Ends!!!')



timer()
mainloop()