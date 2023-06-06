#!/usr/bin/python3
for code in range(122, 96, -1):
    if code % 2 != 0:
        code -= 32
    print("{:c}".format(code), end="")
