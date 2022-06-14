#!/usr/bin/python3
"""This module content the class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class rectangle that inherits
    from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for width"""
        self.__width = value

    @property
    def height(self):
        """Getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height"""
        self.__height = value

    @property
    def x(self):
        """getter function for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function fot x"""
        self.__x = value

    @property
    def y(self):
        """getter function for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for y"""
        self.__x = value
