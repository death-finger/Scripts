#!/usr/local/bin/python

# e,g, 13-2

import os, getpass
from urllib.request import urlopen
filename = 'monkeys.jpg'
password = getpass.getpass('Pwd: ')
remoteaddr = 'ftp://lutz:%s@ftp.rmi.net/%s;type=i' % (password, filename)
print('Downloading', remoteaddr)

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile.write(remotefile.read())
localfile.close()
remotefile.close()
