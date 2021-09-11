#!/bin/python3

import os
from functools import lru_cache
from itertools import count


@lru_cache(maxsize=None)
def get_grundy(x, y):
    can_reach = set()
    for dx, dy in ((-2, 1), (-2, -1), (1, -2), (-1, -2)):
        move_x, move_y = x + dx, y + dy
        if 0 <= move_x < 15 and 0 <= move_y < 15:  # 1 ≤ x, y ≤ 15
            can_reach.add(get_grundy(move_x, move_y))
    for grundy in count(0):
        if grundy not in can_reach:
            return grundy


#
# Complete the chessboardGame function below.
#
def chessboardGame(coins):
    #
    # Write your code here.
    #
    grundy = 0
    for x, y in coins:
        grundy ^= get_grundy(x - 1, y - 1)
    return 'First' if grundy else 'Second'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        k = int(input())

        coins = []

        for _ in range(k):
            coins.append(list(map(int, input().rstrip().split())))

        result = chessboardGame(coins)

        fptr.write(result + '\n')

    fptr.close()
