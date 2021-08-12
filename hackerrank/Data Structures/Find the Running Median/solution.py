#!/bin/python3

import os


#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here
    from bisect import insort

    arr = []
    medians = []
    for i in range(len(a)):
        insort(arr, a[i])
        j = i + 1
        if j % 2:
            medians.append(arr[j // 2])
        else:
            medians.append((arr[j // 2] + arr[j // 2 - 1]) / 2)
    return medians


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
