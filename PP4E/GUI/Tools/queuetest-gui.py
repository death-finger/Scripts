# e.g. 10-18

import _thread, queue, time
dataQueue = queue.Queue()


def producer(id, root):
    for i in range(5):
        time.sleep(1)
        print('put')
        dataQueue.put('[producer id=%d, count=%d]' % (id, i))
        root.insert('end', 'producer: produce id/count => %d/%d\n' % (id, i))
        root.see('end')

def consumer(root):
    try:
        print('get')
        data = dataQueue.get(block=False)
    except queue.Empty:
        pass
    else:
        root.insert('end', 'consumer got =>%s\n' % str(data))
        root.see('end')
    root.after(100, lambda: consumer(root))

def makethreads(root):
    for i in range(4):
        _thread.start_new_thread(producer, (i, root))

if __name__ == '__main__':
    from tkinter.scrolledtext import ScrolledText
    root = ScrolledText()
    root.pack()
    root.config(font=('courier', 14, 'bold'))
    root.bind('<Button-1>', lambda event: makethreads(root))
    consumer(root)
    root.mainloop()

