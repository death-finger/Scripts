#!/usr/bin/env python
# eg. 3-3

import os
print('setenv...', end=' ')
print(os.environ['USER'])

os.environ['USER'] = 'Brian'
os.system('python echoenv.py')

os.environ['USER'] = 'Arthur'
os.system('python echoenv.py')

os.environ['USER'] = input('?')
print(os.popen('python3.5 echoenv.py').read())