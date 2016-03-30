# e.g. 11-11

import math, sys, time
from tkinter import *

def point(tick, range, radius):
    angle = tick * (360 / range)
    radiansPerDegree = math.pi / 180
    pointX = int( round( radius * math.sin(angle * radiansPerDegree) ))
    pointY = int( round( radius * math.cos(angle * radiansPerDegree) ))
    return (pointX, pointY)

def circle(points, radius, centerX, centerY, slow=0):
    canvas.delete('lines')
    canvas.delete('points')
    for i in range(points):
        x, y = point(i+1, points, radius-4)
        scaledX, scaledY = (x + centerX), (centerY - y)
        canvas.create_line(centerX, centerY, scaledX, scaledY, tag='lines')
        canvas.create_rectangle(scaledX-2, scaledY-2, scaledX+2, scaledY+2,
                                fill='red', tags='points')
        if slow:
            time.sleep(1)
            canvas.update()

def plotter():
    circle(scaleVar.get(), (Width // 2), originX, originY, checkVar.get())

def makewidgets():
    global canvas, scaleVar, checkVar
    canvas = Canvas(width=Width, height=Width)
    canvas.pack(side=TOP)
    scaleVar = IntVar()
    checkVar = IntVar()
    scale = Scale(label='Points on circle', variable=scaleVar, from_=1, to=60)
    scale.pack(side=LEFT)
    Checkbutton(text='Slow Mode', variable=checkVar).pack(side=LEFT)
    Button(text='Plot', command=plotter).pack(side=LEFT, padx=50)


if __name__ == '__main__':
    Width = 500
    if len(sys.argv) == 2: Width = int(sys.argv[1])
    originX = originY = Width // 2
    makewidgets()
    mainloop()
