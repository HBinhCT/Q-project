#!/bin/python3

import os


#
# Complete the playWithWords function below.
#
def playWithWords(s):
    #
    # Write your code here.
    #
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(1, n):
        for j in range(n - i):
            if s[j] == s[j + i]:
                dp[j][j + i] = dp[j + 1][j + i - 1] + 2
            else:
                dp[j][j + i] = max(dp[j + 1][j + i], dp[j][j + i - 1])
    ans = 0
    for i in range(n - 1):
        ans = max(ans, dp[0][i] * dp[i + 1][n - 1])
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = playWithWords(s)

    fptr.write(str(result) + '\n')

    fptr.close()
