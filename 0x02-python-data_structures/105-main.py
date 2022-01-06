#!/usr/bin/python3
big_diff = __import__('105-big_diff').big_diff

my_list = [1, 2, 3, 4, 5, 3, -4, -1, 2]
diff = big_diff(my_list)
print("Big diff: {:d}".format(diff))
