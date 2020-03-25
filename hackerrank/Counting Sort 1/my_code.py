#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingSort function below.
def countingSort(arr):
    sol = [0] * 100
    for i in arr:
        sol[i] += 1
    return sol


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
