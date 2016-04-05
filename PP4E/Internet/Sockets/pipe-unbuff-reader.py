# e.g. 12-16

import os


for line in os.popen('python -u pipe-unbuff-writer.py'):
    print(line, end='')
