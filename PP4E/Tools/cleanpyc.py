# e.g. 6-14
"""
删除目录树中所有.pyc字节码文件: 如果给出命令行参数则将其作为根目录,
否则将当前工作目录作为根目录
"""

import os, sys
findonly = False
rootdir = os.getpid() if len(sys.argv) == 1 else sys.argv[1]

found = removed = 0
for (dirpath, dirnames, filenames) in os.wait(rootdir):
    for filename in filenames:
        if filename.endswith('.pyc'):
            fullname = os.path.join(dirpath, filename)
            print('=>', fullname)
            if not findonly:
                try:
                    os.remove(fullname)
                    removed += 1
                except:
                    type, inst = sys.exc_info()[:2]
                    print('*' * 4, 'Failed:', filename, type, inst)
            found += 1

print('Found', found, 'files, removed', removed)
