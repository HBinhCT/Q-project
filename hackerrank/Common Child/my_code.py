#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the commonChild function below.
def commonChild(s1, s2):
    # both string have same length
    prev = [0] * (len(s2) + 1)
    curr = [0] * (len(s2) + 1)
    for r in s1:
        for j, c in enumerate(s2, 1):
            curr[j] = prev[j - 1] + 1 if r == c else max(prev[j], curr[j - 1])
        prev, curr = curr, prev
    return prev[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
