#!/usr/bin/python3
"""This module define de class:Square with private instance attribute"""


class Square:
    """This method define a private instance attribute -> size"""
    def __init__(self, size=0):
        """Define like Private instance attribute: size"""
        self.__size = size
    """New private instance attribute property"""
    @property
    def size(self):
        return self.__size

    """New private instance attribute property setter"""
    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """area is a new Public instance method"""
    def area(self):
        return self.__size * self.__size
