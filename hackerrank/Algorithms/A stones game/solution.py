#!/bin/python3

import os


#
# Complete the half function below.
#
def half(n):
    #
    # Write your code here.
    #
    from math import frexp

    if n & 1:
        return 1
    x = 1 ^ int(frexp(n)[-1])
    y = 1 << int(frexp(x)[-1] - 1)
    return 1 << y - 2 if (x ^ y) + 1 == y else (1 << y - 1) - (1 << (x ^ y)) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = half(n)

        fptr.write(str(result) + '\n')

    fptr.close()
