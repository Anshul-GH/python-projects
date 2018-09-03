# Find PI to the Nth Digit
# Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.


def printPi(n):
    # numerator for Pi
    num = 22
    # denominator for Pi
    den = 7

    # innovative way to dynamically incorporate the precision specifier while using the format function.
    valPi = ("{:."+n+"f}").format(float(num/den))
    print(valPi)


if __name__ == '__main__':
    n = input('Please specify the precision for Pi value to be printed:')
    printPi(n)