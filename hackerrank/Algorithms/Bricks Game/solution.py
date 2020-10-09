#!/bin/python3

import os
import sys


#
# Complete the bricksGame function below.
#
def bricksGame(arr):
    #
    # Write your code here.
    #
    n = len(arr)
    dp = [0] * (n + 4)
    s = 0
    for i in range(n - 1, -1, -1):
        s += arr[i]
        dp[i] = s - (min(dp[i + 1], dp[i + 2], dp[i + 3]))
    return dp[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = bricksGame(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
