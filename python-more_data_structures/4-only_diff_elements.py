#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_dif = set()
    for x in set_1:
        if x not in set_2:
            only_dif.add(x)
    for x in set_2:
        if x not in set_1:
            only_dif.add(x)
    return only_dif
