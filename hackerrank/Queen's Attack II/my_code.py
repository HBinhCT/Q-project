#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    cell = set([(x, y) for y, x in obstacles])
    move = [
        [-1, 1], [0, 1], [1, 1],
        [-1, 0], [1, 0],
        [-1, -1], [0, -1], [1, -1]
    ]
    num = 0
    for position in move:
        x = c_q
        y = r_q
        while True:
            x += position[0]
            y += position[1]
            if x == 0 or x == n + 1 or y == 0 or y == n + 1:
                break
            if (x, y) in cell:
                break
            num += 1
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
