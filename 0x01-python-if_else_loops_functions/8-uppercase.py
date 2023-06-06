#!/usr/bin/python3
def uppercase(s):
    new_str = ""

    for char in s:
        ascii_code = ord(char)
        if ascii_code >= 97 and ascii_code <= 122:
            ascii_code -= 32
        new_str += chr(ascii_code)

    print("{}".format(new_str))
