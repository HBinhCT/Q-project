#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    n = len(a)
    m = len(b)
    lcs = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[j - 1] == b[i - 1]:
                lcs[i][j] = 1 + lcs[i - 1][j - 1]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    i = m
    j = n
    common = []
    while i > 0 and j > 0:
        if a[j - 1] == b[i - 1]:
            common.append(a[j - 1])
            i -= 1
            j -= 1
        else:
            if lcs[i - 1][j] > lcs[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return common[::-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
