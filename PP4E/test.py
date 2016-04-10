import imaplib, poplib, getpass


# Init
recv_server = input('[POP|IMAP]Address: ') or 'pop-mail.outlook.com'
#send_server = input('[SMTP]Address: ')
username = input('Username: ') or 'joshuapu@outlook.com'
password = getpass.getpass('Password: ') or 'Password01!'

if recv_server[:3] == 'pop':
    conn = poplib.POP3_SSL(recv_server, 995)
else:
    conn = imaplib.IMAP4_SSL(recv_server, 993)

conn.user(username)
conn.pass_(password)

# Recv mail
try:
    print(conn.getwelcome())
    msgCount, msgBytes = conn.stat()
    print('%s Mails\n%s Bytes in all' % (msgCount, msgBytes))
    input('[Press Enter to continue]')
    print(conn.list()[1].decode())
finally:
    conn.quit()