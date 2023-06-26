#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for n in range(0, x):
            print("{:d}".format(my_list[n]), end="")
            i += 1
    except Exception:
        pass
    print("")
    return i
