#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if a_dictionary is None:
        return None
    for k in a_dictionary.keys():
        max = a_dictionary[k] if a_dictionary[k] > max else max
    return max
