#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Class that represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Arguments:
        first_name (str): First name of the student.
        last_name (str): Last name of the student.
        age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student
        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Arguments:
        attrs: The attributes to represent
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {at: getattr(self, at) for at in attrs if hasattr(self, at)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.
        Arguments:
        json (dict): key/value pairs to replace attributes with.
        """
        for key, values in json.items():
            setattr(self, key, values)
