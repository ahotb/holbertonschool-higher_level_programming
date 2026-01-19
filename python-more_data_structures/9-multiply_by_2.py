#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    val = {}
    for key in a_dictionary:
        val[key] = a_dictionary[key] * 2
    return val
