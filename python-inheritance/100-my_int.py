#!/usr/bin/python3
"""
Docstring for python-inheritance.100-my_int
"""


class MyInt(int):
    """
        Docstring for MyInt
        """

    def __eq__(self, other):
        if other == other:
            return False

    def __ne__(self, other):

        return True
