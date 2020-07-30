#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'clique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def clique(n, m):
    # Write your code here
    low, high = 1, n + 1
    while low + 1 < high:
        mid = (low + high) // 2
        k = turan(n, mid)
        if k < m:
            low = mid
        else:
            high = mid
    return high


def turan(n, r):
    """
    Calculates the number of edges in a Turan graph
    https://en.wikipedia.org/wiki/Tur%C3%A1n_graph
    :param n: vertex (int)
    :param r: max clique (int)
    :return: number of edges
    :rtype: int
    """
    mod = n % r
    upper = math.ceil(n / r)  # ⌈n/r⌉
    lower = math.floor(n / r)  # ⌊n/r⌋
    return (n * n - mod * upper * upper - (r - mod) * lower * lower) // 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = clique(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
