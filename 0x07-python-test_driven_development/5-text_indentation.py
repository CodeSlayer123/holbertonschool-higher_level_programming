#!/usr/bin/python3
"""prints a text with 2 new lines  after each sentence"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these: ., ?, :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    txt = list(text)  # breaks text into iterable list

    for i in range(len(txt)):
        if txt[i] == '.' or txt[i] == '?' or txt[i] == ':':
            txt.insert(i+1, "\n")  # inserts 1st newline
            txt.insert(i+2, "\n")  # inserts 2nd newline
            txt.pop(i+3)   # deletes space after 2nd newline

    print("".join(txt), end="")
