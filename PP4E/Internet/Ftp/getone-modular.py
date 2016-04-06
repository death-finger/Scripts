#!/usr/local/bin/python

# e.g. 13-3


import getfile
from getpass import getpass
filename = 'monkeys.jpg'


getfile.getfile(file=filename, site='ftp.rmi.net', dir='.',
                user=('lutz', getpass('PWD:')), refetch=True)

if input('Open file?') in ['Y', 'y']:
    from PP4E.System.Media.playfile import playfile
    playfile(filename)
