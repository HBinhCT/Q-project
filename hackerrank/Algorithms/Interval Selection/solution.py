#!/bin/python3

import os


#
# Complete the intervalSelection function below.
#
def intervalSelection(intervals):
    #
    # Write your code here.
    #
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    count = 0
    check = [0, 0]
    for a, b in sorted_intervals:
        if a > check[1]:
            count += 1
            check[1] = b
        elif a > check[0]:
            count += 1
            check[0], check[1] = check[1], b
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        intervals = []

        for _ in range(n):
            intervals.append(list(map(int, input().rstrip().split())))

        result = intervalSelection(intervals)

        fptr.write(str(result) + '\n')

    fptr.close()
