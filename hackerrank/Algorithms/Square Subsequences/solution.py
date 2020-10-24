#!/bin/python3

import os
import sys


#
# Complete the squareSubsequences function below.
#
def squareSubsequences(s):
    #
    # Write your code here.
    #
    from functools import lru_cache

    mod = 1000000007

    @lru_cache()
    def count(s1, s2):
        n = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    n[i][j] = n[i - 1][j] + n[i][j - 1] + 1
                else:
                    n[i][j] = n[i - 1][j] + n[i][j - 1] - n[i - 1][j - 1]
                n[i][j] %= mod
        return n[-1][-1] % mod

    total = 0
    for i in range(1, len(s)):
        total += count(s[:i], s[i:]) - count(s[:i - 1], s[i:])
    return total % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = squareSubsequences(s)

        fptr.write(str(result) + '\n')

    fptr.close()
