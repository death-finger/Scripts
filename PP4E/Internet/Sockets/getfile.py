# e.g. 12-17

import sys, os, time, _thread as thread
from socket import *


blksz = 1024
defaultHost = 'localhost'
defaultPort = 50001

helptext = """
Usage...
server=> getfile.py -mode server [-port nnn] [-host hhh|localhost]
client=> getfile.py [-mode client] -file fff [-port nnn] [-host hhh|localhost]
"""

def now():
    return time.asctime()

def parsecommandline():
    dict = {}
    args = sys.argv[1:]
    while len(args) >=2:
        dict[args[0]] = args[1]
        args = args[2:]
    return dict

def client(host, port, filename):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send((filename + '\n').encode())
    dropdir = os.path.split(filename)[1]
    file = open(dropdir, 'wb')
    while True:
        data = sock.recv(blksz)
        #print('client recv:', data)
        if not data: break
        file.write(data)
    sock.close()
    file.close()
    print('Client got', filename, 'at', now())

def serverthread(clientsock):
    sockfile = clientsock.makefile('r')
    filename = sockfile.readline()[:-1]
    try:
        file = open(filename, 'rb')
        while True:
            bytes = file.read(blksz)
            #print('Server send data=>', bytes)
            if not bytes: break
            sent = clientsock.send(bytes)
            assert sent == len(bytes)
    except:
        print('Error downloading file on server:', filename)
    clientsock.close()

def server(host, port):
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind((host, port))
    serversock.listen(5)
    while True:
        clientsock, clientaddr = serversock.accept()
        print('Server connected by', clientaddr, 'at', now())
        thread.start_new_thread(serverthread, (clientsock,))

def main(args):
    host = args.get('-host', defaultHost)
    port = int(args.get('-port', defaultPort))
    if args.get('-mode') == 'server':
        if host == 'localhost': host = ''
        server(host, port)
    elif args.get('-file'):
        client(host, port, args['-file'])
    else:
        print(helptext)


if __name__ == '__main__':
    args = parsecommandline()
    main(args)
