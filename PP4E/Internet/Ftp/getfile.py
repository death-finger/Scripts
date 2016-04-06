#!/usr/local/bin/python

# e.g. 13-4

from ftplib import FTP
from os.path import exists


def getfile(file, site, dir, user=(), *, verbose=True, refetch=False):
    if exists(file) and not refetch:
        if verbose:
            print(file, 'already fetched')
    else:
        if verbose:
            print('Downloading', file)
        local = open(file, 'wb')
        try:
            remote = FTP(site)
            remote.login(*user)
            remote.cwd(dir)
            remote.retrbinary('RETR ' + file, local.write, 1024)
            remote.quit()
        finally:
            local.close()
        if verbose:
            print('Download done.')


if __name__ == '__main__':
    from getpass import getpass
    file = 'monkeys.jpg'
    dir = '.'
    site = 'ftp.rmi.net'
    user = ('lutz', getpass('PWD:'))
    getfile(file, site, dir, user)