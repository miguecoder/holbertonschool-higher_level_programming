#!/usr/bin/python3
"""Function that read a text file and print it"""


def read_file(filename=""):
    """Function for open a file"""

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
