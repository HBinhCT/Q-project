#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the connectedCell function below.
def connectedCell(matrix):
    largest = 0
    filled = [(i, j) for i, row in enumerate(matrix) for j, cell in enumerate(row) if cell]
    while filled:
        regions = [filled.pop()]
        count = 0
        while regions:
            region = regions.pop()
            count += 1
            for fill in list(filled):
                if abs(region[0] - fill[0]) <= 1 and abs(region[1] - fill[1]) <= 1:
                    regions.append(fill)
                    filled.remove(fill)
        else:
            largest = max(largest, count)
    return largest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
