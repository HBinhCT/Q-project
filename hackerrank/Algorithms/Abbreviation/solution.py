#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the abbreviation function below.
def abbreviation(a, b):
    a = "." + a
    b = "." + b
    dp = [[0] * len(b) for _ in range(len(a))]
    dp[0][0] = True
    for i in range(1, len(a)):
        for j in range(min(len(b), i + 1)):
            dp[i][j] = a[i].islower() and dp[i - 1][j] or a[i].upper() == b[j] and dp[i - 1][j - 1]
    return ['NO', 'YES'][dp[len(a) - 1][len(b) - 1]]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
