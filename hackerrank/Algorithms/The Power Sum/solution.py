#!/bin/python3

import os


# Complete the powerSum function below.
def powerSum(X, N):
    dp = [1] + [0] * X
    for i in range(1, int(pow(X, 1 / N)) + 1):
        k = i ** N
        for j in range(X, k - 1, -1):
            dp[j] += dp[j - k]
    return dp[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
