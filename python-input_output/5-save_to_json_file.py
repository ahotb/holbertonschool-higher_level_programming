#!/usr/bin/python3
"""json module"""
import json


def save_to_json_file(my_obj, filename):
    """
        Docstring for save_to_json_file

        :param my_obj: Description
        :param filename: Description
        """
    with open(filename, 'w', encoding='utf=8') as f:
        json.dump(my_obj, f)
