#!/bin/python3

import os
import sys


#
# Complete the simplifiedChessEngine function below.
#
def simplifiedChessEngine(whites, blacks, moves):
    #
    # Write your code here.
    #
    from functools import lru_cache

    n = 4
    d = (
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 1),
        (-1, 1),
        (-1, -1),
        (1, -1),
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1)
    )
    figures = 'QNBR'
    ranges = ((0, 8), (8, 16), (4, 8), (0, 4))

    @lru_cache(maxsize=None)
    def search(board, step):
        white = (step % 2 == 1)
        for i in range(n):
            for j in range(n):
                field = board[i][j]
                if field == 0 or (field > 0) != white:
                    continue
                for k in range(*ranges[abs(field) - 1]):
                    dx, dy = d[k]
                    x, y = i, j
                    while True:
                        x += dx
                        y += dy
                        if x < 0 or x >= n or y < 0 or y >= n:
                            break
                        pos = board[x][y]
                        if pos != 0 and (pos > 0) == (field > 0):
                            break
                        if abs(pos) == 1:
                            return white
                        if step > 1:
                            new = list(map(list, board))
                            new[i][j] = 0
                            new[x][y] = field
                            new = tuple(map(tuple, new))
                            res = search(new, step - 1)
                            if white == res:
                                return res
                        if pos:
                            break
        return not white

    lw = len(whites)
    moves -= (moves + 1) % 2
    fields = [[0] * n for _ in range(n)]
    for index, val in enumerate(whites + blacks):
        figure, col, row = val
        col = ord(col) - ord('A')
        row = int(row) - 1
        figure = figures.find(figure) + 1
        if index >= lw:
            figure *= -1
        fields[row][col] = figure
    return 'YES' if search(tuple(map(tuple, fields)), moves) else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        wbm = input().split()

        w = int(wbm[0])

        b = int(wbm[1])

        m = int(wbm[2])

        whites = []

        for _ in range(w):
            whites.append(list(map(lambda x: x[0], input().rstrip().split())))

        blacks = []

        for _ in range(b):
            blacks.append(list(map(lambda x: x[0], input().rstrip().split())))

        result = simplifiedChessEngine(whites, blacks, m)

        fptr.write(result + '\n')

    fptr.close()
