#!/usr/bin/python3

def uppercase(str):
    s = list(str)
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[1]) <= 122:
            s[i] = ord(s[i])
            s[i] -= 32
            s[i] = chr(s[i])
        print(s[i], end="")

    print("")
