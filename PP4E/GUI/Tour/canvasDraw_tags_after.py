# e.g. 9-31

from tkinter import *
import PP4E.GUI.Tour.canvasDraw_tags as canvasDraw_tags


class CanvasEventsDemo(canvasDraw_tags.CanvasEventsDemo):
    def moveEm(self, tag, moremoves):
        (diffx, diffy), moremoves = moremoves[0], moremoves[1:]
        self.canvas.move(tag, diffx, diffy)
        if moremoves:
            self.canvas.after(250, self.moveEm, tag, moremoves)

    def moveInSquares(self, tag):
        allmoves = [(+20, 0), (0, +20), (-20, 0), (0, -20)]
        self.moveEm(tag, allmoves)


if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()
