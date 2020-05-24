#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for item in sorted(arr, key=lambda row: row[k]):
        print(*item)
