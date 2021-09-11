#!/bin/python3

import os


# Complete the countingValleys function below.
def countingValleys(n, s):
    level = valleys = 0
    for step in s:
        level += -1 if step == 'D' else 1
        valleys += level == 0 and step == 'U'
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
