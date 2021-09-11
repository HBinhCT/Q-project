#!/bin/python3


#
# Complete the kMarsh function below.
#
def kMarsh(grid):
    #
    # Write your code here.
    #
    rows = len(grid)
    cols = len(grid[0])
    up = [[0] * cols for _ in range(rows)]
    left = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if j > 0:
                left[i][j] = left[i][j - 1] + 1 if grid[i][j - 1] != 'x' else 0
            if i > 0:
                up[i][j] = up[i - 1][j] + 1 if grid[i - 1][j] != 'x' else 0
    max_perimeter = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] != 'x':
                a = i - up[i][j]
                b = 0
                while a < i and 2 * (i - a) + 2 * (j - b) > max_perimeter:
                    b = max(j - left[a][j], j - left[i][j])
                    while up[i][b] < i - a and b < j and 2 * (i - a) + 2 * (j - b) > max_perimeter:
                        b += 1
                    if b < j and left[i][j] >= j - b and grid[a][b] != 'x':
                        max_perimeter = max(max_perimeter, 2 * (i - a) + 2 * (j - b))
                    a += 1
                    b = 0
    print(max_perimeter if max_perimeter > 0 else 'impossible')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    grid = []

    for _ in range(m):
        grid_item = input()
        grid.append(grid_item)

    kMarsh(grid)
