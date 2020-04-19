#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the lilysHomework function below.
def lilysHomework(arr):
    def solution(a):
        m = {}
        for i in range(len(a)):
            m[a[i]] = i
        sorted_a = sorted(a)
        ret = 0
        for i in range(len(a)):
            if a[i] != sorted_a[i]:
                ret += 1
                index_to_swap = m[sorted_a[i]]
                m[a[i]] = index_to_swap
                a[i], a[index_to_swap] = sorted_a[i], a[i]
        return ret

    return min(solution(arr[::]), solution(arr[::-1]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
