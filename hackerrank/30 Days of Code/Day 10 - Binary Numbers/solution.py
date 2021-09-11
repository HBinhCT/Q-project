#!/bin/python3


def main(num):
    print(max(map(len, bin(num)[2:].split('0'))))


if __name__ == '__main__':
    n = int(input())

    main(n)
