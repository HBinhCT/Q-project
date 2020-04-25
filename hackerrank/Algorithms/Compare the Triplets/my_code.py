#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    diff = [(bool(ai - bi), 0) if ai > bi else (0, bool(ai - bi)) for ai, bi in zip(a, b)]
    return list(map(sum, zip(*diff)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
