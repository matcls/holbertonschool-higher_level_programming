#!/usr/bin/python3
"""Class that defines a Student."""


class Student:
    """Represent a Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrive a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        return self.__dict__.update(json)
