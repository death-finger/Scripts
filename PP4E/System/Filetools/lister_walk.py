# e.g. 4-4

import sys, os

def lister(root):
    for (dirname, subdir, filename) in os.walk(root):
        print('[' + dirname + ']')
        for file in filename:
            path = os.path.join(dirname, file)
            print(path)

if __name__ == '__main__':
    lister(sys.argv[1])
