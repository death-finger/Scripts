# e.g. 12-8

import socketserver, time
myHost = ''
myPort = 50007


def now():
    return time.ctime(time.time())

class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address, now())
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            if not data: break
            reply = 'Echo=>%s at %s' % (data, now())
            self.request.send(reply.encode())
        self.request.close()


myaddr = (myHost, myPort)
server = socketserver.ThreadingTCPServer(myaddr, MyClientHandler)
server.serve_forever()