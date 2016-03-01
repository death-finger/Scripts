# e.g. 6-16
"""
找到并删除命令行指定的目录及其子目录下所有的“*.pyc”字节码文件；它使用了一个Python
编码的寻找工具，因此是可跨平台一直的；可运行此脚本删除老的Python版本留下的.pyc文件；
"""

import os, sys, find        # import Tools.find

count = 0
for filename in find.find('*.pyc', sys.argv[1]):
    count += 1
    print(filename)
    os.remove(filename)

print('Removed %d .pyc files' % count)
