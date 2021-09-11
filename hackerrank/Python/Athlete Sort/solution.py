#!/bin/python3


def main(array, k):
    for item in sorted(array, key=lambda row: row[k]):
        print(*item)


if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    main(arr, k)
