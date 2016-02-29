# e.g. 6-4

import os, pprint
from sys import argv, exc_info

trace = 1       # 0 - 关闭; 1 - 目录; 2 - 加上文件
dirname, extname = os.curdir, '.py'    # 默认为当前工作目录下的.py文件
if len(argv) > 1: dirname = argv[1]     # e.g. C:\ or /Users
if len(argv) > 2: extname = argv[2]     # e.g. .pyw, .txt
if len(argv) > 3: trace = int(argv[3])  # e.g. "/usr/bin .py 2"

def tryprint(arg):
    try:
        print(arg)      # 不能打印的文件名?
    except UnicodeEncodeError:
        print(arg.encode())     # 尝试原始字节字符串

visited = set()
allsizes = []
for (dirpath, dirnames, filenames) in os.walk(dirname):
    if trace: tryprint(dirpath)
    dirpath = os.path.normpath(dirpath)
    fixname = os.path.normcase(dirpath)
    if fixname in visited:
        if trace: tryprint('skipping ' + dirpath)
    else:
        visited.add(fixname)
        for filename in filenames:
            if filename.endswith(extname):
                if trace > 1: tryprint('+++' + filename)
                fullname = os.path.join(dirpath, filename)
                try:
                    bytesize = os.path.getsize(fullname)
                    linesize = sum(+1 for line in open(fullname, 'rb'))
                except Exception:
                    print('error', exc_info()[0])
                else:
                    allsizes.append((bytesize, linesize, fullname))

for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    allsizes.sort(key = lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[:-3])

