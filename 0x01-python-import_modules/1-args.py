#!/usr/bin/python3
def main():
    from sys import argv
    size = len(argv) - 1
    if size == 0:
        print("{}".format(size), "arguments.")
    elif size == 1:
        print("{}".format(size), "argument:")
    else:
        print("{}".format(size), "arguments:")

    for i in range(1, len(argv)):
        print("{}:".format(i), argv[i])


if __name__ == "__main__":
    main()
