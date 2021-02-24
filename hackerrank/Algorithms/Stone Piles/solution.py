#!/bin/python3

import os
import sys


#
# Complete the stonePiles function below.
#
def stonePiles(arr):
    #
    # Write your code here.
    #
    from collections import Counter

    total = 0
    counter = Counter(arr)
    end_numbers = [0, 1]
    while len(end_numbers) <= 50:
        end_numbers += [end_numbers[-1] + 1] * len(end_numbers)
    losing_numbers = (1, 2, 4, 8)
    for size, count in counter.items():
        if size not in losing_numbers and count & 1 != 0:
            total ^= (size - min(4, end_numbers[size]))
    return 'ALICE' if total else 'BOB'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = stonePiles(arr)

        fptr.write(result + '\n')

    fptr.close()
