#!/bin/python3

import os


# Complete the gameOfStones function below.
def gameOfStones(n):
    return ['First', 'Second'][n % 7 in [0, 1]]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
