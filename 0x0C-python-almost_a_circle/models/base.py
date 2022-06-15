#!/usr/bin/python3
"""This module contain the class Base"""


import csv
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """method that serializes in CSV"""
        filename = cls.__name__ + ".csv"
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[i.id, i.width, i.height, i.x, i.y]
                             for i in list_objs]
            elif cls is Square:
                list_objs = [[i.id, i.size, i.x, i.y]
                             for i in list_objs]
        with open(filename, "w") as file:
            csv_file = csv.writer(file)
            csv_file.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """method that deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        from models.rectangle import Rectangle
        from models.square import Square
        list_csv = list()

        with open(filename, "r") as f:
            file = csv.reader(f)
            for line in file:
                args = [int(content) for content in line]
                if cls is Rectangle:
                    dictionary = {
                        "id": args[0],
                        "width": args[1],
                        "height": args[2],
                        "x": args[3],
                        "y": args[4]
                        }
                elif cls is Square:
                    dictionary = {
                        "id": args[0],
                        "size": args[1],
                        "x": args[2],
                        "y": args[3]
                    }
                list_csv.append(cls.create(**dictionary))
        return list_csv
