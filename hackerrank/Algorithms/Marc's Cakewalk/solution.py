#!/bin/python3

import os


# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    from functools import reduce

    return reduce(lambda x, y: 2 * x + y, sorted(calorie))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
