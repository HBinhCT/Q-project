#!/bin/python3

import os
import sys


#
# Complete the summingPieces function below.
#
def summingPieces(arr):
    #
    # Write your code here.
    #
    from collections import defaultdict

    dp = defaultdict(list)
    n = len(arr)
    mod = 1000000007  # 10 ** 9 + 7
    contributions = [0] * ((n + 1) // 2)
    contributions[0] = pow(2, n, mod) - 1  # 2 ** n % mod - 1
    for i in range(1, (n + 1) // 2):
        contributions[i] = (contributions[i - 1] + pow(2, n - 1 - i, mod) - pow(2, i - 1, mod)) % mod
    dp[n] = contributions + contributions[:n // 2][::-1]
    return sum((dp[n][i] * arr[i]) % mod for i in range(n)) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
