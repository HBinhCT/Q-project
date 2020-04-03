#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr = sorted(arr)
    diff = []
    for i in range(len(arr) - 1):
        diff.append(arr[i + 1] - arr[i])
    value = min(diff)
    res = []
    for i in range(len(arr) - 1):
        if (arr[i + 1] - arr[i]) == value:
            res.append(arr[i])
            res.append(arr[i + 1])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
