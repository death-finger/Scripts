#!/usr/local/bin/python
# e.g. 6-23

import os, sys, mimetypes, webbrowser


helpmsg = """
Sorry: can't find a media player for '%s' on your system!
Add an entry for your system to the media player dictionary
for this type of file in playfile.py, or play the file manually.
"""

def trace(*args): print(*args)

###################################
# 播放器技巧: 通用或特定: 待扩展
###################################

class MediaTool:
    def __init__(self, runtext=''):
        self.runtext = runtext
    def run(self, mediafile, **options):
        fullpath = os.path.abspath(mediafile)
        self.open(fullpath, **options)

class Filter(MediaTool):
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        player = os.popen(self.runtext, 'w')
        player.write(media.read())

class CmdLine(MediaTool):
    def open(self, mediafile, **ignored):
        cmdline = self.runtext % mediafile
        os.system(cmdline)

class Winstart(MediaTool):
    def open(self, mediafile, wait=False, **other):
        if not wait:
            os.startfile(mediafile)
        else:
            os.system('start /WAIT' + mediafile)

class Webbrowser(MediaTool):
    # file:// 必须用绝对路径
    def open(self, mediafile, **options):
        webbrowser.open_new('file://%s' % mediafile, **options)


###################################################################
# 媒体类型特异且系统平台特异的策略: 修改,或者传入一个新的策略作为替代
###################################################################

# 建立系统平台和播放器的对应关系, 在此修改!

audiotools = {
    'sunos5': Filter('/usr/bin/audioplay'),
    'linux2': CmdLine('cat %s > /dev/audio'),
    'sunos4': Filter('/usr/demo/SOUND/play'),
    'win32': Winstart()
    # 'win32': Cmdline('start %s')
}

videotools = {
    'linux2': CmdLine('tkcVideo_c700 %s'),
    'win32': Winstart()
}

imagetools = {
    'linux2': CmdLine('zimager %s'),
    'win32': Winstart()
}

texttools = {
    'linux2': Cmdline('vi %s'),
    'win32': CmdLine('notepad %s')
}

apptools = {
    'win32': Winstart()
}

# 建立文件名的mimetype与播放器表格的对应关系

mimetable = {'audio': audiotools,
             'video': videotools,
             'image': imagetools,
             'text': texttools,
             'application': apptools}

###################################
# 顶层接口
###################################

def trywebbrowser(filename, helpmsg=helpmsg, **options):
    """
    用网页浏览器打开文本/html, 另外对于其他文件类型, 如果碰到未知mimetype
    或系统平台, 也用网页游览器进行尝试, 作为最后的办法
    """
    trace('trying browser', filename)
    try:
        palyer = Webbrowser()
        palyer.run(filename, **options)
    except:
        print(helpmsg % filename)

def playknownfile(filename, playertable={}, **options):
    """
    播放已知类型的媒体文件: 使用平台特异的播放器对象, 如果这个平台下没有相应
    工具则派生一个网页游览器; 接受媒体特异的播放器表格
    """
    if sys.platform in playertable:
        playertable[sys.platform].run(filename, **options)
    else:
        trywebbrowser(filename, **options)

def playfile(filename, mimetable=mimetable, **options):
    """
    播放任意类型媒体文件: 使用mimetypes猜测媒体类型并对应到平台特异的播放器表格;
    如果是文本/html, 或者未知媒体类型, 或者没有播放表格, 则派生网页游览器
    """
    contenttype, encoding = mimetypes.guess_type(filename)
    if contenttype == None or encoding is not None:
        contenttype = '?/?'
    maintype, subtype = contenttype.split('/', 1)
    if maintype == 'text' and subtype == 'html':
        trywebbrowser(filename, **options)
    elif maintype in mimetable:
        playknownfile(filename, mimetable[maintype], **options)
    else:
        trywebbrowser(filename, **options)

###################################
# 自测代码
###################################

if __name__ == '__main__':
    playknownfile('sousa.au', audiotools, wait=True)
    playknownfile('ora-pp3e.gif', imagetools, wait=True)
    playknownfile('ora-lp4e.jpg', imagetools)

    # 媒体类型猜测完毕
    input('Stop players and press Enter')
    playfile('ora-lp4e.jpg')
    playfile('ora-pp3e.gif')
    playfile('priorcalendar.html')
