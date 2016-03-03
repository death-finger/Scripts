# e.g. 6-18
"""
##########################################################################
python visitor.py dir testmask [string]
使用类和子类封装os.wall调用手法某些细节，以便进行遍历和搜索；testmask是一个整数
比特掩码，每个可用的自我测试占1位；另请参考：visitor_*/.py子类用例；
框架中一般应当使用_X作为伪局部名称，不过为了在子类和客户端的使用，这里的
所有名称都将导出；可重新定义reset以支持多个需要更新子类的相互独立的遍历操作；
##########################################################################
"""

import os, sys


class FileVisitor:
    """
    访问startDir(默认为'.')下所有非目录文件；可通过重载visit*方法定制文件/目录
    处理器；情境参数/属性为可选的子类特异的状态；追踪开关：0-关闭，1-显示目录，
    2-显示目录及文件
    """
    def __init__(self, context=None, trace=2):
        self.fcount = 0
        self.dcount = 0
        self.context = context
        self.trace = trace

    def run(self, startDir=os.curdir, reset=True):
        if reset: self.reset()
        for (dirpath, dirnames, filenames) in os.walk(startDir):
            self.visitdir(dirpath)
            for fname in filenames:
                fpath = os.path.join(dirpath, fname)
                self.visitfile(fpath)

    def reset(self):
        self.fcount = self.dcount = 0

    def visitdir(self, dirpath):
        self.dcount += 1
        if self.trace > 0: print(dirpath, '...')

    def visitfile(self, filepath):
        self.fcount += 1
        if self.trace > 1: print(self.fcount, '=>', filepath)


class SearchVisitor(FileVisitor):
    """
    在startDir及其子目录下的文件中搜索字符串；子类：根据需要重新定义
    visitmatch、扩展列表和候选；子类可以使用testexts来指定进行搜索的文件
    类型(还可以重定义候选以对文本内容使用mimetypes)
    """
    skipexts = []
    testexts = ['.txt', '.py', '.pyw', '.html', '.c', '.h']
    # skipexts = ['.gif', '.jpg', '.pyc', '.o', '.a', '.exe']

    def __init__(self, searchkey, trace=2):
        FileVisitor.__init__(self, searchkey, trace)
        self.scount = 0

    def reset(self):
        self.scount = 0

    def candidate(self, fname):
        ext = os.path.splitext(fname)[1]
        if self.testexts:
            return ext in self.testexts
        else:
            return ext not in self.skipexts

    def visitfile(self, fname):
        FileVisitor.visitfile(self, fname)
        if not self.candidate(fname):
            if self.trace > 0: print('Skipping', fname)
        else:
            text = open(fname).read()
            if self.context in text:
                self.visitmatch(fname, text)
                self.scount += 1

    def visitmatch(self, fname, text):
        print('%s has %s' % (fname, self.context))

if __name__ == '__main__':
    dolist = 1
    dosearch = 2 # 3=进行列出和搜索
    donext = 4

    def selftest(testmask):
        if testmask & dolist:
            visitor = FileVisitor(trace=2)
            visitor.run(sys.argv[2])
            print('Visited %d files and %d dirs' % (visitor.fcount, visitor.dcount))

        if testmask & dosearch:
            visitor = SearchVisitor(sys.argv[3], trace=0)
            visitor.run(sys.argv[2])
            print('Found in %d files, visited %d' % (visitor.scount, visitor.fcount))

    selftest(int(sys.argv[1]))