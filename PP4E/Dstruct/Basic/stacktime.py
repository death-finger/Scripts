import stack2, stack3, stack4, timer

rept = 2000
from sys import argv
pushes, pops, items = (int(arg) for arg in argv[1:])

def stackops(stackClass):
    x = stackClass('spam')
    for i in range(pushes): x.push(i)
    for i in range(items): t = x[i]
    for i in range(pops): x.pop()

for mod in (stack2, stack3, stack4):
    print('%s:' % mod.__name__, end=' ')
    print(timer.test(rept, stackops, getattr(mod, 'Stack')))
