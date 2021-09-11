#!/bin/python3

import os


#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    a.reverse()
    b.reverse()
    stack = []
    total = score = 0
    while a:
        item = a.pop()
        if total + item <= maxSum:
            total += item
            score += 1
            stack.append(item)
        else:
            break
    max_score = score
    while b:
        item = b.pop()
        total += item
        score += 1
        while total > maxSum and stack:
            total -= stack.pop()
            score -= 1
        if total <= maxSum and score > max_score:
            max_score = score
    return max_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
