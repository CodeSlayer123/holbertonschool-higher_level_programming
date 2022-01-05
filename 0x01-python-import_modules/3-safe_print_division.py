#!/usr/bin/python3
def main():
    def safe_print_division(a, b):
        try:
            product = a / b
        except:
            product = None
        finally:
            print("Inside result: {}".format(product))
            return(product)

if __name__ == "__main__":
    main():
