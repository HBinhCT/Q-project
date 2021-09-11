#!/bin/python3

import os


# Complete the maximizingXor function below.
def maximizingXor(l, r):
    return max(i ^ j for i in range(l, r + 1) for j in range(i, r + 1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
