#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    x.sort()
    loc, i, ln = 0, 0, len(x)
    while i < ln:
        t = x[i]
        while i < ln and x[i] - t <= k:
            i += 1
        loc += 1  # build a antenna
        t = x[i - 1]
        while i < ln and x[i] - t <= k:
            i += 1
    return loc


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
