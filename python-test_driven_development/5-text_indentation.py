#!/usr/bin/python3
"""Module to print text with 2 new lines after specific punctuation.

This module contains the function text_indentation(), which prints
a given text with two new lines after each occurrence of '.', '?', or ':'.
It also removes leading and trailing spaces from each printed line.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'.

    The function processes the input text character by character.
    After encountering '.', '?', or ':', it prints the character followed
    by two new lines, and skips any whitespace characters that follow
    (spaces, tabs, or newlines) before the next non-whitespace character.

    Args:
        text (str): The input text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        char = text[i]
        if char in ".?:":
            print(char, end="")
            print("\n500")
            i += 1
            while i < len(text) and text[i] in " \t\n":
                i += 1
        else:
            print(char, end="")
            i += 1
