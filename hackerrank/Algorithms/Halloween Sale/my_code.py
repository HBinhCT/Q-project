#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if s < p:
        return 0
    # calc the number of terms in the arithmetic progression taking into account linear inequality
    # i.e. last element >= `m`
    n = (p - m) // d + 1
    t = int(n / 2 * (2 * p - (n - 1) * d))  # S(n) = n/2 * (2*a + (n−1)*d)
    if s > t:
        # The case have enough money to reach `m` dollars
        n += (s - t) // m
    else:
        # The case runs out of money before reaching 'm' dollars
        # for n purchases with discount (before limit),
        # total cost = p + (p-d) + (p-d-d) + (p-d-d-d) ... = n * p - C(n,2) * d
        # how many games (x) can be purchased with $ budget (before limit)
        # total cost of x games <= $ budget
        # x*p - C(x,2)*d <= $
        # p*x - d/2*x*(x-1) <= $
        # p*x - d/2*(x^2-x) <= $
        # d/2*x^2 -(2*p+d)/2*x <= $
        # so the number of games is the solution of the quadratic equation
        # d*x^2 -(2*p+d)*x - 2*$ == 0
        b = 2 * p + d
        n = int((b - math.sqrt(b ** 2 - 4 * d * 2 * s)) / (2 * d))
        # x = (−b + sqrt(b**2 − 4ac)) / 2*a or x = (−b - sqrt(b**2 − 4ac)) / 2*a
    return n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
