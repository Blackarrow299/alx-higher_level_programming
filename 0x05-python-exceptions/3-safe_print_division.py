#!/usr/bin/python3
def safe_print_division(a, b): 
    out = 0 
    try:
        out = a / b
    except Exception:
        out = None
    finally:
        print("Inside result: {}".format(out))
        return out


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
