#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """json file content to object"""
    with open(filename, "r") as f:
        text = f.read()
        return json.loads(text)
