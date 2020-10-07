#!/usr/bin/python3
"""Function that reads n lines of a text file (UTF8) and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """Read n lines of a text file."""
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        for line in f:
            print(line, end="")
            nb_lines -= 1
            if nb_lines <= 0:
                break
