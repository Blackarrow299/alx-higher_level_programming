#!/usr/bin/python3
"""0-read_file"""


def read_file(filename=""):
    """print file content to stdout"""
    with open(filename, "+r", encoding="UTF-8") as f:
        text = f.read()
        print(text)
