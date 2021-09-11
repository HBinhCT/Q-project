#!/bin/python3

import os


# Complete the cavityMap function below.
def cavityMap(grid):
    length = len(grid)
    for i in range(1, length - 1):
        for j in range(1, length - 1):
            if grid[i][j] > max(grid[i][j - 1], grid[i - 1][j], grid[i + 1][j], grid[i][j + 1]):
                grid[i] = grid[i][:j] + 'X' + grid[i][j + 1:]  # 'X' > '9' > '1'
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
