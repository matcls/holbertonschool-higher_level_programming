#!/usr/bin/python3
"""Module for print <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Prints first and las name

    Args:
        first_name (str): First name
        last_name (str): Last name

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
