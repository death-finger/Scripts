# e.g. 10-23

import sys
from socket import *
port =50008
host = 'localhost'


def redirectOut(port=port, host=host):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('w')
    sys.stdout = file

def redirectIn(port=port, host=host): pass