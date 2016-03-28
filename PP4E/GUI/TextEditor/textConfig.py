# -*- coding:utf-8 -*-
# e.g. 11-1

#--------------------------------------------------------------
# 常规配置
#--------------------------------------------------------------

# 初始字体
font = ('courier', 9, 'normal')

# 初始颜色
bg = 'lightcyan'
fg = 'black'

# 初始大小
height = 20
width = 80

# 区分大小写的搜索
caseinsens = True

#--------------------------------------------------------------
# Unicode编码行为以及打开和保存文件进行命名
#--------------------------------------------------------------
                                # 1) 尝试内部默认编码
opensAskUser = True             # 2) 尝试用户输入(if True)
opensEncoding = ''              # 3) 尝试这些编码(如果有定义)
                                # 4) 尝试平台默认编码sys.getdefaultencoding()
                                # 5) 使用binary模式和Tk策略

savesUseKnownEncoding = 1       # 1) 从上一次的打开或保存中尝试已知编码(if > 0)
savesAskUser = True             # 2) 尝试用户输入(if True)
savesEncoding = ''              # 3) 尝试这些编码(如果有定义)
                                # 4) 尝试平台默认编码sys.getdefaultencoding()
