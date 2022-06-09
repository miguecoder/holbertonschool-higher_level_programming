#!/usr/bin/python3
"""Class Student"""


class Student:
    """Initialization"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            if i in self.__dict__:
                dic[i] = self.__dict__[i]
        return dic

    def reload_from_json(self, json):
        """Method that replaces all attributes of
        the Student instance:"""
        for key, value in json.items():
            self.__dict__[key] = value
