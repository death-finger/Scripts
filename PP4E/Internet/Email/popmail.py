#!/usr/local/bin/python

# e.g. 13-18

import poplib, getpass, sys, mailconfig
import imaplib

mailserver = mailconfig.popservername
mailuser = mailconfig.popusername
mailpasswd = getpass.getpass('Password for %s:' % mailserver)

print('Connecting...')
server = poplib.POP3(mailserver)
server.user(mailuser)
server.pass_(mailpasswd)

try:
    print(server.getwelcome())
    msgCount, msgBytes = server.stat()
    print('There are', msgCount, 'mails in Total', msgBytes, 'bytes.')
    print(server.list())
    print('-'*80)
    input('[Press Enter to continue]')

    for i in range(msgCount):
        hdr, message, octets = server.retr(i+1)
        for line in message: print(line.decode())
        print('-' * 80)
        if i < msgCount - 1:
            input('[Press Enter to show next]')
finally:
    server.quit()
print('Bye.')
