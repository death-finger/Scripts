# e.g. 5-17

import os
exitstat = 0

def child():
    global exitstat
    exitstat += 1
    print('Hello form child', os.getpid(), exitstat)
    os._exit(exitstat)
    print('Never reached')

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pid, status = os.wait()
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q': break

if __name__ == '__main__':
    parent()
