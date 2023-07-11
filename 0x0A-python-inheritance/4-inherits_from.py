#!/usr/bin/python3
""" inherits_from """


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited

    Args:
        obj (class): 
        a_class (class): 

    Returns:
        boolean: 
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
