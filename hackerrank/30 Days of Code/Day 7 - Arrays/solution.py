#!/bin/python3


def main(array):
    print(*array[::-1])


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    main(arr)
