#!/bin/python3


# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    amin = -10 ** 4
    arr = [2 * amin] + arr
    for j in range(2, n + 1):
        i, a = j, arr[j]
        while a < arr[i - 1]:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = a
        print(*arr[1:])


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
