#!/usr/bin/python3
def magic_string():
    magic_string.i = getattr(magic_string, 'i', 0) + 1
    return ', '.join(["Holberton" for i in range(magic_string.i)])
