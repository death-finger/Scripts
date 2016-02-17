"""
Read a file and counts its lines and characters.
"""

def countLines(name):
    name.seek(0)
    lines = name.readlines()
    tot = 0
    for i in lines: tot += 1
    return tot
"""
def countLines(name):
    name.seek(0)
    lines = name.readlines()
    return len(lines)
"""

def countChars(name):
    name.seek(0)
    chars = name.read()
    tot = 0
    for i in chars: tot += 1
    return tot

"""
def countChars(name):
    name.seek(0)
    chars = name.read()
    return len(chars)
"""
def test(filename):
    name = open(filename)
    print('This file has %s lines and %s chars!' %(countLines(name), countChars(name)))

"""
def test(filename):
    import time
    start = time.time()
    count(filename)
    passed = time.time() - start
    print('Time uses: ', passed)
"""

if __name__ == '__main__':
    import sys
    test(sys.argv[1])
