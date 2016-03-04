# e.g. 8-23

from tkinter import *


states = []
def onPress(i):
    states[i] = not states[i]

root = Tk()
for i in range(10):
    chk = Checkbutton(root, text=str(i), command=(lambda i=i: onPress(i)))
    chk.pack(side=LEFT)
    states.append(False)

root.mainloop()
print(states)
