# e.g. 10-21

import time
from threadtools import threadChecker, startThread
from tkinter.scrolledtext import ScrolledText


class MyGUI:
    def __init__(self, reps=3):
        self.reps = reps
        self.text = ScrolledText()
        self.text.pack()
        threadChecker(self.text)
        self.text.bind('<Button-1>',
                       lambda event: list(map(self.onEvent, range(6))))

    def onEvent(self, i):
        myname = 'thread-%s' % i
        startThread(action=self.threadaction, args=(i, ),
                    context=(myname,), onExit=self.threadexit,
                    onFail=self.threadfail, onProgress=self.threadprogress)

    def threadaction(self, id, progress):
        for i in range(self.reps):
            time.sleep(1)
            if progress: progress(i)
        if id % 2 == 1: raise Exception

    def threadexit(self, myname):
        self.text.insert('end', '%s\texit\n' % myname)
        self.text.see('end')

    def threadfail(self, exc_info, myname):
        self.text.insert('end', '%s\tfail\t%s\n' % (myname, exc_info[0]))
        self.text.see('end')
    def threadprogress(self, count, myname):
        self.text.insert('end', '%s\tprog\t%s\n' % (myname, count))
        self.text.see('end')
        self.text.update()


if __name__ == '__main__':
    MyGUI().text.mainloop()

