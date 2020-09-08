#!/usr/bin/python3
def no_c(my_string):
    copy = ''
    for char in my_string:
        if char != 'C' and char != 'c':
            copy += char
    return copy
