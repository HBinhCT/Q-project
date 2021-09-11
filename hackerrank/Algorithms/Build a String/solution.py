#!/bin/python3

import os


#
# Complete the buildString function below.
#
def buildString(a, b, s):
    #
    # Write your code here.
    #
    size = len(s)
    costs = [float('inf')] * (size + 1)
    costs[0] = 0
    k = 0
    i = 1
    while i <= size:  # i is the number of char finished, s[i-1] finished
        # find the maximum substring
        j = max(i, k)
        while j <= size and (s[i - 1:j] in s[:i - 1]):
            j += 1
        if j - 1 != i:
            costs[j - 1] = min(costs[i - 1] + b, costs[j - 1])
            k = j
        costs[i] = min(costs[i - 1] + a, costs[i])
        i += 1
    return costs[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nab = input().split()

        n = int(nab[0])

        a = int(nab[1])

        b = int(nab[2])

        s = input()

        result = buildString(a, b, s)

        fptr.write(str(result) + '\n')

    fptr.close()
