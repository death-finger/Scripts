"""
################################################
== 复用模块 ==
mailtools (包)
    服务器发送与接收, 解析, 撰写
threadtools.py
    GUI回调的线程队列管理
windows.py
    顶层窗口的边界配置
textEditor.py
    邮件查看窗口和一些弹出窗口里的文本组件

== 通用模块 ==
popuputil.py
    通用的帮助和忙碌窗口
messagecache.py
    缓存, 用于追踪已加载的邮件
wraplines.py
    工具脚本, 为邮件中长文本行换行
html2text.py
    基本的HTML解析器, 用于提取纯文本
mailconfig.py
    用户配置参数: 服务器名称, 字体等

== 专用模块 ==
SharedNames.py
    窗口类和主文件的共享对象
ViewWindows.py
    实现查看, 撰写, 回复和转发窗口
ListWindows.py
    邮件服务器和本地文件列表窗口
PyMailGuiHelp.py
    帮助文本
PyMailGui.py
    主文件
################################################
"""


