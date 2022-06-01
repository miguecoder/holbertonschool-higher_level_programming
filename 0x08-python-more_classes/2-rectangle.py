#!/usr/bin/python3
"""This is a module with the class Rectangle"""


class Rectangle:
    """
    Class rectangle with privates instances
    attributes width and height.
    """
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Private instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """Private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Public instance method that
        returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method that
        returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width
