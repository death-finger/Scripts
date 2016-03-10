# e.g. 9-29

from tkinter import *
import alarm


class Alarm(alarm.Alarm):
    def reperter(self):
        self.bell()
        if self.master.state() == 'normal':
            self.master.iconify()
        else:
            self.master.deiconify()
            self.master.lift()
        self.after(self.msecs, self.reperter)

if __name__ == '__main__':
    Alarm().mainloop()