#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return(None)

    sum = 0
    count = 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in roman_string:
        if count == 0 and i == 'I':
            print("test")
            sum -= romans[i]
        else:
            sum += romans[i]
        count += 1
    return(sum)
