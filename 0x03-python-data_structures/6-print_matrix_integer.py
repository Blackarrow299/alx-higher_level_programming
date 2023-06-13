#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for n in arr:
            print("{:d}".format(n), end="")
            if arr[-1] != n:
                print(" ", end="")
        print()
