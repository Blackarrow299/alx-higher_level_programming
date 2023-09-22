#!/usr/bin/python3
"""1-base.py"""


import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to be serialized.

        Returns:
            str: JSON string representation of the list of dictionaries.

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of dictionaries from its JSON string representation.

        Args:
            json_string (str): JSON string representation of a list of dictionaries.

        Returns:
            list: A list of dictionaries.

        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of objects to be serialized and saved to a file.

        """
        filename = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                content.append(obj_dict)

        with open(filename, "w", encoding='utf-8') as jfile:
            json.dump(content, jfile)

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: A list of instances.

        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding='utf-8') as jfile:
                content = json.load(jfile)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        instances = []

        for obj_dict in content:
            temp = cls.create(**obj_dict)
            instances.append(temp)

        return instances
