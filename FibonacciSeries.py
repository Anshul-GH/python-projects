# Fibonacci Sequence
# Enter a number and have the program generate the
# Fibonacci sequence to that number or to the Nth number.


def generateFibonacci(n):
    # initialize the variables
    a = 1
    b = 1
    cnt = 0
    fiboSer = list()
    fiboSer.append(a)
    fiboSer.append(b)
    while cnt < n-2:
        tmp = b
        b = a + b
        a = tmp
        fiboSer.append(b)
        cnt += 1

    print('Fibonacci Series (length ', n, '):', fiboSer)


if __name__ == '__main__':
    flg=1
    while flg==1:
        n = int(input('Please specify count of number required in the series:'))
        generateFibonacci(n)
        flg = int(input('Run Again? (Yes-1/No-0):\n'))
