#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arithmeticExpressions function below.
def arithmeticExpressions(arr):
    import operator

    def _arithmetic_expressions(array):
        operations = (
            ('+', operator.add),
            ('-', lambda x, y: x - y + 101),
            ('*', operator.mul)
        )
        cache = {}
        first = array[0]
        cache[first] = str(first)
        for i, v in enumerate(array[1:], 1):
            next_cache = {}
            for val in cache:
                for name, operation in operations:
                    next_val = operation(val, v) % 101
                    next_exp = cache[val] + name + str(v)
                    if next_val == 0:
                        return next_exp, i
                    next_cache[next_val] = next_exp
            cache = next_cache

    exp, index = _arithmetic_expressions(arr)
    extra = ''
    remain = len(arr) - (index + 1)
    if remain:
        extra = '*' + '*'.join(map(str, arr[-remain:]))
    return exp + extra


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = arithmeticExpressions(arr)

    fptr.write(result + '\n')

    fptr.close()
