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

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list
        of the JSON string representation json_string:"""
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance
        with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 8)
        if cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        list_ins = []
        try:
            with open(filename, "r") as file:
                list_ins = [cls.create(**i)
                            for i in cls.from_json_string(file.read())]
            return list_ins
        except FileNotFoundError:
            return []
