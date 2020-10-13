#!/usr/bin/python3
"""Summary."""
from models.base import Base


class Rectangle(Base):
    """Summary."""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Summary."""
        return self.__width

    @property
    def height(self):
        """Summary."""
        return self.__height

    @property
    def x(self):
        """Summary."""
        return self.__x

    @property
    def y(self):
        """Summary."""
        return self.__y

    @width.setter
    def width(self, width):
        """Summary."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Summary."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Summary."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Summary."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the Rectangle area."""
        return self.__height * self.__width

    def display(self):
        """Summary."""
        print("\n" * self.__y, end="")
        print(((self.__x * ' ') + ('#' * self.__width +
                                   '\n')) * self.__height, end="")

    def __str__(self):
        """Summary."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Summary."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Summary."""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height':
                self.height, 'width': self.width}
