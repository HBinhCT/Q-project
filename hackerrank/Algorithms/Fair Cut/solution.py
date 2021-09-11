#!/bin/python3

import os


#
# Complete the fairCut function below.
#
def fairCut(k, arr):
    #
    # Write your code here.
    #
    ln = len(arr)
    if k > ln // 2:
        k = ln - k
    arr.sort()
    dp = [[float('inf')] * (ln + 1) for _ in range(ln + 1)]
    dp[0][0] = 0
    for i in range(0, ln):
        for j in range(0, i + 1):
            if j > k or i - j > ln - k:
                continue
            temp_li = dp[i][j] + arr[i] * (i - j - (ln - k - (i - j)))
            temp_lu = dp[i][j] + arr[i] * (j - (k - j))
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], temp_li)
            dp[i + 1][j] = min(dp[i + 1][j], temp_lu)
    return dp[ln][k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
