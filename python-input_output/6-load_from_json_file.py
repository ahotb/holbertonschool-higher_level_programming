#!/usr/bin/python3
"""json module"""
import json


def load_from_json_file(filename):
    """
        Docstring for save_to_json_file

        :param my_obj: Description
        :param filename: Description
        """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
