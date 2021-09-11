#!/bin/python3

import os


# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    from collections import deque

    paths = dict(ladders + snakes)
    queue = deque([(1, 0)])
    visited = set()
    while queue:
        square, rolls = queue.popleft()
        if 100 == square:
            return rolls
        visited.add(square)
        for i in range(1, 7):
            move = square + i
            if move not in visited and move <= 100:
                queue.append((move in paths and paths[move] or move, rolls + 1))
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
