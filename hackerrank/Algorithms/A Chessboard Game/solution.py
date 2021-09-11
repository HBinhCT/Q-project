#!/bin/python3

import os


# Complete the chessboardGame function below.
def chessboardGame(x, y):
    x = x % 4
    y = y % 4
    return 'First' if y == 0 or y == 3 or x == 0 or x == 3 else 'Second'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])

        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()
