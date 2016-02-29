#!/usr/bin/python
# -*- coding:utf-8 -*-
# e.g. 6-6
"""
合并split.py创建的目录下的所有组分文件以重建文件;
大概相当于Unix下的"cat fromdir/* > tofile"命令;
可移植和可配置性更好, 并且和复用函数; 依赖文件名排序
顺序: 长度必须一致; 可以进一步扩展分割/合并, 弹出Tkinter
"""

import os, sys
readsize = 1024

def join(fromdir, tofile):
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj = open(filepath, 'rb')
        while True:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close()
    output.close()

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: join.py [from-dir-name] [to-file-name]')
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromdir = input('Input the directory contains files: ')
            tofile = input('Name of the file to be recreated: ')
        else:
            interactive = False
            fromdir, tofile = sys.argv[1:3]
        absfrom, absto = map(os.path.abspath, [fromdir, tofile])
        print('Joining', absfrom, 'to make', absto)

        try:
            join(fromdir, tofile)
        except:
            print('Error joining files:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Join complete: see', absto)
        if interactive: input('Press Enter to exit...')
