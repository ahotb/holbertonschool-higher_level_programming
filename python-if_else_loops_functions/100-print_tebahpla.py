#!/usr/bin/python3
for code in range(ord("z"), ord("a") - 1, -1):
    cher = chr(code)
    position = ord("z") - code
    if position % 2 == 0:
        print(cher.lower(), end="")
    else:
        print(cher.upper(), end="")
