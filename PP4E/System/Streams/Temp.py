#!/usr/bin/python3.5
# -*- coding:utf-8 -*-

from subprocess import Popen, PIPE

#p1 = Popen('python3.5 writer.py', stdout=PIPE, shell=True)
p1 = Popen(['python3.5', 'writer.py'], stdout=PIPE)
p2 = Popen('python3.5 reader.py', stdin=p1.stdout, stdout=PIPE, shell=True)
output = p2.communicate()[0]
print(output)
print(p2.returncode)