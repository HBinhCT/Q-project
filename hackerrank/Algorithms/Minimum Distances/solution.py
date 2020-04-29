#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumDistances function below.
def minimumDistances(a):
    stash = dict()
    min_d = len(a)
    for i, v in enumerate(a):
        d = i - stash.setdefault(v, i)
        if d > 0:
            if d == 1:
                return d
            min_d = min(min_d, d)
    return min_d if min_d < len(a) else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
