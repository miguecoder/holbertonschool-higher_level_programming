#!/usr/bin/python3
"""This module content the class Rectangle"""

from ast import arguments
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

    def display(self):
        """Public method display, that prints in
        stdout the Rectangle instance with the character #"""
        for v in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Public method __str__ that returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        a = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        b = f" - {self.__width}/{self.__height}"
        return a + b

    def update(self, *args):
        """public method def update(self, *args):
        that assigns an argument to each attribute: """

        if args:
            arg = list(args)
            for i in range(len(arg)):
                if i == 0:
                    self.id = arg[i]
                if i == 1:
                    self.__width = arg[i]
                if i == 2:
                    self.__height = arg[i]
                if i == 3:
                    self.__x = arg[i]
                if i == 4:
                    self.__y = arg[i]
