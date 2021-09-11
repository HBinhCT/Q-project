#!/bin/python3

import os


# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    def bfs(a, b, t):
        # i, j, c initial cost is 0
        q = [(0, 0, 0)]
        visited = [[False] * t for _ in range(t)]  # or a cost matrix
        while len(q):
            i, j, c = q.pop()
            if i == t - 1 and j == t - 1:
                # reach the end then this path is valid
                return c
            moves = [
                (i + a, j + b), (i + b, j + a),
                (i + a, j - b), (i + b, j - a),
                (i - a, j + b), (i - b, j + a),
                (i - a, j - b), (i - b, j - a),
            ]
            valid_moves = [(_i, _j) for _i, _j in moves if 0 <= _i < t and 0 <= _j < t]
            # update q, only pushed the unseen
            for _i, _j in valid_moves:
                if not visited[_i][_j]:
                    q.insert(0, (_i, _j, c + 1))
                    # important! this is actually is greedy as it basically declare the first
                    # observation is the lowest cost before we really visit it.
                    # Therefore, we avoid involving this point in the next BFS
                    visited[_i][_j] = True
        return -1  # if we did not exist from the while loop, then we find no path

    cost = [[-1 for _ in range(n - 1)] for _ in range(n - 1)]
    cost[n - 2][n - 2] = 1
    for row in range(n - 1):
        for col in range(row, n - 1):
            if row < n // 2 or col < n // 2:
                cost[row][col] = bfs(row + 1, col + 1, n)
                cost[col][row] = cost[row][col]
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
