#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    p = [i - 1 for i in q]
    for i, v in enumerate(p):
        if v - i > 2:
            print('Too chaotic')
            return
        for j in range(max(v - 1, 0), i):
            if p[j] > v:
                moves += 1
    print(moves)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
