#!/usr/bin/python3
"""This module contain the class Base"""


import json


class Base:
    """Class Base with private attribute and
    public instance"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that return the JSON string
        representation of list_dictionaries"""

        if list_dictionaries == "" or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON
        string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_objs))
