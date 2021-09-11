#!/bin/python3

import os


#
# Complete the chocolateGame function below.
#
def chocolateGame(arr):
    #
    # Write your code here.
    #
    from collections import defaultdict

    prefixes = (defaultdict(int), defaultdict(int))
    iter_arr = iter(arr)
    loses = 0
    prev = next(iter_arr)
    curr_xor = [prev, 0]
    it = 1
    prefixes[0][0] = 1
    prefixes[1][0] = 1
    prefixes[0][prev] = 1
    for i in iter_arr:
        curr_xor[it] ^= (i - prev)
        loses += prefixes[it][curr_xor[it]]
        prefixes[it][curr_xor[it]] += 1
        prefixes[it][curr_xor[it] ^ i] += 1
        it = not it
        prev = i
    n = len(arr)
    return n * (n - 1) // 2 - loses


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chocolateGame(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
