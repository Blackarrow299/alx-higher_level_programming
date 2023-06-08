#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    print("{} ".format(arg_count), end="")
    if arg_count == 0:
        print("arguments.")
    elif arg_count > 0:
        if arg_count == 1:
            print("argument:")
        else:
            print("arguments:")
        for i in range(1, arg_count + 1):
            print("{}: {}".format(i, sys.argv[i]))
