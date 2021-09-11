#!/bin/python3

import os

from functools import lru_cache


# precompute the Sprague-Grundy (SG) function for all 0 <= i <= 300
# 1 <= n <= 300
@lru_cache(maxsize=1)
def precompute():
    g = [0, 1, 2]
    for i in range(3, 301):
        s = set()
        # hit one or two pins
        for j in (1, 2):
            # the group of i pins can be split into two
            # group of i and i - j - k pins
            for k in range((i - j) // 2 + 1):
                s.add(g[k] ^ g[i - j - k])
        # compute mex (minimum excluded value)
        m = 0
        while m in s:
            m += 1
        g.append(m)
    return g


#
# Complete the isWinning function below.
#
def isWinning(n, config):
    #
    # Return WIN or LOSE depending on whether you will win
    #
    ret = 0
    groups = precompute()
    # split the pins into groups and xor the SG values
    for p in config.strip().split('X'):
        ret ^= groups[len(p)]
    return 'WIN' if ret else 'LOSE'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        config = input()

        result = isWinning(n, config)

        fptr.write(result + '\n')

    fptr.close()
