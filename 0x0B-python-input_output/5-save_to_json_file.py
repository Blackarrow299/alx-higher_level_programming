#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """write obj to file as json format"""
    with open(filename, "w") as f:
        json_data = json.dumps(my_obj)
        f.write(json_data)
