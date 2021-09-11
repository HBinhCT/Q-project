#!/bin/python3

import os


# Complete the lonelyinteger function below.
def lonelyinteger(a):
    from functools import reduce
    from operator import xor

    return reduce(xor, a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
