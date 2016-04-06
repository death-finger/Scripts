#!/usr/local/bin/python

# e.g. 13-6

from getpass import getpass
from PP4E.Internet.Ftp.getfile import getfile
from PP4E.System.Media.playfile import playfile


file = 'sousa.au'

site = 'ftp.rmi.net'
dir = '.'
user = ('lutz', getpass('Pswd?'))

getfile(file, site, dir, user)
playfile(file)