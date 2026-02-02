#!/usr/bin/python3
"""
Docstring for python-input_output.7-add_item
"""
import sys

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []
arg = sys.argv[1:]
existing_list.extend(arg)
save_to_json_file(existing_list, "add_item.json")
