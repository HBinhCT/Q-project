#!/bin/python3

import os


# Complete the fairRations function below.
def fairRations(B):
    total = 0
    for i in range(len(B) - 1):
        if B[i] % 2:
            total += 2
            B[i + 1] += 1
    return 'NO' if B[-1] % 2 else total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
