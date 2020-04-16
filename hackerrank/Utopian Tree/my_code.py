#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the utopianTree function below.
def utopianTree(n):
    # return ~(~1 << (n >> 1)) << n % 2
    k = n // 2  # 2 cycles of growth every year
    m = 1 if n % 2 == 0 else 2
    return 2 ** (k + m) - m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
