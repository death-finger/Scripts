# e.g. 12-3

import sys
from PP4E.launchmodes import QuietPortableLauncher


numclients = 1

def start(cmdline):
    QuietPortableLauncher(cmdline, cmdline)()

args = ''
for i in range(numclients):
    start('echo-client.py %s' % args)

input()