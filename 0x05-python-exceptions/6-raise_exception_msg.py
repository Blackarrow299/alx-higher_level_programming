#!/usr/bin/python3
class NameError(Exception):
    pass
def raise_exception_msg(message=""):
    raise NameError(message)
