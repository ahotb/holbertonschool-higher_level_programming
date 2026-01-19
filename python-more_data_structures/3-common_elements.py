#!/usr/bin/python3
def common_elements(set_1, set_2):
    add_set = set()
    for x in set_1:
        if x in set_2:
            add_set.add(x)
    return add_set
