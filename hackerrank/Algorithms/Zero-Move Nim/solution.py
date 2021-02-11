#!/bin/python3

import os
import sys


#
# Complete the zeroMoveNim function below.
#
def zeroMoveNim(p):
    #
    # Write your code here.
    #
    import functools
    import operator

    q = [i - 1 + 2 * (i % 2) for i in p]
    return 'W' if functools.reduce(operator.xor, q) else 'L'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        p = list(map(int, input().rstrip().split()))

        result = zeroMoveNim(p)

        fptr.write(str(result) + '\n')

    fptr.close()
