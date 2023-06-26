#!/usr/bin/python3
def safe_print_division(a, b):
    out = 0
    print("Inside result: ", end="")
    try:
        out = a / b
    except Exception:
        out = None
    finally:
        print("{}".format(out))
    return out
