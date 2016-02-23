#!/usr/bin/python3.5
from sys import argv
from scanfile import scanner
class UnknownCommand(Exception): pass

def processLine(line):
    if line[0] == '*':
        print('Ms.', line[1:-1])
    elif line[0] == '+':
        print('Mr.', line[1:-1])
    else:
        raise UnknownCommand(line)

filename = 'data.txt'
if len(argv) == 2: filename = argv[1]
scanner(filename, processLine)