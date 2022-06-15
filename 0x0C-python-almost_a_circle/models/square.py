#!/usr/bin/python3
"""Class Square that inherits of Rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class inherits of rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Public method __str__ that returns
        [Square] (<id>) <x>/<y> - <width>/<height>"""
        a = f"[Square] ({self.id}) {self.x}/{self.y}"
        b = f" - {self.width}"
        return a + b
