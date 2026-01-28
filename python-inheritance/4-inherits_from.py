#!/usr/bin/python3
"""
Docstring for python-inheritance.4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
        Docstring for inherits_from

        :param obj: Description
        :param a_class: Description
        """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
