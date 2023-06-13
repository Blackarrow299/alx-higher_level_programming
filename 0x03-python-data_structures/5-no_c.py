#!/usr/bin/python3
def no_c(my_string):
    out = ""
    for char in my_string:
        if char == "c" or char == "C":
            continue
        out += char
    return out
