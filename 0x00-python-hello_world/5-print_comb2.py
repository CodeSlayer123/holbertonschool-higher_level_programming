#!/usr/bin/python3
for i in range(00, 100):
    if i == 99:
        print("{}".format(i))
    else:
        if i < 10:
            print("{}".format("0"), end="")
        print("{}".format(i), end=", ")
