# e.g. 6-17
"""
python search_all.py dir string
"""

import os, sys
listonly = False
textexts = ['.py', '.pyw', '.txt', '.c', '.h']      # 指定后缀名来忽略二进制文件

def searcher(startdir, searchkey):
    global fcount, vcount
    fcount = vcount = 0
    for (dirpath, dirnames, filenames) in os.walk(startdir):
        for filename in filenames:
            fpath = os.path.join(dirpath, filenames)
            visitfile(fpath, searchkey)

def visitfile(fpath, searchkey):
    global fcount, vcount       # 搜索字符串
    print(vcount+1, '=>', fpath)        # 跳过受保护的文件
    try:
        if not listonly:
            if os.path.splitext(fpath)[1] not in textexts:
                print('Skipping', fpath)
            elif searchkey in open(fpath).read():
                input('%s has %s' % (fpath, searchkey))
                fcount += 1
    except:
        print('Failed:', fpath, sys.exc_info()[0])
    vcount += 1

if __name__ == '__main__':
    searcher(sys.argv[1], sys.argv[2])
    print('Found in %d files, visited %d' % (fcount, vcount))
