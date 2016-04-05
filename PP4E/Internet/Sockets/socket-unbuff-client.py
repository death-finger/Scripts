# e.g. 12-14

import time
from socket import *
sock = socket()
sock.connect(('localhost', 50007))
file = sock.makefile('w', buffering=1)


print('sending data1')
file.write('spam\n')
time.sleep(5)
#file.flush()

print('sending data2')
print('eggs', file=file)
time.sleep(5)
#file.flush()

print('sending data3')
sock.send(b'ham\n')
time.sleep(5)
