# e.g. 6-2

import sys, os, pprint
trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Python43\Lib'
else:
    dirname = '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5'

allsize = []
for (dirpath, dirnames, filenames) in os.walk(dirname):
    if trace: print(dirpath)
    for filename in filenames:
        if trace: print('...', filename)
        fullname = os.path.join(dirpath, filename)
        filesize = os.path.getsize(fullname)
        allsize.append((fullname, filesize))

allsize.sort()
pprint.pprint(allsize[:2])
pprint.pprint(allsize[-2:])
