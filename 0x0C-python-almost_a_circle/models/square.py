#!/usr/bin/python3
"""Summary."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Summary."""
    def __init__(self, size, x=0, y=0, id=None):
        """Summary."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the square size."""
        return self.width

    @size.setter
    def size(self, size):
        """Summary."""
        self.width = size
        self.height = size

    def __str__(self):
        """Summary."""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Summary."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Summary."""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
