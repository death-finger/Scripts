# e.g. 8-1

from tkinter import *

root = Tk()
labelfont = ('times', 20, 'bold')
widget = Label(root, text='Hello config world')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
