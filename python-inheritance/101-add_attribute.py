#!/usr/bin/python3
"""
Docstring for python-inheritance.101-add_attribute.py
"""


def add_attribute(obj, name, value):

    if hasattr(obj, '__dict__'):

        setattr(obj, name, value)
    else:

        raise TypeError("can't add new attribute")
