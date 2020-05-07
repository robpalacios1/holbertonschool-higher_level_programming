#!/usr/bin/python3
def roman_to_int(roman_string):
    a = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
             'M': 1000}
    if roman_string is None or type(roman_string) != str:
        return 0
    for i in roman_string:
        if i in roman:
            a = a + roman[i]
    for compare in range(0, len(roman_string) - 1):
        if roman[roman_string[compare]] < roman[roman_string[compare + 1]]:
            a = a - 2
    return a
