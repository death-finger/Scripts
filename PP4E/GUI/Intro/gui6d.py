# e.g. 7-23

from tkinter import *
from gui6 import Hello


class HelloExtender(Hello):
    def make_widgets(self):
        Hello.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)

    def message(self):
        print('Hello', self.data)

if __name__ == '__main__':
    HelloExtender().mainloop()