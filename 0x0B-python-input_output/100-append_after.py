#!/usr/bin/python3
"""Function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string """
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        for i in line:
            f.write(i)
            if (search_string in i):
                f.write(new_string)
