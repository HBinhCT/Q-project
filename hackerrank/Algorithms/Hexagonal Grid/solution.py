#!/bin/python3

import os


#
# Complete the hexagonalGrid function below.
#
def hexagonalGrid(a, b):
    #
    # Write your code here.
    #
    dp = []
    ln = len(a)
    for i in range(ln):
        dp.append(int(a[i]))
        dp.append(int(b[i]))
    if sum(dp) % 2 != 0:
        return 'NO'
    for i in range(2 * ln):
        if dp[i] != 1:
            dp[i] = 1
            if i < 2 * ln - 1 and dp[i + 1] == 0:
                dp[i + 1] = 1
            elif i < 2 * ln - 2 and dp[i + 2] == 0:
                dp[i + 2] = 1
            else:
                return 'NO'
    return 'YES' if sum(dp) == 2 * ln else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = input()

        b = input()

        result = hexagonalGrid(a, b)

        fptr.write(result + '\n')

    fptr.close()
