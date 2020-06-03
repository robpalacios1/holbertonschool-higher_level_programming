#!/usr/bin/python3
def number_of_lines(filename=""):
    numlines = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            numlines = numlines + 1
    return numlines
