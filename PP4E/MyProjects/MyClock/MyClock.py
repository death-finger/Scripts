from tkinter import *
import math, time


points = 60
radius = 400 / 2
centX = centY = 400 / 2 + 50
degree = 6 * math.pi / 180


class MainFrame(Frame):
    left = True
    right = False

    def __init__(self, parent=None, size=400):
        self.size = size
        Frame.__init__(self, parent)
        self.pack(side=TOP, fill=BOTH, expand=YES)
        self.makeCanvas()
        self.bindFunc()
        self.timeFlies()

    def makeCanvas(self):
        self.canv = Canvas(self, width=self.size+100, height=self.size+100)
        self.canv.pack(side=TOP, fill=BOTH, expand=YES)
        bg = 'red'
        for point in range(points):
            dot_len = 3
            if point % 5: dot_len = 1
            X = radius * (1 + math.sin(degree * point)) + 50
            Y = radius * (1 - math.cos(degree * point)) + 50
            self.canv.create_rectangle(X-dot_len, Y-dot_len, X+dot_len, Y+dot_len, fill=bg)

    def timeFlies(self):
        timeTuple = time.localtime(time.time())
        hours, mins, secs = timeTuple[3:6]
        hours = hours + mins / 60
        mins = mins + secs / 60
        self.canv.delete('hours', 'mins', 'secs')
        X_h = 200 + 0.75 * radius * math.sin(degree * hours * 5) + 50
        Y_h = 200 - 0.75 * radius * math.cos(degree * hours * 5) + 50
        X_m = 200 + 0.85 * radius * math.sin(degree * mins) + 50
        Y_m = 200 - 0.85 * radius * math.cos(degree * mins) + 50
        X_s = 200 + radius * math.sin(degree * secs) + 50
        Y_s = 200 - radius * math.cos(degree * secs) + 50
        self.canv.create_line(centX, centY, X_h, Y_h, arrow=LAST, width=8, fill='red', tags='hours')
        self.canv.create_line(centX, centY, X_m, Y_m, arrow=LAST, width=4, fill='cyan', tags='mins')
        self.canv.create_line(centX, centY, X_s, Y_s, arrow=LAST, width=1, fill='grey', tags='secs')
        self.canv.create_oval(centX-10, centY-10, centX+10, centY+10, fill='black')
        self.canv.after(200, self.timeFlies)

    def bindFunc(self):
        self.bind_all('<Button-1>', self.onLeftClick)
        self.canv.bind('<Button-3>', self.onRightClick)

    def onLeftClick(self, event):
        self.left = not self.left
        if not self.left:
            self.canv.forget()
            self.drawDigitClock()
        else:
            self.frm.forget()
            self.makeCanvas()
            self.timeFlies()

    def drawDigitClock(self):
        self.frm = Frame(self)
        self.frm.pack(side=TOP, expand=YES, fill=BOTH)
        self.digitTimeFlies()

    def digitTimeFlies(self):
        hours, mins, secs = time.localtime(time.time())[3:6]
        col = 0
        for i in hours, mins, secs:
            lab = Label(self.frm, text=i, width=20, height=1, relief=SUNKEN, bd=2)
            lab.grid(row=0, column=col)
            col += 1
        self.after(200, self.digitTimeFlies)

    def onRightClick(self):
        pass





if __name__ == '__main__':
    MainFrame().mainloop()