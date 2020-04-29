#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    ln = len(c)
    energy = 100  # initial energy
    i = k % ln  # initial jump from 0
    energy -= c[i] * 2 + 1  # initial energy loss
    while i != 0:
        i = (i + k) % ln
        energy -= c[i] * 2 + 1
    return energy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
