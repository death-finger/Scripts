#!/usr/local/bin/python

import poplib, smtplib, email.utils
import mailconfig
from email.parser import Parser
from email.message import Message
fetchEncoding = mailconfig.fetchEncoding


def decodeToUnicode(messageBytes, fetchEncoding=fetchEncoding):
    return [line.decode(fetchEncoding) for line in messageBytes]

def splitaddrs(field):
    pairs = email.utils.getaddresses([field])
    return [email.utils.formataddr(pair) for pair in pairs]

def inputmessage():
    import sys
    From = input('From: ').strip
    To = input('To: ').strip
    To = splitaddrs(To)
    Subj = input('Subject: ').strip()
    print('Type message text, end with line="EOF"')
    text = ''
    while True:
        line = sys.stdin.readline()
        import re
        if re.match('[EeOoFf]*', line).group(): break
        text += line
    return From, To, Subj, text

def sendmessage():
    From, To, Subj, text = inputmessage()
    msg = Message()
    msg['From'] = From
    msg['To'] = To
    msg['Subject'] = Subj,
    msg['Data'] = email.utils.formatdate()
    msg.set_payload(text)
    server = smtplib.SMTP(mailconfig.smtpservername)
    try:
        failed = server.sendmail(From, To, str(msg))
    except:
        print('Error - send failed')
    else:
        if failed:
            print('Failed:', failed)

def connect(servername, user, passwd):
    print('Connecting...')
    server = poplib.POP3(servername)
    server.user(user)
    server.pass_(passwd)
    print(server.getwelcome())
    return server

def loadmessages(servername, user, passwd, loadfrom=1):
    server = connect(servername, user, passwd)
    try:
        print(server.list())
        (msgCount, msgBytes) = server.stat()
        print(msgCount, 'Mails;', msgBytes, 'Bytes')
        print('Retrieving...')
        msgList = []
        for i in range(loadfrom, msgCount + 1):
            hdr, message, octets = server.retr(i)
            message = decodeToUnicode(message)
            msgList.append('\n'.join(message))
    finally:
        server.quit()
    assert len(msgList) == (msgCount - loadfrom) + 1
    return msgList

def deletemessages(servername, user, passwd, toDelete, verify=True):
    print('To be deleted:', toDelete)
    if verify and input('Delete?')[:1] not in ['y', 'Y']:
        print('Delete cancelled')
    else:
        server = connect(servername, user, passwd)
        try:
            print('Deleting messages from server...')
            for msgnum in toDelete:
                server.dele(msgnum)
        finally:
            server.quit()

def showindex(msgList):
    count = 0
    for msgtext in msgList:
        msghdrs = Parser().parsestr(msgtext, headersonly=True)
        count += 1
        print('%d:\t%d bytes' % (count, len(msgtext)))
        for hdr in ('From', 'To', 'Data', 'Subject'):
            try:
                print('\t%-8s=>%s' % (hdr, msghdrs[hdr]))
            except KeyError:
                print('\t%-8s=>(unknown)' % hdr)
        if count % 5 == 0:
            input('[Press Enter to continue...]')

def showmessage(i, msgList):
    if 1 <= i <= len(msgList):
        print('-' * 79)
        msg = Parser().parsestr(msgList[i-1])
        content = msg.get_payload()
        if isinstance(content, str):
            content = content.rstrip() + '\n'
        print(content)
        print('-' * 79)
    else:
        print('Bad msg number')

def savemessage(i, mailfile, msgList):
    if 1 <= i <= len(msgList):
        savefile = open(mailfile, 'a', encoding=mailconfig.fetchEncoding)
        savefile.write('\n' + msgList[i-1] + '-'*80 + '\n')
    else:
        print('Bad msg number')

def msgnum(command):
    try:
        return int(command.split()[1])
    except:
        return -1

helptext = """
Available commands:
i       -   index display
l n?    -   list all msgs (or just msg n)
d n?    -   mark all msgs (or just msg n)
s n?    -   save all msgs (or just msg n)
m       -   compose and send a new mail msg
q       -   quit
?       -   disp help
"""

def interact(msgList, mailfile):
    showindex(msgList)
    toDelete = []
    while True:
        try:
            command = input('[Pymail] Action<?>:')
        except EOFError:
            command = 'q'
        if not command:
            command = '*'
        if command == 'q':
            break
        elif command[0] == 'i':
            showindex(msgList)
        elif command[0] == 'l':
            if len(command) == 1:
                for i in range(1, len(msgList) + 1):
                    showmessage(i, msgList)
            else:
                showmessage(msgnum(command), msgList)
        elif command[0] == 's':
            if len(command) == 1:
                for i in range(1, len(msgList) + 1):
                    savemessage(i, mailfile, msgList)
            else:
                savemessage(msgnum(command), mailfile, msgList)
        elif command[0] == 'd':
            if len(command) == 1:
                toDelete = list(range(1, len(msgList)+1))
            else:
                delnum = msgnum(command)
                if (1 <= delnum <= len(msgList)) and (delnum not in toDelete):
                    toDelete.append(delnum)
                else:
                    print('Bad msg number')
        elif command[0] == 'm':
            sendmessage()
        elif command[0] == '?':
            print(helptext)
        else:
            print('Command not exist, type "?" for help')
    return toDelete

if __name__ == '__main__':
    import getpass, mailconfig
    mailserver = mailconfig.popservername
    mailuser = mailconfig.popusername
    mailfile = mailconfig.savemailfile
    mailpwd = mailconfig.poppasswdfile
    print('[Pymail email client]')
    msgList = loadmessages(mailserver, mailuser, mailpwd)
    toDelete = interact(msgList, mailfile)
    if toDelete:
        print('Delete:', toDelete, sep=' | ')
    print('Bye')
