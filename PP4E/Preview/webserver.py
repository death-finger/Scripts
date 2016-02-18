"""
eg. 1-32
用python实现一个HTTP Web服务器
脚本必须储存在webdir/cgi-bin or webdir/htbin
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 8000

os.chdir(webdir)
srvraddr = ('', port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
