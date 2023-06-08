#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    print("{} arguments".format(arg_count), end="")
    if arg_count > 0:
        print(':')
        for i in range(1, arg_count + 1):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print('.')
