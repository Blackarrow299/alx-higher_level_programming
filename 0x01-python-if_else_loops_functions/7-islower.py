#!/usr/bin/python3
def islower(c):
    ascii_code = ord(c)
    if ascii_code >= 96 and ascii_code <= 122:
        return True
    else:
        return False
