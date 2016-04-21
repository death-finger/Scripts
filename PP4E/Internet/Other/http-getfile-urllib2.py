# e.g. 13-31

import sys, os, urllib.request, urllib.parse
showlines = 6

servername, filename = 'www.sina.com.cn', '/index.html'

remoteaddr = 'http://%s%s' % (servername, filename)
scheme, server, path, parms, query, frag = urllib.parse.urlparse(remoteaddr)
localname = os.path.split(path)[1]

print(remoteaddr, localname)
urllib.request.urlretrieve(remoteaddr, localname)
remotedata = open(localname, 'rb').readlines()
for line in remotedata[:showlines]:
    print(line)
