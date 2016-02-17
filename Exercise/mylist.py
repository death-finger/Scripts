# File: mylist.py

class MyList():
    def __init__(self, start):
        self.wrapped = []
        for x in start: self.wrapped.append(x)
    def __add__(self, other):
        return MyList(self.wrapped + other)
    def __mul__(self, time):
        return MyList(self.wrapped * time)
    def __getitem__(self, offset):
        return self.wrapped[offset]
    def __len__(self):
        return len(self.wrapped)
    def __getslice__(self, low, high):
        return MyList(self.wrapped[low:high])
    def append(self, node):
        self.wrapped.append(node)
    def __getattr__(self, name):
        return getattr(self.wrapped, name)
    def __repr__(self):
        return repr(self.wrapped)

class MyListSub(MyList):
    calls = 0
    def __init__(self, start):
        self.adds = 0
        MyList.__init__(self, start)
    def __add__(self, other):
        MyListSub.calls += 1
        self.adds += 1
        return MyList.__add__(self, other)
    def stats(self):
        return self.calls, self.adds

class Meta:
    def __getattr__(self, name):
        print('get', name)
    def __setattr__(self, name, value):
        print('set', name, value)
        
if __name__ == '__main__':
    print('','-'*32, 'MyList Test', '='*32, sep='\n')
    x = MyList('spam')
    print(x)
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x * 3)
    x.append('a')
    x.sort()
    for c in x: print(c, end=' ')
    print('','-'*32, 'MyListSub Test', '='*32,  sep='\n')
    x = MyListSub('spam')
    y = MyListSub('foo')
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x + ['toast'])
    print(y + ['bar'])
    print(x.stats())
    
