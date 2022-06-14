#!/usr/bin/python3
"""Thi module contain the class Base"""


class Base:
    """Class Base with private attribute and
    public instance"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
