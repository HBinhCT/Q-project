#!/bin/python3

import os


#
# Complete the stoneDivision function below.
#
def stoneDivision(n, s):
    #
    # Write your code here.
    #
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def splitting(x):
        for v in s:
            if x % v == 0 and not splitting(x // v):
                return True
        return False

    if n % 2 == 0:
        for i in s:
            if i % 2 == 0 and n % i == 0:
                return 'First'
    return 'First' if splitting(n) else 'Second'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    s = list(map(int, input().rstrip().split()))

    result = stoneDivision(n, s)

    fptr.write(result + '\n')

    fptr.close()
