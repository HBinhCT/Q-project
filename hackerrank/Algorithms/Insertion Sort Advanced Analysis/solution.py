#!/bin/python3

import os


def merge(array, left, right):
    i = il = ir = inversion_count = 0
    left_len = len(left)
    right_len = len(right)
    while il < left_len and ir < right_len:
        if left[il] <= right[ir]:
            array[i] = left[il]
            il += 1
        else:
            array[i] = right[ir]
            ir += 1
            inversion_count += left_len - il
        i += 1
    while il < left_len:
        array[i] = left[il]
        il += 1
        i += 1
    while ir < right_len:
        array[i] = right[ir]
        ir += 1
        i += 1
    return inversion_count


# Complete the insertionSort function below.
def insertionSort(arr):
    mid = len(arr) // 2
    count = 0
    if mid > 0:
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        count += insertionSort(left_arr)
        count += insertionSort(right_arr)
        count += merge(arr, left_arr, right_arr)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
