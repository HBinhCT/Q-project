#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY shots
#  2. 2D_INTEGER_ARRAY players
#

def solve(shots, players):
    # Write your code here
    from bisect import bisect_left, bisect_right

    start, end = [], []
    for a, b in shots:
        start.append(a)
        end.append(b)
    start.sort()
    end.sort()
    ans = 0
    for c, d in players:
        ans += bisect_right(start, d) - bisect_left(end, c)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    shots = []

    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))

    players = []

    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))

    result = solve(shots, players)

    fptr.write(str(result) + '\n')

    fptr.close()
