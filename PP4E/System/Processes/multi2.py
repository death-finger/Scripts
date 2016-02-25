# e.g. 5-30

import os
from multiprocessing import Process, Pipe

def sender(pipe):
    pipe.send(['spam'] + [42, 'eggs'])
    pipe.close()

def talker(pipe):
    pipe.send(dict(name='bob', spam=42))
    reply = pipe.recv()
    print('talker got:', reply)

if __name__ == '__main__':
    (parentEnd, childEnd) = Pipe()
    Process(target=sender, args=(childEnd,))
    print('parent god:', parentEnd.recv())
    parentEnd.close()

    (parentEnd, childEnd) = Pipe()
    child = Process(target=talker, args=(childEnd,))
    child.start()
    print('parent got:', parentEnd.recv())
    parentEnd.send({x * 2 for x in 'spam'})
    child.join()
    print('parent exit')