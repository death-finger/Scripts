# e.g. 5-10

import _thread, time
stdoutmutex = _thread.allocate_lock()
numthreads = 5
exitmutexes = [_thread.allocate_lock() for i in range(numthreads)]

def counter(myId, count, mutex):
    for i in range(count):
        start = time.time()
        time.sleep(1 / (myId + 1))
        with mutex:
            print('Time Used: %.2f' % (time.time() - start))
            print('[%s] => %s' % (myId, i))
    exitmutexes[myId].acquire()

for i in range(numthreads):
    _thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25)
print('Main thread exiting.')