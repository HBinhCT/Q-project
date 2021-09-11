#!/bin/python3


def main(n, k):
    print(k - 1 if ((k - 1) | k) <= n else k - 2)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        main(n, k)
