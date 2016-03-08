# e.g. 9-7

from tkinter import *


root = Tk()
var1 = StringVar()
var2 = StringVar()
opt1 = OptionMenu(root, var1, 'spam', 'eggs', 'toast')
opt2 = OptionMenu(root, var2, 'ham', 'bacon', 'sausage')
opt1.pack(fill=X)
opt2.pack(fill=X)
var1.set('spam')
var2.set('ham')

def state(): print(var1.get(), var2.get())
Button(root, command=state, text='State').pack()
root.mainloop()
