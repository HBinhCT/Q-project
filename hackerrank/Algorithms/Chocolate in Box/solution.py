#!/bin/python3

import os


#
# Complete the chocolateInBox function below.
#
def chocolateInBox(arr):
    #
    # Write your code here.
    #
    x = 0
    for i in arr:
        x ^= i
    return sum(i ^ x < i for i in arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chocolateInBox(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
