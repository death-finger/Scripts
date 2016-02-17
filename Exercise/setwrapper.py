# File: Set

class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)
    def intersect(self, other):
        res = []
        for x in other:
            if x in self.data:
                res.append(x)
        return Set(res)
    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in self.data:
                res.append(x)
        return Set(res)
    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)
    def __getitem__(self, key):
        return self.data[key]
    def __and__(self, other):
        return self.intersect(other)
    def __or__(self, other):
        return self.union(other)
    def __repr__(self):
        return 'Set:' + repr(self.data)

class SubSet(Set):
    def intersect(self, *args):
        res = []
        for x in self:
            for other in args:
                if not x in other:
                    break
            else:
                res.append(x)
        return Set(res)
    def union(self, *args):
        res = self.data[:]
        for x in args:
            for val in x:
                if val not in res:
                    res.append(val)
        return Set(res)

                    
if __name__ == '__main__':
    x = SubSet([1,2,3])
    y = SubSet([2,3,4])
    z = SubSet([3,4,5])
    a = SubSet('abc')
    b = SubSet('bcd')
    c = SubSet('cde')
    
