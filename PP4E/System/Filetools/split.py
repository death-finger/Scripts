# e.g. 6-5
#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
将文件分割成很多组分, join.py将他们合并回去;
这是标准的Unix split命令工具行的一个可定制版本, 因为它用python写成,
所以在Windows 下也能工作和方便地修改; 因为它输出一个函数, 所以它的逻辑
业务也可以由其他应用程序导入并重复使用;
"""

import os, sys
kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)

def split(fromfile, todir, chunksize=chunksize):
    if not os.path.exists(todir):
        os.mkdir(todir)
    else:
        # delconfirm = input('Filename: %s exists, do you want to remove it?(Y/N): ')    尝试添加删除确认
        # if delconfirm in ['Y', 'y']:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir, fname))
    partnum = 0
    input = open(fromfile, 'rb')
    while True:
        chunk = input.read(chunksize)
        if not chunk: break
        partnum += 1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()
    input.close()
    assert partnum <= 999
    return partnum

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromfile = input('Input the file to be split: ')
            todir = input('The directory to store part files: ')
        else:
            interactive = False
            fromfile, todir = sys.argv[1:3]
            if len(sys.argv) == 4: chunksize = int(sys.argv[3])
        absfrom, absto = map(os.path.abspath, [fromfile, todir])
        print('Splitting', absfrom, 'to', absto, 'by', chunksize)

        try:
            parts = split(fromfile, todir, chunksize)
        except:
            print('Error during split:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Split finished:', parts, 'parts are in', absto)
        if interactive: input('Press Enter to exit')
