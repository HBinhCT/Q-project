#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sansaXor function below.
def sansaXor(arr):
    import functools
    import operator
    return 0 if len(arr) % 2 == 0 else functools.reduce(operator.xor, arr[::2])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
