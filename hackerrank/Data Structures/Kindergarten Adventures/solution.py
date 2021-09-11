#!/bin/python3

import os


#
# Complete the solve function below.
#
def solve(t):
    #
    # Return the ID
    #
    ln = len(t)
    diagonals = [0] * ln
    values = [0] * ln
    for i, time in enumerate(t):
        diagonals[i - time] += 1
        values[0] += (time <= i)
    for i in range(1, ln):
        values[i] = values[i - 1] - diagonals[i - 1] + 1
    return values.index(max(values)) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_count = int(input())

    t = list(map(int, input().rstrip().split()))

    id = solve(t)

    fptr.write(str(id) + '\n')

    fptr.close()
