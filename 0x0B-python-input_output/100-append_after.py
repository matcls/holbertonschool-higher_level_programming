#!/usr/bin/python3
"""Function that inserts a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a given text to a file, after each line."""
    with open(filename, "r") as f:
        lines = f.readlines()

    new = []
    for i in range(len(lines)):
        new.append(lines[i])
        if search_string in lines[i]:
            new.append(new_string)

    with open(filename, "w") as f:
        f.writelines(new)
