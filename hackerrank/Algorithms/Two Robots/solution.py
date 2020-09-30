#!/bin/python3

import os
import sys


#
# Complete the twoRobots function below.
#
def twoRobots(m, queries):
    #
    # Write your code here.
    #
    dp = [0]
    s = abs(queries[0][1] - queries[0][0])
    for i in range(1, len(queries)):
        dp.append(min(dp[j] + (0 if j == 0 else abs(queries[j - 1][1] - queries[i][0])) for j in range(i)))
        for j in range(i):
            dp[j] += abs(queries[i - 1][1] - queries[i][0])
        s += abs(queries[i][1] - queries[i][0])
    return s + min(dp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):
        mn = input().split()

        m = int(mn[0])

        n = int(mn[1])

        queries = []

        for _ in range(n):
            queries.append(list(map(int, input().rstrip().split())))

        result = twoRobots(m, queries)

        fptr.write(str(result) + '\n')

    fptr.close()
