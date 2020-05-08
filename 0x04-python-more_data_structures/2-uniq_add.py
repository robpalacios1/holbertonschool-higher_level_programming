#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    uniq = set(my_list)
    for i in uniq:
        a = a + i
    return a
