# e.g. 6-3

import sys, os, pprint
trace = 0   # 1代表目录, 2代表加上文件

visited = {}
allsizes = []
for srcdir in sys.path:
    for (dirpath, dirnames, filenames) in os.walk(srcdir):
        if trace >0: print(dirpath)
        dirpath = os.path.normpath(dirpath)
        fixcase = os.path.normcase(dirpath)
        if fixcase in visited: continue
        else: visited[fixcase] = True
        for filename in filenames:
            if filename.endswith('.py'):
                if trace >1: print('...', filename)
                pypath = os.path.join(dirpath, filename)
                try:
                    pysize = os.path.getsize(pypath)
                except os.error:
                    print('skipping', pypath, sys.exc_info()[0])
                else:
                    pylines = len(open(pypath, 'rb').readlines())
                    allsizes.append((pysize, pylines, pypath))

print('By size...')
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])

print('By lines...')
allsizes.sort(key=lambda x: x[1])
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])
