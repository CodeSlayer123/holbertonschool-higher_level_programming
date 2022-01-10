#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return(None)
    sort = dict(sorted(a_dictionary.items(), key=lambda item: item[1]))
    best = len(sort) - 1
    keys_list = list(sort)
    return(keys_list[best])
