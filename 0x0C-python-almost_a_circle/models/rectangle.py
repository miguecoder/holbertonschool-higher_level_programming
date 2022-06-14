#!/usr/bin/python3
"""This module content the class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class rectangle that inherits
    from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter function for width"""
        return self.__width

    @property
    def height(self):
        """Getter function for height"""
        return self.__height

    @property
    def x(self):
        """getter function for x"""
        return self.__x

    @property
    def y(self):
        """getter function for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter function for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter function for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter function fot x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter function for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
 
    def area(self):
        """public method area, that return the
        area of rectangle"""
        return self.__height * self.__width
