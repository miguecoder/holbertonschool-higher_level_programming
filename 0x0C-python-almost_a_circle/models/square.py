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

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter function for size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter function for size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """public method def update(self, *args):
        that assigns an argument to each attribute"""

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])
