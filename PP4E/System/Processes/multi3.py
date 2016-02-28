# -*- coding:utf-8 -*-
# e.g. 5-31

import os
from multiprocessing import Process, Value, Array

procs = 3
count = 0

def showdata(label, val, arr):
    # 在此进程内打印数据值
    msg = '%-12s: pid:%4s, global:%s, value:%s, array:%s'
    print(msg % (label, os.getpid(), count, val.value, list(arr)))

def updater(val, arr):
    # 通过共享内存进行通讯
    global count
    count += 1
    val.value += 1
    for i in range(3): arr[i] += 1

if __name__ == '__main__':
    scalar = Value('i', 0)  # 共享内存是进程/线程安全的
    vector = Array('d', procs)  # ctypes中的类型代码: 就像int和double

    # 在父进程中显示起始值
    showdata('parent start', scalar, vector)

    # 派生子进程, 传入共享内存
    p = Process(target=showdata, args=('child', scalar, vector))
    p.start(); p.join()

    # 传入父进程中更新过的共享内存,等待每次传入结束
    # 每个子进程看到了父进程中到现在为止对args的更新(但全局变量的看不到)

    print('\nloop1 (updates in parent, serial children)...')
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s' % i), scalar, vector))
        p.start(); p.join()

    # 同上,不过允许子进程并行运行
    # 所有进程都看到了最近一次迭代的结果, 因为他们都共享这个对象

    print('\nloop2 (updates in parent, parallel children)...')
    ps = []
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s' % i), scalar, vector))
        p.start()
        ps.append(p)
    for p in ps: p.join()

    # 共享内存在派生子进程中进行更新,等待每个更新结束

    print('\nloop3 (updates in parent, serial children)...')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        p.join()
    showdata('parent temp', scalar, vector)

    # 同上,不过允许子进程并行地进行更新

    ps = []
    print('\nloop4 (updates in parent, parallel children)...')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)
    for p in ps: p.join()
    # 仅在父进程中全局变量count=6

    #在此显示最终结果
    showdata('parent end', scalar, vector)