#!/bin/env python
"""
e.g. 13-10
"""

import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type


nonpassive = False
remotesite = 'home.rmi.net'
remotedir = '.'
remoteuser = 'lutz'
remotepass = getpass('Password for %s on %s: ' % (remoteuser, remotesite))
localdir = (len(sys.argv) > 1 and sys.argv[1]) or '.'
cleanall = input('Clean local directory first?')[:1] in ['y', 'Y']

print('Connecting...')
connection = ftplib.FTP(remotesite)
connection.login(remoteuser, remotepass)
connection.cwd(remotedir)
if nonpassive:
    connection.set_pasv(False)

if cleanall:
    for localname in os.listdir(localdir):
        try:
            print('deleting local', localname)
            os.remove(os.path.join(localdir, localname))
        except:
            print('cannot delete local', localname)

count = 0
remotefiles = connection.nlst()

for remotename in remotefiles:
    if remotename in ('.', '..'): continue
    mimetype, encoding = guess_type(remotename)
    mimetype = mimetype or '?/?'
    maintype = mimetype.split('/')[0]
    localpath = os.path.join(localdir, remotename)
    print('downloading', remotename, 'to', localpath, end=' ')
    print('as', maintype, encoding or '')

    if maintype == 'text' and encoding == None:
        localfile = open(localpath, 'w', encoding=connection.encoding)
        callback = lambda line: localfile.write(line + '\n')
        connection.retrlines('RETR ' + remotename, callback)

    else:
        localfile = open(localpath, 'wb')
        connection.retrbinary('RETR ' + remotename, localfile.write)

    localfile.close()
    count += 1

connection.quit()
print('Done:', count, 'files downloaded')




