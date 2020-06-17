#!/bin/python3

import math
import os
import random
import re
import sys


def main(array):
    res = []
    for i in range(0, 4):
        for j in range(0, 4):
            s = sum(array[i][j:j + 3]) + array[i + 1][j + 1] + sum(array[i + 2][j:j + 3])
            res.append(s)
    print(max(res))


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    main(arr)
