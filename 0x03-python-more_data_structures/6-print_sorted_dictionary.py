#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = dict(sorted(a_dictionary.items(), key=lambda item: item[0]))

    for i in sort:
        print("{}:".format(i,), sort[i])
