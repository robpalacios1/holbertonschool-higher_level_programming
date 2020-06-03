#!/usr/bin/python3
'''Read file module'''


def read_file(filename=""):
    '''open file 'filename' and print content'''
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
