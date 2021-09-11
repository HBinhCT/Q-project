#!/bin/python3

import os


#
# Complete the verticalRooks function below.
#
def verticalRooks(r1, r2):
    #
    # Write your code here.
    #
    from functools import reduce
    from operator import xor

    return 'player-2' if reduce(xor, (abs(r1[i] - r2[i]) - 1 for i in range(len(r1)))) else 'player-1'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        r1 = []

        for _ in range(n):
            r1_item = int(input())
            r1.append(r1_item)

        r2 = []

        for _ in range(n):
            r2_item = int(input())
            r2.append(r2_item)

        result = verticalRooks(r1, r2)

        fptr.write(result + '\n')

    fptr.close()
