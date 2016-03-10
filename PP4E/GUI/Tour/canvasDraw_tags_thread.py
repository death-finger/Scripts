# e.g. 9-32

from tkinter import *
import _thread, time
import PP4E.GUI.Tour.canvasDraw_tags as canvasDraw_tags


class CanvasEventsDemo(canvasDraw_tags.CanvasEventsDemo):
    def moveEm(self, tag):
        for i in range(5):
            for (diffx, diffy) in [(+20, 0), (0, +20), (-20, 0), (0, -20)]:
                self.canvas.move(tag, diffx, diffy)
                time.sleep(0.25)

    def moveInSquares(self, tag):
        id = _thread.start_new_thread(self.moveEm, (tag,))


if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()
