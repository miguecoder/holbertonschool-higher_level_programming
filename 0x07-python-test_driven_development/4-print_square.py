#!/usr/bin/python3
"""Function that print a square with the character # """


def print_square(size):
    """
    Function that print a square with the character #
    """
    if not type(size) is int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    i, j = 0, 0
    for i in range(size):
        for z in range(size):
            print('#', end='')
        print()
