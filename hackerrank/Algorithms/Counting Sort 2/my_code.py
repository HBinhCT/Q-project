#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingSort function below.
def countingSort(arr):
    count = [0] * 100
    output = []
    for i in arr:
        count[i] += 1
    for i in range(100):
        output += [i] * count[i]
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
