#!/bin/python3

import os


# Complete the counterGame function below.
def counterGame(n):
    if n == 1:
        return 'Richard'
    return 'Louise' if (bin(n - 1)[2:].count('1')) % 2 else 'Richard'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
