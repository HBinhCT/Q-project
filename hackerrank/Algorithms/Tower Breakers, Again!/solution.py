#!/bin/python3

import math
import os
from functools import lru_cache


@lru_cache(maxsize=None)
def prime_factors(n):
    count = 0
    if n % 2 == 0:
        count += 1
    while n % 2 == 0:
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            count += 1
            n = n / i
    if n > 2:
        count += 1
    return count


#
# Complete the towerBreakers function below.
#
def towerBreakers(arr):
    #
    # Write your code here.
    #
    d = 0
    for x in arr:
        d ^= prime_factors(x)
    return 2 - (d != 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = towerBreakers(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
