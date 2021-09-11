#!/bin/python3

import os


# Complete the anotherMinimaxProblem function below.
def anotherMinimaxProblem(a):
    if sum(a) == 0:
        return 0
    bits = un_bits = 0
    for i in a:
        bits |= i
        un_bits |= ~i
    j = bits & un_bits
    while j & (j - 1):
        j &= j - 1
    xs = [i for i in a if i & j]
    ys = [i for i in a if i & j == 0]
    return min(x ^ y for x in xs for y in ys)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = anotherMinimaxProblem(a)

    fptr.write(str(result) + '\n')

    fptr.close()
