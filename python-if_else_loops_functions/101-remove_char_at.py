#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n >= 0 and n < length:
        return str[:n] + str[n+1:]
    else:
        return str
