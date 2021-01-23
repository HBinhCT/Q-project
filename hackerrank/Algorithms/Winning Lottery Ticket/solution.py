#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the winningLotteryTicket function below.
def winningLotteryTicket(tickets):
    digits = '0123456789'
    frequency = [0] * 1024
    for ticket in tickets:
        binary = ''
        for num in digits:
            if num in ticket:
                binary += '1'
            else:
                binary += '0'
        binary = int(binary, 2)
        frequency[binary] += 1
    res = 0
    for i, freq in enumerate(frequency[:1023]):
        if freq:
            for j in range(i + 1, 1024):
                if i | j == 1023:
                    res += freq * frequency[j]
    res += frequency[-1] * (frequency[-1] - 1) // 2
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()
