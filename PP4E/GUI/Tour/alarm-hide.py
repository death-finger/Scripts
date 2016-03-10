# e.g. 9-28

from tkinter import *
import alarm


class Alarm(alarm.Alarm):
    def __init__(self, msecs=1000):
        self.shown = False
        alarm.Alarm.__init__(self, msecs)

    def repeater(self):
        self.bell()
        if self.shown:
            self.stopper.pack_forget()
        else:
            self.stopper.pack()
        self.shown = not self.shown
        self.after(self.msecs, self.repeater)

if __name__ == '__main__':
    Alarm(msecs=500).mainloop()
