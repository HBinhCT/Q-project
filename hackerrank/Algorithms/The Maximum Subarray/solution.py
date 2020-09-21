#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxSubarray function below.
def maxSubarray(arr):
    subarray_sum = arr[0]
    subsequence_sum = arr[0]
    current_sum = arr[0]
    for ind, val in enumerate(arr[1:], 1):
        subsequence_sum = max(subsequence_sum, val, subsequence_sum + val)
        current_sum = max(val, current_sum + val)
        subarray_sum = max(subarray_sum, current_sum)
    return [subarray_sum, subsequence_sum]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
