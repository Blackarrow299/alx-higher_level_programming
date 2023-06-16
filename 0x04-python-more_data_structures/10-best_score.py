#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    maxkey = list(a_dictionary.keys())[0]
    for k in a_dictionary.keys():
        maxkey = k if a_dictionary[k] > a_dictionary[maxkey] else maxkey
    return maxkey
