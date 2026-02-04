#!/usr/bin/python3
"""
Docstring for python-input_output.100-append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Docstring for append_after

        :param filename: Description
        :param search_string: Description
        :param new_string: Description
        """

    with open(filename, 'r') as file:
        lines = file.readlines()

    new_content = []
    for line in lines:
        new_content.append(line)
        if search_string in line:
            new_content.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(new_content)
