# e.g. 9-27

from tkinter import *
import random


class Alarm(Frame):
    def __init__(self, msecs=1000, colors=[]):
        Frame.__init__(self)
        self.msecs = msecs
        self.colors = colors
        self.pack()
        stopper = Button(self, text='Stop the beeps!', command=self.quit)
        stopper.pack()
        stopper.config(bg='navy', fg='white', bd=8)
        #lab = Label(self, text='Hello there!', bd=15)
        #lab.pack()
        self.stopper = stopper
        self.repeater()

    def repeater(self):
        self.bell()
        """
        if self.colors:
            colorset = random.choice(self.colors), random.choice(self.colors)
            self.flasher.config(bg=colorset[0], fg=colorset[1])
        """
        self.stopper.flash()
        self.after(self.msecs, self.repeater)

if __name__ == '__main__':
    #colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
    Alarm().mainloop()