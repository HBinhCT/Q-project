#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the cost function below.
def cost(B):
    low, high = 0, 0
    for i in range(1, len(B)):
        curr, prev = B[i], B[i - 1]
        low, high = max(low, high + prev - 1), max(high + abs(curr - prev), low + curr - 1)
    return max(low, high)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
