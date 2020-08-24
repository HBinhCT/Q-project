#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the candies function below.
def candies(n, arr):
    counter = [1]
    for i, x in enumerate(arr[1:], 1):
        if x <= arr[i - 1]:
            counter.append(1)
        else:
            counter.append(counter[i - 1] + 1)
    for i, x in enumerate(arr[-2::-1], 2):
        if x <= arr[n - i + 1]:
            counter[n - i] = max(counter[n - i], 1)
        else:
            counter[n - i] = max(counter[n - i], counter[n - i + 1] + 1)
    return sum(counter)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
