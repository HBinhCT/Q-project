#!/bin/python3

import os


# Complete the chiefHopper function below.
def chiefHopper(arr):
    bot_energy = 0
    for height in reversed(arr):
        bot_energy = (bot_energy + height + 1) // 2
    return bot_energy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
