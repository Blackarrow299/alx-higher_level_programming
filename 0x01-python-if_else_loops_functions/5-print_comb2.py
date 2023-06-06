#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print(f"{n:0>2d}", end="")
        continue
    print(f"{n:0>2d}, ", end="")
