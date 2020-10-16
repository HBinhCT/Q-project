#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the stringReduction function below.
def stringReduction(s):
    n = len(s)
    a, b, c = [s.count(c) for c in 'abc']
    if n in (a, b, c):
        return n
    if a % 2 == b % 2 == c % 2:
        return 2
    return 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = stringReduction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
