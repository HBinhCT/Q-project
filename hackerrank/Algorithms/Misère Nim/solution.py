#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the misereNim function below.
def misereNim(s):
    import functools
    import operator

    if set(s) == {1}:
        return 'Second' if len(s) % 2 else 'First'
    return 'First' if functools.reduce(operator.xor, s) else 'Second'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
