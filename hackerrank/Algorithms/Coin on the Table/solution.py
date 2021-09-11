#!/bin/python3

import os


#
# Complete the coinOnTheTable function below.
#
def coinOnTheTable(m, k, board):
    #
    # Write your code here.
    #
    from functools import lru_cache

    rows = len(board)
    cols = len(board[0])
    directions = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}

    @lru_cache(None)
    def dp(i, j, k):
        if k < 0:
            return float('inf')
        if not (0 <= i < rows and 0 <= j < cols):
            return float('inf')
        if board[i][j] == '*':
            return 0
        return min((d != board[i][j]) + dp(i + x, y + j, k - 1) for d, (x, y) in directions.items())

    ans = dp(0, 0, k)
    return ans if ans != float('inf') else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    board = []

    for _ in range(n):
        board_item = input()
        board.append(board_item)

    result = coinOnTheTable(m, k, board)

    fptr.write(str(result) + '\n')

    fptr.close()
