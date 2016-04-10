#!/usr/local/bin/python

# e.g. 13-19

import smtplib, sys, email.utils, mailconfig
mailserver = mailconfig.smtpservername


From = 'joshuapu@outlook.com'
To = 'joshuap@wicresoft.com'
Tos = To.split(';')
Subj = input('Subj: ').strip()
Data = email.utils.formatdate()

text = ('From %s\nTo: %s\nData: %s\nSubject: %s\n\n' % (From, To, Data, Subj))

print('Type message text, end with line=[Ctrl+D(Unix)|Ctrl+Z(Win)]')
while True:
    line = sys.stdin.readline()
    if not line:
        break
    if line[:4] == 'From':
        line = '>' + line
    text += line

print('Connecting...')
server = smtplib.SMTP('smtp-mail.outlook.com')
server.starttls()
server.login(mailconfig.smtpuser, mailconfig.smtppasswdfile)
#server.password(mailconfig.smtppasswdfile)
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:
    print('Failed recipients:', failed)
else:
    print('Done')
print('Bye.')