# e.g. 10-8

import sys
from packer import marker
mlen = len(marker)


def unpack(ifile, prefix='new-'):
    file = open(ifile, 'r')
    output = None
    for line in file.readlines():
        if line[:mlen] == marker:
            name = prefix + line[mlen:-1]
            output = open(name, 'w')
        else:
            output.write(line)

if __name__ == '__main__':
    unpack(sys.argv[1])
