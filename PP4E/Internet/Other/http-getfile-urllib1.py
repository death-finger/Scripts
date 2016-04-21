# e.g. 13-30

import sys
from urllib.request import urlopen
showlines = 60
servername, filename = 'www.sina.com.cn', '/index.html'

remoteaddr = 'http://%s%s' % (servername, filename)
print(remoteaddr)
remotefile = urlopen(remoteaddr)
remotedata = remotefile.readlines()
remotefile.close()
for line in remotedata[:showlines]:
    print(line)
