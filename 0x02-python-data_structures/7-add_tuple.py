#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)

    if len(a) == 0:
        a.append(0)
        a.append(0)
    elif len(a) == 1:
        a.append(0)

    if len(b) == 0:
        b.append(0)
        b.append(0)
    elif len(b) == 1:
        b.append(0)

    sumA = a[0] + b[0]
    sumB = a[1] + b[1]
    tuple_c = (sumA, sumB)
    return(tuple_c)
