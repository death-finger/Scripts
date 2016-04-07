#!/bin/env python

# e.g. 13-14

import os, sys, ftplib
from getpass import getpass
from mimetypes import  guess_type, add_type


dfltSite = 'home.rmi.net'
dfltRdir = '.'
dfltUser = 'lutz'


class FtpTools:
    def getlocaldir(self):
        return (len(sys.argv) > 1 and sys.argv[1]) or '.'

    def getcleanall(self):
        return input('Clean target dir first?')[:1] in ['Y', 'y']

    def getpassword(self):
        return getpass('Password for %s on %s:' % (self.remoteuser, self.remotesite))

    def configTransfer(self, site=dfltSite, rdir=dfltRdir, user=dfltUser):
        self.nonpassive = False
        self.remotesite = site
        self.remotedir = rdir
        self.remoteuser = user
        self.localdir = self.getlocaldir()
        self.cleanall = self.getcleanall()
        self.remotepass = self.getpassword()

    def isTextKind(self, remotename, trace=True):
        add_type('text/x-python-win', '.pyw')
        mimetype, encoding = guess_type(remotename, strict=False)
        mimetype = mimetype or '?/?'
        maintype = mimetype.split('/')[0]
        if trace: print(maintype, encoding or '')
        return maintype == 'text' and encoding == None

    def connectFtp(self):
        print('connecting...')
        connection = ftplib.FTP(self.remotesite)
        connection.login(self.remoteuser, self.remotepass)
        connection.cwd(self.remotedir)
        if self.nonpassive:
            connection.set_pasv(False)
        self.connection = connection

    def cleanLocals(self):
        if self.cleanall:
            for localname in os.listdir(self.localdir):
                try:
                    print('deleting local', localname)
                    os.remove(os.path.join(self.localdir, localname))
                except:
                    print('cannot delete local', localname)

    def cleanRemotes(self):
        if self.cleanall:
            for remotename in self.connection.nlst():
                try:
                    print('deleting remote', remotename)
                    self.connection.delete(remotename)
                except:
                    print('cannot delete remote', remotename)

    def downloadOne(self, remotename, localpath):
        if self.isTextKind(remotename):
            localfile = open(localpath, 'w', encoding=self.connection.encoding)
            def callback(line):
                localfile.write(line + '\n')
            self.connection.retrlines('RETR ' + remotename, callback)
        else:
            localfile = open(localpath, 'wb')
            self.connection.retrbinary('RETR ' + remotename, localfile.write)
        localfile.close()

    def uploadOne(self, localname, localpath, remotename):
        if self.isTextKind(localname):
            localfile = open(localpath, 'rb')
            self.connection.storlines('STOR ' + remotename, localfile)
        else:
            localfile = open(localpath, 'rb')
            self.connection.storbinary('STOR ' + remotename, localfile)
        localfile.close()

    def downloadDir(self):
        remotefiles = self.connection.nlst()
        for remotefile in remotefiles:
            if remotefile in ('.', '..'): continue
            localpath = os.path.join(self.localdir, remotename)
            print('downloading', remotename, 'to', localpath, 'as', end=' ')
            self.downloadOne(remotename, localpath)
        print('Done:', len(remotefiles), 'files downloaded.')

    def uploadDir(self):
        localfiles = os.listdir(self.localdir)
        for localname in localfiles:
            localpath = os.path.join(self.localdir, localname)
            print('uploading', localpath, 'to', localname, 'as', end=' ')
            self.uploadOne(localname, localpath, localname)
        print('Done:', len(localfiles), 'files uploaded.')

    def run(self, cleanTarget=lambda: None, transferAct=lambda: None):
        self.connectFtp()
        cleanTarget()
        transferAct()
        self.connection.quit()

if __name__ == '__main__':
    ftp = FtpTools()
    xfermode = 'download'
    if len(sys.argv) > 1:
        xfermode = sys.argv.pop(1)
    if xfermode == 'download':
        ftp.configTransfer()
        ftp.run(cleanTarget=ftp.cleanLocals, transferAct=ftp.downloadDir)
    elif xfermode == 'upload':
        ftp.configTransfer(site='learning-python.com', rdir='books', user='lutz')
        ftp.run(cleanTarget=ftp.cleanRemotes, transferAct=ftp.uploadDir)
    else:
        print('Usage: ftptools.py ["download" | "upload"] [localdir]')
