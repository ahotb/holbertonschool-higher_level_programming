#!/usr/bin/python3
"""
Docstring for python-inheritance.101-add_attribute.py
"""


def add_attribute(obj, name, value):
    """
    Docstring for add_attribute

    :param obj: Description
    :param name: Description
    :param value: Description
    """
    if hasattr(obj, '__dict__'):

        setattr(obj, name, value)
    else:

        raise TypeError("can't add new attribute")
