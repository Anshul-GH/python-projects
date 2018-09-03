# Find exponential power to e to the Nth Digit
# Enter a number and have the program generate e**(n) up to that many decimal places.
# Keep a limit to how far the program will go.
from math import e


def printE(n):
    # innovative way to dynamically incorporate the precision specifier while using the format function.
    valE = ("{:."+n+"f}").format(e)
    print(valE)


if __name__ == '__main__':
    n = input('Please specify the exponent for e to be used:')
    printE(n)