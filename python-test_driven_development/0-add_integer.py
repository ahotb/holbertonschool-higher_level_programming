#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers after casting floats to integers.

    If either argument is not an integer or float,
    a TypeError is raised with a specific message.
    The function returns the integer sum of a and b.

    Args:
        a: First number (int or float)
        b: Second number (int or float, default: 98)

    Returns:
        int: The sum of a and b as integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
