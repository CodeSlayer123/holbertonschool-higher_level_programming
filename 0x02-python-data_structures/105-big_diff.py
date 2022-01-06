#!/usr/bin/python3
def big_diff(my_list=[]):
    if len(my_list) == 0 or len(my_list) == 1:
        return(0)
    my_list.sort()
    max = my_list[len(my_list) - 1]
    min = my_list[0]
    return(max - min)
