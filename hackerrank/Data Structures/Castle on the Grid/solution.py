#!/bin/python3

import os


#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    from collections import deque

    size = len(grid)
    visited = [[False] * size for _ in range(size)]
    queue = deque([(startX, startY, 0)])
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while queue:
        x, y, d = queue.pop()
        nd = d + 1
        for mx, my in moves:
            nx = x + mx
            ny = y + my
            while 0 <= nx < size and 0 <= ny < size and grid[nx][ny] != 'X':
                if (nx, ny) == (goalX, goalY):
                    return nd
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.appendleft((nx, ny, nd))
                nx += mx
                ny += my


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
