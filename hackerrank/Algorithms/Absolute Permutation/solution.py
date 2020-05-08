#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k == 0:
        for i in range(1, n + 1):
            yield i
    elif n % (2 * k) != 0 or 2 * k > n:
        yield -1
    else:
        for i in range(1, n + 1):
            yield i + k
            if i % k == 0:
                k *= -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
