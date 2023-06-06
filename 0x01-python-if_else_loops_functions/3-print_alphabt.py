#!/usr/bin/python3
for chr in range(97, 123):
    if chr == 101 or chr == 113:
        continue
    print("{:c}".format(chr), end="")
