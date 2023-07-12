#!/usr/bin/python3
"""1-write_file"""


def write_file(filename="", text=""):
    """write text to file"""
    with open(filename, "w") as f:
        return f.write(text)
