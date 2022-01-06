#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        s = ' '.join(map(str, row))
        for i in range(0, len(s), 2):
            integer = int(s[i])
            if i == len(s) - 1:
                print("{:d}".format(integer), end="")
            else:
                print("{:d}".format(integer), end=" ")
        print()
