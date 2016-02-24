# e.g. 5-11

import threading

class Mythread(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))

stdoutmutex = threading.Lock()
threads = []
for i in range(10):
    thread = Mythread(i, 100, stdoutmutex)
    threads.append(thread)
for thread in threads:
    thread.run()
print('Main thread exiting.')