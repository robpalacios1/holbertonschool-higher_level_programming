#!/usr/bin/python3
'''from JSON string to object module'''


import json


def from_json_string(my_str):
    '''return an object by Json string 'my_str' '''
    return json.loads(my_str)
