#!/usr/bin/python3
""" 9-student.py """


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns directory description """
        return self.__dict__.copy()
