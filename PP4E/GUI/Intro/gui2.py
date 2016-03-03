# e.g. 7-10

import sys
from tkinter import *

widget = Button(None, text='Hello GUI world!', command=sys.exit)
widget.pack()
widget.mainloop()