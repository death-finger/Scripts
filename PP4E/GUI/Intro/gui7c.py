# e.g. 7-26

import gui7
from tkinter import *

class HelloPackage(gui7.HelloPackage):
    def __getattr__(self, item):
        return getattr(self.top, item)

if __name__ == '__main__':
    HelloPackage().mainloop()
