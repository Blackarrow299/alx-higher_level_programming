#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for n in my_list:
            if x <= 0:
                break
            print("{}".format(n), end="")
            i += 1
            x -= 1
        print("")
    except Exception:
        pass
    return i
