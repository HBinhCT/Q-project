#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bomberMan function below.
def bomberMan(n, grid):
    if n in [0, 1]:
        return grid
    elif n % 2 == 0:
        return ['O' * len(row) for row in grid]
    else:
        # replace symbols and split rows into list
        g = [list(map(int, list(x.replace('O', '2').replace('.', '0')))) for x in grid]
        rows = len(g)
        cols = len(g[0])
        for t in range(2, (4 + n % 4) + 1):
            # each second check whole grid
            destroyed = []  # for location of cells that will explode
            for row in range(rows):
                for col in range(cols):
                    if g[row][col] > 0:
                        # decrease bomb timer (simultaneously with either planting or explosion)
                        g[row][col] -= 1
                    if t % 2 == 0 and g[row][col] == 0:
                        # plant
                        g[row][col] = 3
                    elif g[row][col] == 0:
                        destroyed.append((row, col))
                        if row > 0:
                            destroyed.append((row - 1, col))
                        if row < rows - 1:
                            destroyed.append((row + 1, col))
                        if col > 0:
                            destroyed.append((row, col - 1))
                        if col < cols - 1:
                            destroyed.append((row, col + 1))
            if destroyed:
                for row, col in set(destroyed):
                    g[row][col] = 0
        # convert lists to strings
        return [''.join(list(map(str, x))).replace('2', 'O').replace('0', '.') for x in g]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
