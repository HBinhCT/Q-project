#!/bin/python3

import os
import sys


def nck(n, k):
    from math import factorial
    res = 0
    for i in range(k + 1):
        res += factorial(n) // (factorial(i) * factorial(n - i))
    return res


def divisors(n):
    from math import sqrt
    d1 = [1]
    d2 = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            d1.append(i)
            if i * i != n:
                d2.append(n // i)
    d1.extend(d2[::-1])
    return d1


#
# Complete the stringTransmission function below.
#
def stringTransmission(k, s):
    #
    # Write your code here.
    #
    ln = len(s)
    if ln == 1:
        return ln + k
    total = nck(ln, k)
    div = divisors(ln)
    dp = [[0] * (ln + k + 1) for _ in range(len(div))]
    is_periodic = 0
    for i, d in enumerate(div):
        dp[i][0] = 1
        for offset in range(d):
            zeros = 0
            for j in range(offset, ln, d):
                if s[j] == "0":
                    zeros += 1
            ones = ln // d - zeros
            prev = list(dp[i])
            dp[i][:] = [0] * (ln + k + 1)
            for j in range(k + 1):
                if prev[j]:
                    dp[i][j + zeros] += prev[j]
                    dp[i][j + ones] += prev[j]
        if dp[i][0]:
            is_periodic = 1
        for x in range(i):
            y = div[x]
            if d % y == 0:
                for j in range(k + 1):
                    dp[i][j] -= dp[x][j]
        for j in range(1, k + 1):
            total -= dp[i][j]
    return (total - is_periodic) % 1000000007


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().strip().split()

        n = int(nk[0])

        k = int(nk[1])

        s = input().strip()

        result = stringTransmission(k, s)

        fptr.write(str(result) + '\n')

    fptr.close()
