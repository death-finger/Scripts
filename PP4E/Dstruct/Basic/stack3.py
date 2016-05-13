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
    from stack4 import Stack as AppendStack
    x = NormStack()
    y = Stack()
    z = AppendStack()
    tests = []
    for i in x, y, z:
        start = time.time()
        for num in range(50000):
            i.push(num)
        f_time = time.time() - start
        tests.append(f_time)

    for ti in tests:
        sep = '='*30
        print('Time => %s\n' % (ti))
        print(sep)
    print('NormStack/TupleStack = %s' % (tests[0]/tests[1]))
    print('NormStack/AppendStack = %s' % (tests[0]/tests[2]))
    print('AppendStack/TupleStack = %s' % (tests[2]/tests[1]))


