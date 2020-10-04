#!/bin/python3

import os
import sys


#
# Complete the arraySplitting function below.
#
def arraySplitting(arr):
    #
    # Write your code here.
    #
    first = 0
    last = len(arr)
    middle = (first + last) // 2
    sum_arr = sum(arr) / 2
    if sum_arr == 0:
        return len(arr) - 1
    if sum_arr % 1 == 0 and last > 1:
        while True:
            total = sum(arr[:middle])
            if first == last + 1 or first < 0 or last > len(arr):
                return 0
            elif total == sum_arr:
                p = 1 + max(arraySplitting(arr[:middle]), arraySplitting(arr[middle:]))
                return p
            elif total > sum_arr:
                if total - arr[middle - 1] < sum_arr:
                    return 0
                else:
                    last = middle - 1
            elif total < sum_arr:
                if total + arr[middle] > sum_arr:
                    return 0
                else:
                    first = middle + 1
            else:
                last = middle - 1
            middle = (first + last) // 2
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = arraySplitting(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
