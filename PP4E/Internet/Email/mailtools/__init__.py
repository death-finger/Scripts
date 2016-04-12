# e.g. 13-21

# 包目录导入时, 手机此处所有模块的内容

from .mailFetcher import *
from .mailSender import *
from .mailParser import *

# 运行mailtools import *时, 导入此处的嵌套模块

__all__ = 'mailFetcher', 'mailSender', 'mailParser'

