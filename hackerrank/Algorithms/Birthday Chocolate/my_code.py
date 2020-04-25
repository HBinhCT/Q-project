#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    total = count = 0
    for i in range(len(s)):
        total += s[i]
        # M is never less than 1
        if i > m - 1:
            total -= s[i - m]
        if i >= m - 1 and total == d:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
