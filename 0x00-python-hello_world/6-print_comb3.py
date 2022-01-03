#!/usr/bin/python3
for i in range (0, 9):
    print(i, end = "")
    if i == 8:
        flag = 1
    for j in range (1, 10):
        if flag == 1 && j == 9:
            print(i)
        else:
            print(i, end = ",")
