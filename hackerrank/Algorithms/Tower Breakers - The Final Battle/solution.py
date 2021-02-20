#!/bin/python3

import os
import sys


def part(high):
    a = [0] * (high + 1)
    a[0] = 1
    for i in range(1, high + 1):
        j = 1
        while j * j <= i:
            a[i] += a[i - j * j]
            j += 1
    return a


#
# Complete the towerBreakers function below.
#
def towerBreakers(n):
    #
    # Write your code here.
    #
    from bisect import bisect_left

    return bisect_left(part(121), n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = towerBreakers(n)

        fptr.write(str(result) + '\n')

    fptr.close()
