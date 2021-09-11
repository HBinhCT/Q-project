#!/bin/python3

import os


# Complete the nimGame function below.
def nimGame(pile):
    import functools
    import operator
    return 'First' if functools.reduce(operator.xor, pile) else 'Second'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()
