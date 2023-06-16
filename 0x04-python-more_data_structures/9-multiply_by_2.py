#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict(map(lambda k: (k, a_dictionary[k] * 2), a_dictionary))
