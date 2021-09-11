#!/bin/python3

import os


# Complete the winner function below.
def winner(A):
    # Return the name of the winner of the game
    from functools import reduce
    from operator import xor

    # [0, 0, 1, 1, 2, 2, 3, 3, 4]
    return 'Manasa' if reduce(xor, (i % 9 // 2 for i in A)) else 'Sandy'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = winner(A)

        fptr.write(result + '\n')

    fptr.close()
