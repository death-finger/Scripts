#!/bin/env python

# e.g. 13-15

import os, ftptools


class UploadAll(ftptools.FtpTools):
    def __init__(self):
        self.fcount = self.dcount = 0

    def getcleanall(self):
        return False

    def uploadDir(self, localdir):
        localfiles = os.listdir(localdir)
        for localname in localfiles:
            localpath = os.path.join(localdir, localname)
            print('uploading', localpath, 'to', localname, end=' ')
        if not os.path.isdir(localpath):
            self.uploadOne(localname, localpath, localname)
            self.fcount += 1
        else:
            try:
                self.connection.mkd(localname)
                print('directory created')
            except:
                print('directory not created')
            self.connection.cwd(localname)
            self.uploadDir(localpath)
            self.connection.cwd('..')
            self.dcount += 1
            print('directory exited')

if __name__ == '__main__':
    ftp = UploadAll()
    ftp.configTransfer(site='learning-python.com', rdir='training', user='lutz')
    ftp.run(transferAct=lambda: ftp.uploadDir(ftp.localdir))
    print('Done:', ftp.fcount, 'files and', ftp.dcount, 'directories uploaded.')

