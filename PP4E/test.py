import poplib
from email.parser import Parser
#sep = None
sep = '='*80 + '\n\n'


def trace(sep=None):
    print(sep)

def maildec(txt):
    return [line.decode('utf8') for line in txt]

srvr = poplib.POP3('pop.sina.com')
srvr.user('joshuapu@sina.com')
srvr.pass_('bagakira')
srvr.getwelcome()
trace(sep)

msgCount, msgByte = srvr.stat()
trace(sep)

"""msgs = []
for i in range(1, msgCount + 1):
    msg = srvr.retr(i)
    msgs.append(msg)
msg1 = msgs[0]"""



resp, hdrlines, respsz = srvr.top(1, 0)
hdr = maildec(hdrlines)
#hdrpar = Parser.parsestr(hdr)


resp, text, respsz = srvr.retr(1)
msg = maildec(text)
with open('htmltest.html', 'w') as file:
    for item in msg:
        file.write(item + '\n')


print(hdr)
trace(sep)
print(msg)
trace(sep)