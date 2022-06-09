#!/usr/bin/python3
"""Function that write a string to a text file"""


def write_file(filename="", text=""):
    """Function for write a string in a file"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
