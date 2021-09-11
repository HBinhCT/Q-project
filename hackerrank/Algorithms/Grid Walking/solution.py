#!/bin/python3

import os


#
# Complete the gridWalking function below.
#
def gridWalking(m, x, D):
    #
    # Write your code here.
    #
    from functools import lru_cache
    from math import factorial

    mod = 1000000007

    @lru_cache(None)
    def c(n, k):
        return (factorial(n) // (factorial(k) * factorial(n - k))) % mod

    # in array i : we could choose to perform k moves (1 <= k <= steps)
    # then the last i-1 array must perform steps - k moves
    # we have C(k, steps) ways to choose time to perform that k moves
    # so dp[i][moves] = sum(dp[i-1][moves-k] * C(k, moves) * ways[curr][k])
    def single(x, upper, steps):
        dp = [0] * (upper + 1)
        dp[x] = 1
        final = [1]
        # final i: number of moves x can make after i steps
        for _ in range(steps):
            curr = [0] * (upper + 1)
            s = 0
            for i in range(1, upper + 1):
                curr[i] = dp[i - 1] + (i + 1 <= upper and dp[i + 1])
                s += curr[i]
            dp = curr
            final.append(s)
        return final

    last = [1] + [0] * m
    for x, upper in zip(x, D):
        curr = [0] * (m + 1)
        ways = single(x, upper, m)
        for step in range(m + 1):
            for k in range(step + 1):
                curr[step] += c(step, k) * ways[k] * last[step - k]
        last = curr
    return last[-1] % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        x = list(map(int, input().rstrip().split()))

        D = list(map(int, input().rstrip().split()))

        result = gridWalking(m, x, D)

        fptr.write(str(result) + '\n')

    fptr.close()
