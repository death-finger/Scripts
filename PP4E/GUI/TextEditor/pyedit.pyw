#!/usr/bin/python

# e.g. 11-3

import os, sys
mydir = os.path.dirname(sys.argv[0])
sys.path.insert(1, os.sep.join([mydir] + ['..']*3))
exec(open(os.path.join(mydir, 'textEditor.py')).read())
