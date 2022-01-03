#!/usr/bin/python3
flag = 0
for i in range (0, 9):
    print("{}".format(i), end = "")
    if i == 8:
        flag = 1
    for j in range (1, 10):
        if flag == 1 and j == 9:
            print("{}".format(i))
        else:
            print("{}".format(i), end = ",")
