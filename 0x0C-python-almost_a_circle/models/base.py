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
    def save_to_file(self, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of objects to be serialized and saved to a file.

        """
        filename = self.__name__ + ".json"
        content = []

        if list_objs is not None:
            content = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w", encoding='utf-8') as jfile:
            jfile.write(self.to_json_string(content))

    @classmethod
    def load_from_file(self):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: A list of instances.

        """
        filename = self.__name__ + ".json"

        try:
            with open(filename, encoding='utf-8') as jfile:
                content = jfile.read()
        except FileNotFoundError:
            return []  # If the file doesn't exist

        obj_dicts = self.from_json_string(content)
        instances = []

        for obj_dict in obj_dicts:
            temp = self.create(**obj_dict)
            instances.append(temp)

        return instances
