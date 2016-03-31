from tkinter import *
import math, time

Size = 400


def onPlot():
    canv.delete('all')
    points = scl_points_var.get()
    interval = scl_sleep_var.get()
    degree = (360 / points) * math.pi / 180
    radius = Size / 2
    centX, centY = radius, radius
    for point in range(points):
        X = int(round(200 + radius * math.sin(degree * (point + 1))))
        Y = int(round(200 - radius * math.cos(degree * (point + 1))))
        canv.create_line(centX, centY, X, Y)
        print(centX, centY, X, Y)
        canv.create_rectangle(X-2, Y+2, X+2, Y-2)
        canv.update()
        time.sleep(interval)


def makeWindow():
    global root, canv, scl_points_var, scl_sleep_var
    root = Tk()
    root.title('Round Table')
    canv = Canvas(root, width=Size, height=Size)
    canv.pack(side=TOP)
    scl_points_var = IntVar()
    scl_sleep_var = IntVar()
    scl_points = Scale(root, variable=scl_points_var, from_=1, to=360,
                       orient=HORIZONTAL, label='Points')
    scl_points.pack(side=BOTTOM, fill=X)
    scl_sleep = Scale(root, variable=scl_sleep_var, from_=0, to=60,
                      orient=HORIZONTAL, label='Sleep')
    scl_sleep.pack(side=BOTTOM, fill=X)
    btn = Button(root, text='Plot', command=onPlot)
    btn.pack(side=RIGHT)


if __name__ == '__main__':
    makeWindow()
    mainloop()