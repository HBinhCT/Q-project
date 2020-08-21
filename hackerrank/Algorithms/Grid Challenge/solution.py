#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridChallenge function below.
def gridChallenge(grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        grid[i] = sorted(grid[i])
    for i in range(rows - 1):
        for j in range(cols):
            if grid[i][j] > grid[i + 1][j]:
                return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
