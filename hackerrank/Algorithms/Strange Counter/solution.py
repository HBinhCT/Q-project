#!/bin/python3

import math
import os


# Complete the strangeCounter function below.
def strangeCounter(t):
    return 6 * 2 ** int(math.log2((t + 2) / 3)) - (t + 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
