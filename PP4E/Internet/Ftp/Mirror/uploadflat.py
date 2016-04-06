#!/bin/env python

# e.g. 13-11

import sys, os, ftplib
from getpass import getpass
from mimetypes import guess_type


nonpassive = False
remotesite = 'learning-python.com'
remotedir = 'books'
remoteuser = 'lutz'
remotepass = getpass('Password for %s on %s:' % (remoteuser, remotesite))
localdir = (len(sys.argv) > 1 and sys.argv[1]) or '.'
cleanall = input('Clean remote directory first?')[:1] in ['Y', 'y']

print('connecting...')
connection = ftplib.FTP(remotesite)
connection.login(remoteuser, remotepass)
connection.cwd(remotedir)
if nonpassive:
    connection.set_pasv(False)

if cleanall:
    for remotename in connection.nlst():
        try:
            print('deleting remote', remotename)
            connection.delete(remotename)
        except:
            print('cannot delete remote', remotename)

count = 0
localfiles = os.listdir(localdir)

for localname in localfiles:
    mimetype, encoding = guess_type(localname)
    mimetype = mimetype or '?/?'
    maintype = mimetype.split('/')[0]

    localpath = os.path.join(localdir, localname)
    print('uploading', localpath, 'to', localname, end=' ')
    print('as', maintype, encoding or '')

    if maintype == 'text' and encoding == None:
        localfile = open(localpath, 'rb')
        connection.storlines('STOR ' + localname, localfile)

    else:
        localfile = open(localpath, 'rb')
        connection.storbinary('STOR ' + localname, localfile)

    localfile.close()
    count += 1

connection.quit()
print('Done:', count, 'files uploaded.')
