#!/bin/python3

import os


# Complete the isValid function below.
def isValid(s):
    from collections import Counter
    freq = Counter(s)
    values = sorted(freq.values())
    if values.count(values[0]) == len(values) or (
            values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1) or (
            values.count(values[-1]) == len(values) - 1 and values[0] == 1):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
