#!/usr/bin/python3
def main():
    from add_0 import add
    a = 1
    b = 2
    sum = add(a, b)
    print(a, "{}".format("+"), b, "=", sum)

if __name__ == "__main__":
    main()
