# e.g. 13-9

import os, sys
print('Running in: ', os.getcwd())

from PP4E.Tools.find import findlist
mydir = os.path.dirname(findlist('PyFtpGui.pyw', startdir=os.curdir)[0])

if sys.platform[:3] == 'win':
    os.system('start %s\getfilegui.py' % mydir)
    os.system('start %s\putfilegui.py' % mydir)
else:
    os.system('python3.5 %s/getfilegui.py' % mydir)
    os.system('python3.5 %s/putfilegui.py' % mydir)
