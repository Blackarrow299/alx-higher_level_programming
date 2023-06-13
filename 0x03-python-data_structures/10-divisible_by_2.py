#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    out = []
    for n in my_list:
        if n % 2 == 0:
            out.append(True)
        else:
            out.append(False)
    return out
