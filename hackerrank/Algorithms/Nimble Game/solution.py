#!/bin/python3

import os


# Complete the nimbleGame function below.
def nimbleGame(s):
    import functools
    import operator

    return 'First' if functools.reduce(operator.xor, [i if s[i] % 2 else 0 for i in range(1, len(s))], 0) else 'Second'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)

        fptr.write(result + '\n')

    fptr.close()
