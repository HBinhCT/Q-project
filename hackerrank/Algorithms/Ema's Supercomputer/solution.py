#!/bin/python3

import os


# Complete the twoPluses function below.
def twoPluses(grid):
    h, w = len(grid), len(grid[0])
    mn = min(h, w)
    plus = []
    is_good = lambda row, col: grid[row][col] == 'G'
    how = lambda x: 2 * x - 1
    for step in range(1, mn // 2 + (1 if mn % 2 else 0)):
        for r in range(step, h - step):
            for c in range(step, w - step):
                if is_good(r, c):
                    s1 = {(r1, c) for r1 in range(r - 1, r - step - 1, -1) if is_good(r1, c)}
                    s2 = {(r1, c) for r1 in range(r + 1, r + step + 1, +1) if is_good(r1, c)}
                    s3 = {(r, c1) for c1 in range(c - 1, c - step - 1, -1) if is_good(r, c1)}
                    s4 = {(r, c1) for c1 in range(c + 1, c + step + 1, +1) if is_good(r, c1)}
                    if len(s1) == len(s2) == len(s3) == len(s4) == step:
                        plus.append((how(2 * step + 1), {(r, c)} | s1 | s2 | s3 | s4))
    if not plus:
        return 1
    if len(plus) == 1:
        return plus.pop()[0]
    from itertools import combinations
    combs = [s1 * s2 for (s1, a), (s2, b) in combinations(plus, 2) if a.isdisjoint(b)]
    return max(combs) if combs else plus.pop()[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
