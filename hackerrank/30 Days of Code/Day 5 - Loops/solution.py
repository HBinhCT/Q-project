#!/bin/python3

import math
import os
import random
import re
import sys


def main(num):
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')


if __name__ == '__main__':
    n = int(input())
    main(n)
