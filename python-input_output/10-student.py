#!/usr/bin/python3
"""
Docstring for python-input_output.10-student
"""


class Student:
    """
        Docstring for Student
        """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict

        return self.__dict__
