#!/usr/bin/python3
"""Class that defines a Student."""


class Student:
    """Represent a Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrive a dictionary representation of a Student instance."""
        return self.__dict__.copy()
