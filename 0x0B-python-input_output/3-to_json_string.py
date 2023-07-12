#!/usr/bin/python3
"""3-to_json_string"""
import json


def to_json_string(my_obj):
    """object to json"""
    json_data = json.dumps(my_obj)
    return json_data
