#!/usr/bin/python3
"""
Docstring for python-input_output.0-read_file
"""


def read_file(filename=""):
    """
        Docstring for read_file
        Read a UTF-8 text file and print its content to stdout
        :param filename: Description
        """
    if filename:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read(), end="")
