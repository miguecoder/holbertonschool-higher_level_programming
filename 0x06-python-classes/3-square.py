#!/usr/bin/python3
"""This module define de class:Square with private instance attribute"""


class Square:
    """This method define a private instance attribute -> size"""
    def __init__(self, size=0):
        """Define like Private instance attribute: size"""
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
    """Area is a new Public instance method"""
    def area(self):
        return self.__size * self.__size
