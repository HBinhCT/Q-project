#!/bin/python3

import os


# Complete the permutationEquation function below.
def permutationEquation(p):
    # Each element in the sequence is distinct.
    return [p.index(p.index(i + 1) + 1) + 1 for i in range(len(p))]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
