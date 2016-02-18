from tkinter import *

def onPress():
    popup = Toplevel()
    color = 'yellow'
    Label(popup, text='Wow~~').pack()



main = Tk()
mainLabel = Label(main, text="It's my first GUI")
mainLabel.config(font=('arial', 15, 'italic'), fg='red', bg='green')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text='Press', command=onPress).pack(side=LEFT)

mainloop()