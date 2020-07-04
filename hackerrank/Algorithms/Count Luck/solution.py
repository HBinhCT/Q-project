#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countLuck function below.
def countLuck(matrix, k):
    def time_wave(row, col, turns):
        if not 0 <= row < rows or not 0 <= col < cols:
            return None
        elif grid[row][col] == 'X':
            return None
        elif grid[row][col] == '*':
            return turns

        path = 0
        non_block = ('.', '*')
        if row > 0 and grid[row - 1][col] in non_block:
            path += 1
        if row < rows - 1 and grid[row + 1][col] in non_block:
            path += 1
        if col > 0 and grid[row][col - 1] in non_block:
            path += 1
        if col < cols - 1 and grid[row][col + 1] in non_block:
            path += 1

        if path > 1:
            turns += 1
            grid[row][col] = '1'
        else:
            grid[row][col] = '0'
        for x, y in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if not 0 <= x < rows or not 0 <= y < cols:
                continue
            if grid[x][y] in ('1', '0'):
                continue
            times = time_wave(x, y, turns)  # RECURSION CALL!
            if times is None:
                continue
            else:
                return times

    rows = len(matrix)
    cols = len(matrix[0])
    # find position M
    position = (0, 0)
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(matrix[i][j])
            if matrix[i][j] == 'M':
                position = (i, j)
    # find k times to wave
    count = time_wave(position[0], position[1], 0)
    return 'Impressed' if count == k else 'Oops!'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
