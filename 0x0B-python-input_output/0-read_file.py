#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "+r", encoding="UTF-8") as f:
        text = f.read()
        print(text)
