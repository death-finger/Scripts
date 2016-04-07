#!/bin/env python

# e.g. 13-16

from ftptools import FtpTools


class CleanAll(FtpTools):
    def __init__(self):
        self.fcount = self.dcount = 0

    def getlocaldir(self):
        return None

    def getcleanall(self):
        return True

    def cleanDir(self):
        lines = []
        self.connection.dir(lines.append)
        for line in lines:
            parsed = line.split()
            permiss = parsed[0]
            fname = parsed[-1]
            if fname in ('.', '..'):
                continue
            elif permiss[0] != 'd':
                print('file', fname)
                self.connection.delete(fname)
                self.fcount += 1
            else:
                print('directory', fname)
                self.connection.cwd(fname)
                self.cleanDir()
                self.connection.cwd('..')
                self.connection.rmd(fname)
                self.dcount += 1
                print('directory exited')

if __name__ == '__main__':
    ftp = CleanAll()
    ftp.configTransfer(site='learning-python.com', rdir='training', user='lutz')
    ftp.run(cleanTarget=ftp.cleanDir)
    print('Done', ftp.fcount, 'files and', ftp.dcount, 'directories cleaned')
