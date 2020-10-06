#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the mandragora function below.
def mandragora(H):
    ans = s = sum(H)
    for hp, j in enumerate(sorted(H), start=2):
        s -= j
        ans = max(ans, hp * s)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        H = list(map(int, input().rstrip().split()))

        result = mandragora(H)

        fptr.write(str(result) + '\n')

    fptr.close()
