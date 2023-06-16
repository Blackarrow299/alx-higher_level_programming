#!/usr/bin/python3
def weight_average(my_list=[]):
    a = b = 0
    for t in my_list:
        a += t[0] * t[1]
        b += t[1]
    return a / b
