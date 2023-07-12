#!/usr/bin/python3
"""2-append_write"""


def append_write(filename="", text=""):
    """append text to file"""
    with open(filename, "w") as f:
        return f.write(text)
