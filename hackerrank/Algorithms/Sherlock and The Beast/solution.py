#!/bin/python3


# Complete the decentNumber function below.
def decentNumber(n):
    if n % 3 == 0 and n != 0:
        print('5' * n)
    elif n % 3 == 1 and n >= 10:
        print('5' * (n - 10) + '3' * 10)
    elif n % 3 == 2 and n >= 5:
        print('5' * (n - 5) + '3' * 5)
    else:
        print('-1')


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
