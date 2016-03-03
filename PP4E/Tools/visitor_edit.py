# e.g. 6-19
"""
python visitor_edit.py string rootdir?
对SearchVisitor添加一个作为外部子类组分的编辑器自动启动行为; 在遍历过程中
对含有字符串的每个文件自动弹出一个编辑器; 在Windows下还可以使用editor='edit'
或'notepad'; 想要使用本书稍后介绍到的texteditor, 可以试试r'python Gui\TextEditor\textEditor.py'
也可传入一个搜索命令, 在某些编辑器启动时即调到第一处匹配
"""

import os, sys
from visitor import SearchVisitor


class EditVisitor(SearchVisitor):
    """
    编辑startDir及其目录下含有字符串的文件
    """
    editor = r'C:\cygwin\bin\vim-nox.exe' if sys.platform[:3] == 'win' else 'vim'

    def visitmatch(self, fpathname, text):
        os.system('%s %s' % (self.editor, fpathname))

if __name__ == '__main__':
    visitor = EditVisitor(sys.argv[1])
    visitor.run('.' if len(sys.argv) < 3 else sys.argv[2])
    print('Edited %d files, visited %d' % (visitor.scount, visitor.fcount))

