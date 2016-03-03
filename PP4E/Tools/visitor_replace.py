# e.g. 6-20
"""
python visitor_replace.py rootdir fromStr toStr
"""

import sys
from visitor import SearchVisitor


class ReplaceVisitor(SearchVisitor):
    """
    将startDir及其子目录下的所有文件中的fromStr替换成toStr;
    修改过变量的文件名储存在obj.changed中
    """
    def __init__(self, fromStr, toStr, listOnly=False, trace=0):
        self.changed = []
        self.toStr = toStr
        self.listOnly = listOnly
        SearchVisitor.__init__(self, fromStr, trace)

    def visitmatch(self, fname, text):
        self.changed.append(fname)
        if not self.listOnly:
            fromStr, toStr = self.context, self.toStr
            text = text.replace(fromStr, toStr)
            open(fname, 'w').write(text)

if __name__ == '__main__':
    listonly = input('List only?') == 'y'
    visitor = ReplaceVisitor(sys.argv[2], sys.argv[3], listonly)
    if listonly or input('Proceed with changes?') == 'y':
        visitor.run(startDir=sys.argv[1])
        action = 'Changed' if not listonly else 'Found'
        print('Visited %d files' % visitor.fcount)
        print(action, '%d files' % len(visitor.changed))
        for fname in visitor.changed: print(fname)

