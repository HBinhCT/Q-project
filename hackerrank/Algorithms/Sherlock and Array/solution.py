#!/bin/python3

import os


# Complete the balancedSums function below.
def balancedSums(arr):
    left_sum = 0
    right_sum = sum(arr)
    for i in arr:
        right_sum -= i
        if left_sum == right_sum:
            return 'YES'
        left_sum += i
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
