#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    err = None
    operator = None
    a = 0
    b = 0
    result = 0
    if len(sys.argv) > 4 or len(sys.argv) == 1:
        err = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            result = a / b
        else:
            err = "Unknown operator. Available operators: +, -, * and /"

    if err is not None:
        print("{}".format(err), end="")
        sys.exit(1)
    else:
        print("{:d} {} {:d} = {:.0f}".format(a, operator, b, result), end="")
        sys.exit(0)
