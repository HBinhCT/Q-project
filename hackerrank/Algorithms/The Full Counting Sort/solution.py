#!/bin/python3


# Complete the countSort function below.
def countSort(arr):
    from collections import defaultdict
    d = defaultdict(list)
    n = len(arr)
    for i in range(n // 2):
        d[int(arr[i][0])].append('-')
    for i in range(n // 2, n):
        d[int(arr[i][0])].append(arr[i][1])
    print(*[' '.join(d[k]) for k in sorted(d)])


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
