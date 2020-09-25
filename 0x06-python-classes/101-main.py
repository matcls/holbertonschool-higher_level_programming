#!/usr/bin/python3
"""Summary

Attributes:
    my_square (TYPE): Description
    Square (TYPE): Description
"""
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
