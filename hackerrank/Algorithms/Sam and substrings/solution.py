#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrings function below.
def substrings(n):
    mod = 1000000007  # 10 ** 9 + 7
    res = 0
    f = 1
    for i in range(len(n) - 1, -1, -1):
        res = (res + int(n[i]) * f * (i + 1)) % mod
        f = (f * 10 + 1) % mod
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
