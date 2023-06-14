#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    out = 0
    flag = False
    for i, char in enumerate(roman_string):
        if char == 'X':
            flag = True
            out += 10
        elif char == 'I':
            if flag is False:
                out -= 1
            else:
                out += 1
        elif char == 'V':
            flag = True
            out += 5
        elif char == 'L':
            flag = True
            out += 50
        elif char == 'C':
            flag = True
            out += 100
        elif char == 'D':
            flag = True
            out += 500
        elif char == 'M':
            flag = True
            out += 1000

    return out
