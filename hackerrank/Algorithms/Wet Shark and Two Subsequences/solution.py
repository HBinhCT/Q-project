#!/bin/python3

import os


#
# Complete the twoSubsequences function below.
#
def twoSubsequences(x, r, s):
    #
    # Write your code here.
    #
    if r < s or (r + s) % 2 or (r == 0 and s == 0):
        return 0
    mod = 1000000007  # 10 ** 9 + 7
    ln = len(x)
    dp = [[0] * (ln + 1) for _ in range(r + 1)]
    dp[0][0] = 1
    sum_a = (r + s) // 2
    sum_b = (r - s) // 2
    if x[0] <= sum_a:
        dp[x[0]][1] = 1
    for i in range(1, ln):
        for j in range(sum_a, 0, -1):
            for k in range(1, ln + 1):
                if j >= x[i]:
                    dp[j][k] += dp[j - x[i]][k - 1]
                    dp[j][k] %= mod
    ans = 0
    for i in range(1, ln + 1):
        ans += dp[sum_a][i] * dp[sum_b][i]
        ans %= mod
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mrs = input().split()

    m = int(mrs[0])

    r = int(mrs[1])

    s = int(mrs[2])

    x = list(map(int, input().rstrip().split()))

    result = twoSubsequences(x, r, s)

    fptr.write(str(result) + '\n')

    fptr.close()
