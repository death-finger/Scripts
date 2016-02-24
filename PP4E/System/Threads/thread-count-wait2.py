import _thread

stdoutmutex = _thread.allocate_lock()
exitmutexes = [False] * 10

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutexes[myId] = True

for i in range(10):
    _thread.start_new_thread(counter, (i, 100))

while False in exitmutexes: pass
print('Main thread exiting.')