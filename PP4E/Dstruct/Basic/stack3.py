class Stack:
    def __init__(self, start=[]):
        self.stack = None
        for i in range(-len(start), 0):
            self.push(start[-i-1])

    def push(self, node):
        self.stack = node, self.stack

    def pop(self):
        node, self.stack = self.stack
        return node

    def empty(self):
        return not self.stack

    def __len__(self):
        len, tree = 0, self.stack
        while tree:
            len, tree = len+1, tree[1]
        return len

    def __getitem__(self, index):
        len, tree = 0, self.stack
        while len < index and tree:
            len, tree = len+1, tree[1]
        if tree:
            return tree[0]
        else:
            raise IndexError()

    def __repr__(self):
        return '[FastStack:]' + repr(self.stack) + ']'


if __name__ == '__main__':
    import time
    from stack2 import Stack as NormStack
    x = Stack()
    y = NormStack()
    start = time.time()
    for i in range(50000):
        x.push(i)
    f_time = time.time() - start
    start = time.time()
    for i in range(50000):
        y.push(i)
    n_time = time.time() - start
    print(f_time)
    print(n_time)
    print(n_time/f_time)

