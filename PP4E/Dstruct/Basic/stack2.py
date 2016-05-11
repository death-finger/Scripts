class error(Exception): pass

class Stack:
    def __init__(self, start=[]):
        self.stack = []
        for x in start: self.push(x)
        self.reverse()

    def push(self, obj):
        self.stack = [obj] + self.stack

    def pop(self):
        if not self.stack: raise error('underflow')
        top, *self.stack = self.stack
        return top

    def top(self):
        if not self.stack: raise error('underflow')
        return self.stack[0]

    def empty(self):
        return not self.stack

    def __repr__(self):
        return '[Stack:%s]' % self.stack

    def __eq__(self, other):
        return self.stack == other.stack

    def __len__(self):
        return len(self.stack)

    def __add__(self, other):
        return Stack(self.stack + other.stack)

    def __mul__(self, other):
        return Stack(self.stack * other)

    def __getitem__(self, item):
        return self.stack[item]

    def __getattr__(self, item):
        return getattr(self.stack, item)