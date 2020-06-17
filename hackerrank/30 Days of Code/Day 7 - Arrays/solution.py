#!/bin/python3

import math
import os
import random
import re
import sys


def main(array):
    print(*array[::-1])


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    main(arr)
