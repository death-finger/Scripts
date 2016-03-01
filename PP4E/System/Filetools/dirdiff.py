# e.g. 6-11
"""
python dirdiff.py dir1-path dir2-path
比较两个目录, 找出只在其中一个目录中出现的文件.
此脚本只比较文件名而不涉及文件内容.
"""

import sys, os

def reportdiffs(unique1, unique2, dir1, dir2):
    """
    为目录生成差异报告, comparedirs函数输出一部分
    """
    if not (unique1 or unique2):
        print('Directory lists are identical')
    else:
        if unique1:
            for file in unique1:
                print('...', file)
        if unique2:
            for file in unique2:
                print('...', file)

def difference(seq1, seq2):
    """
    仅返回seq1中的所有项
    """
    return [item for item in seq1 if item not in seq2]

def comparedirs(dir1, dir2, files1=None, files2=None):
    """
    比较目录内容而非文件实际内容, 可能需要listdir的bytes参数来处理
    某些系统平台上不可解码的文件名
    """
    print('Comparing', dir1, 'to', dir2)
    files1 = os.listdir(dir1) if files1 is None else files1
    files2 = os.listdir(dir2) if files2 is None else files2
    unique1 = difference(files1, files2)
    unique2 = difference(files2, files1)
    reportdiffs(unique1, unique2)
    return not (unique1 or unique2)     # 没有差别的话返回True

def getargs():
    "命令行模式参数"
    try:
        dir1, dir2 = sys.argv[1:3]
    except:
        print('Usage: dirdiff.py dir1 dir2')
        sys.exit(1)
    else:
        return (dir1, dir2)

if __name__ == '__main__':
    dir1, dir2 = getargs()
    comparedirs(dir1, dir2)
