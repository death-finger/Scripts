import timer, sys
import set, fastset


def setops(Class):
    a = Class(range(500))
    b = Class(range(200))
    c = Class(range(100))
    d = Class(range(50))
    for i in range(5):
        t = a&b&c&d
        t = a|b|c|b

if __name__ == '__main__':
    rept = len(sys.argv) > 1 and int(sys.argv[1]) or 5
    print('set => ', timer.test(rept, setops, set.Set))
    print('fastset => ', timer.test(rept, setops, fastset.Set))
