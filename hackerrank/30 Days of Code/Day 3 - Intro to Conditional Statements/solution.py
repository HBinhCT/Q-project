#!/bin/python3


def main(n):
    return 'Weird' if n % 2 == 1 or 5 < n < 21 else 'Not Weird'


if __name__ == '__main__':
    N = int(input())
    print(main(N))
