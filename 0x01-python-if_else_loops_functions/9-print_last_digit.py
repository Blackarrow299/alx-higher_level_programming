#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10
    str = "{:.0f}".format(last_digit)
    print(str)
    return str
