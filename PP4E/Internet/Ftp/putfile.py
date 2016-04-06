#!/usr/local/bin/python

# e.g. 13-5

import ftplib


def putfile(file, site, dir, user=(), *, verbose=True):
    if verbose:
        print('Uploading', file)
    local = open(file, 'rb')
    remote = ftplib.FTP(site)
    remote.login(*user)
    remote.cwd(dir)
    remote.storbinary('STOR ' + file, local, 1024)
    remote.quit()
    local.close()
    if verbose:
        print('Upload done.')


if __name__ == '__main__':
    site = 'ftp.rmi.net'
    dir = '.'
    import sys, getpass
    pswd = getpass.getpass(site + ' pswd?')
    putfile(sys.argv[1], site, dir, user=('lutz', pswd))
