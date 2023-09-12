#!/usr/bin/python3
""" 8-class_to_json.py"""


def class_to_json(obj):
    """ Furetuns the dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
