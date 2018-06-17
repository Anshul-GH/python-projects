# Find PI to the Nth Digit
# Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.
from math import pi


def printPi(n):
    # numerator for Pi
    num = 22
    # denominator for Pi
    den = 7

    # The code will compare the built in pi value with the calculated value(22/7).

    # innovative way to dynamically incorporate the precision specifier while using the format function.
    valPi = ("{:."+n+"f}").format(pi)
    print(valPi)
    valPi = ("{:." + n + "f}").format(float(num / den))
    print(valPi)


if __name__ == '__main__':
    f = 1
    while(f == 1):
        n = input('Please specify the precision for Pi value to be printed:')
        printPi(n)
        f = int(input('Run Again? (Yes-1/No-0):\n'))
