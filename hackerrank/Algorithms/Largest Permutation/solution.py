#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    ln = len(arr)
    if k >= int(ln * math.log(ln)):
        return sorted(arr, reverse=True)
    i = 0
    lookup = {v: i for i, v in enumerate(arr)}
    while i != k:
        num = ln - i
        if arr[i] != num:
            index = lookup[num]
            lookup[arr[i]] = index
            arr[i], arr[index] = arr[index], arr[i]
        else:
            k = min(k + 1, ln)
        i += 1
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
