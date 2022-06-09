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
        if type(attrs) is [list, str]:
            dic = {}
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return dic
        return self.__dict__
