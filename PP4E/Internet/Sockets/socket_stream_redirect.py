# e.g. 12-10

import sys
from socket import *
port = 50050
host = 'localhost'


def initListenerSocket(port=port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    conn, addr = sock.accept()
    return conn

def redirectOut(port=port, host=host):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    file = sock.makefile('w')
    sys.stdout = file
    return sock

def redirectIn(port=port, host=host):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    file = sock.makefile('r')
    sys.stdin = file
    return sock

def redirectBothAsClient(port=port, host=host):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    ofile = sock.makefile('w')
    ifile = sock.makefile('r')
    sys.stdout = ofile
    sys.stdin = ifile
    return sock

def redirectBothAsServer(port=port, host=host):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()
    ofile = conn.makefile('w')
    ifile = conn.makefile('r')
    sys.stdout = ofile
    sys.stdin = ifile
    return conn

