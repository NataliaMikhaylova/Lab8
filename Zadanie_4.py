#!/usr/bin/env python3
# -*- config: utf-8 -*-

import sys

def getInput():
    return input('>>> ')

def testInput(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def strToInt(a):
    return int(a)

def printInt(a):
    return print(type(a), a)

if __name__ == '__main__':
    b = getInput()
    if testInput(b) is True:
        c = strToInt(b)
        printInt(c)
    if testInput(b) is False:
        print('Ошибка', file=sys.stderr)
        exit(1)