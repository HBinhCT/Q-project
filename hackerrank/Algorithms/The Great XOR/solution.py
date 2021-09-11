#!/bin/python3

import os


# Complete the theGreatXor function below.
def theGreatXor(x):
    return 2 ** (len(bin(x)) - 2) - 1 - x


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
