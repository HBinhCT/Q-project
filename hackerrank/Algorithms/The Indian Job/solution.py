#!/bin/python3

import os
import sys


#
# Complete the indianJob function below.
#
def indianJob(g, arr):
    #
    # Write your code here.
    #
    total = sum(arr)
    possible = [True] + [False] * total
    for i in arr:
        for j in range(total, -1, -1):
            if possible[j]:
                possible[j + i] = True
    for i in range((total + 1) // 2, min(total, g) + 1):
        if possible[i]:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ng = input().split()

        n = int(ng[0])

        g = int(ng[1])

        arr = list(map(int, input().rstrip().split()))

        result = indianJob(g, arr)

        fptr.write(result + '\n')

    fptr.close()
