#!/bin/python3

import os


# Complete the flippingBits function below.
def flippingBits(n):
    return 2 ** 32 - (n + 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
