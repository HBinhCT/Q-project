#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the longestIncreasingSubsequence function below.
def longestIncreasingSubsequence(arr):
    from bisect import bisect_left

    ln = len(arr)
    x = [0] * ln
    res = 1
    x[0] = arr[0]
    for i in range(1, ln):
        if arr[i] < x[0]:
            x[0] = arr[i]
        elif arr[i] > x[res - 1]:
            x[res] = arr[i]
            res += 1
        else:
            j = bisect_left(x[:res], arr[i])
            x[j] = arr[i]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
