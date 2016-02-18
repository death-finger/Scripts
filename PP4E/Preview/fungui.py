# extra example

from tkinter import *
import random
fontsize = 30
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'purple']
color = random.choice(colors)

def onSpam():
    popup = Toplevel()
    Label(popup, text='Popup', bg='black', fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)

def onFlip():
    mainLabel.config(fg=color)
    main.after(250, onFlip)

def onGrow():
    global fontsize
    fontsize += 1
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(500, onGrow)

main = Tk()
mainLabel = Label(main, text='Fun Gui!', relief=RAISED)
mainLabel.config(font=('arial', fontsize, 'italic'), fg='cyan', bg='navy')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text='spam', command=onSpam).pack(fill=X)
Button(main, text='flip', command=onFlip).pack(fill=X)
Button(main, text='onGrow', command=onGrow()).pack(fill=X)
main.mainloop()

