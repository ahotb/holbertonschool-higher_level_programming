#!/usr/bin/python3
def best_score(a_dictionary):
    best_scor = None
    val = -1
    if not a_dictionary:
        return None
    for i in a_dictionary:
        key = a_dictionary[i]
        if key > val:
            val = key
            best_scor = i
    return best_scor
