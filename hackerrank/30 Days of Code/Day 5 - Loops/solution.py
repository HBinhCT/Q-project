#!/bin/python3


def main(num):
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')


if __name__ == '__main__':
    n = int(input())
    main(n)
