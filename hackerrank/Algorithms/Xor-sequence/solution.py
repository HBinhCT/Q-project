#!/bin/python3

import os


# Complete the xorSequence function below.
def xorSequence(l, r):
    def xor_sum(n):
        m = n % 8
        if m == 1 or m == 2:
            return n - 1
        if m == 3 or m == 4:
            return 2
        if m == 5 or m == 6:
            return n + 1
        if m == 7 or m == 0:
            return 0

    return xor_sum(r + 1) ^ xor_sum(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
