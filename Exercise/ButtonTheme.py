from tkinter import *

root = Tk()
font = ('times', 25, 'italic underline')
widget = Label(root, text='Color test', bg='red', fg='white')
widget.pack()
#widget.config(bg='red', fg='white')
#widget.config(font=font)
root.mainloop()