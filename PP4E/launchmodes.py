# -*- coding:utf-8 -*-
"""
#############################################################################
用命令行和可复用的启动方案来启动Python程序; 在命令行开头自动向Python可执行文件插入
"python"和/或路径; 这个模块的某些部分可能假定'python'在你的系统路径中(参考Launcher.py);

使用subprocess模块也可行, 不过os.popen()在内部调用这个模块, 目标是在这里启动一个独立运行的
程序, 而非连接到它的流; multiprocessing模块也是一个选择, 不过这里处理命令行而非函数, 为实
现这里的选项之一而开始一个进程不是很合理;

脚本文件名路径将经过normpath()处理, 必要时将所有/改成\以供Windows工具使用;
PyEdit和其他工具继承这个修正; 在Windows下吗一般允许在文件打开中用/, 但并非所有启动工具;
#############################################################################
"""

import sys, os
pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'
pyPATH = sys.executable


def fixWindowsPath(cmdline):
    """
    将cmdline开头的脚本文件名路径里所有的/改成\; 在Windows下, 仅为运行需要这种处理的
    工具的类所使用; 在其他平台上, 这么做也没有坏处;
    """
    splitline = cmdline.lstrip().split(' ')
    fixedPATH = os.path.normpath(splitline[0])
    return ' '.join([fixedPATH] + splitline[1:])

class LaunchMode:
    """
    在实例中待命, 声明标签并运行命令; 子类按照run()中的需要格式化命令行; 命令应当以
    准备运行的python脚本名开头, 而且不带"python"或脚本的完整路径
    """
    def __init__(self, label, command):
        self.what = label
        self.where = command
    def __call__(self):             # 等待调用, 执行按钮按下的回调动作
        self.announce(self.what)
        self.run(self.where)        # 子类必须定义run()
    def announce(self, text):       # 子类可以重新定义announce()
        print(text)
    def run(self, cmdline):
        assert False, 'run() must be defined'

class System(LaunchMode):
    """
    运行shell命令行中指定的Python脚本; 小心: 可能阻塞调用者, 除非在
    Unix下带上&操作符
    """
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.system('%s %s' % (pyPATH, cmdline))

class Popen(LaunchMode):
    """
    在新进程中运行shell命令行; 小心: 可能阻塞调用者, 因为管道关闭的太快
    """
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.popen(pyPATH + ' ' + cmdline)        # 假设没有数据可以读取

class Fork(LaunchMode):
    """
    在显示地创建的新进程中运行命令, 仅在类Unix系统下可用, 包括Cygwin
    """
    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = cmdline.split()
        if os.fork() == 0:
            os.execvp(pyPATH, [pyfile] + cmdline)

class Start(LaunchMode):
    """
    独立于调用者运行程序, 仅在WIndows下可用: 使用了文件名关联
    """
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        cmdline = fixWindowsPath(cmdline)
        os.startfile(cmdline)

class StartArgs(LaunchMode):
    """
    仅在Windows下可用: args可能需要用到真正的start命令; 斜杠在这里没问题
    """
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        os.system('start' + cmdline)

class Spawn(LaunchMode):
    """
    在独立于调用者的新进程中运行python; 在Windows和Unix下都可用;
    DOS中使用P_NOWAIT; 斜杠在这里没问题
    """
    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pyPATH, (pyfile, cmdline))

class Top_level(LaunchMode):
    """
    在新窗口中运行, 进程是同一个; 待讨论; 还需要GUI类信息
    """
    def run(self, cmdline):
        assert False, 'Sorry - mode not yet implemented'


#
# 为这个平台挑选一个"最佳"启动器
# 可能需要在其他地方细化这个选项
#

if sys.platform[:3] == 'win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork

class QuietPortableLauncher(PortableLauncher):
    def announce(self, text): pass

def selftest():
    file = 'echo.py'
    input('default mode...')
    launcher = PortableLauncher(file, file)
    launcher()          # 不阻塞

    input('system mode...')
    System(file, file)()        # 阻塞

    if sys.platform[:3] == 'win':
        input('DOS start mode...')      # 不阻塞
        StartArgs(file, file)()

if __name__ == '__main__': selftest()
