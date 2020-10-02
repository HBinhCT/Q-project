#!/bin/python3

import os
import sys


#
# Complete the beautifulPermutations function below.
#
def beautifulPermutations(arr):
    #
    # Write your code here.
    #
    import math

    mod = 1000000007  # 10 ** 9 + 7
    length = len(arr)
    repetitions = length - len(set(arr))
    perm = 0
    mat = 1
    for i in range(repetitions + 1):
        perm += (-1) ** i * mat * math.factorial(length - i) // (2 ** (repetitions - i))
        perm %= mod
        mat = mat * (repetitions - i) // (i + 1)
    return perm % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = beautifulPermutations(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
