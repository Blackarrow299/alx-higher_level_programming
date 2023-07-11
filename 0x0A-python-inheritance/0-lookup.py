#!/usr/bin/python3
"""classs composed of lookup function"""


def lookup(obj):
    """function that return attrs and methods of a given object

    Args:
        obj (Object): object

    Returns:
        list: list of attrs and methods
    """
    return dir(obj)
