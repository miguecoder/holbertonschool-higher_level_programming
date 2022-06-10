#!/usr/bin/python3
'''This module have the Class BaseGeometry'''


class BaseGeometry():
    """/A class empty"""
    def area(self):
        """Class that raises a exception whe thi function
        is called"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Fucntion that validate value"""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

if __name__ == "__main__":
    import doctest
doctest.testfile("tests/7-base_geometry.txt")

