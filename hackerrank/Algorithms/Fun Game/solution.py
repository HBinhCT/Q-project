#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the funGame function below.
def funGame(a, b):
    ln = len(a)
    totals = [a[i] + b[i] for i in range(ln)]
    add = turn = 0
    for i in range(ln):
        idx = totals.index(max(totals))
        if turn == 0:
            add += a[idx]
        if turn == 1:
            add -= b[idx]
        totals.pop(idx)
        a.pop(idx)
        b.pop(idx)
        turn = 1 - turn
    if add > 0:
        return 'First'
    elif add < 0:
        return 'Second'
    else:
        return 'Tie'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = funGame(a, b)

        fptr.write(result + '\n')

    fptr.close()
