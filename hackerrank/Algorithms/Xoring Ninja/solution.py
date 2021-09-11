#!/bin/python3

import os


#
# Complete the xoringNinja function below.
#
def xoringNinja(arr):
    #
    # Write your code here.
    #
    import functools
    import operator
    return (functools.reduce(operator.or_, arr) << (len(arr) - 1)) % 1000000007


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = xoringNinja(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
