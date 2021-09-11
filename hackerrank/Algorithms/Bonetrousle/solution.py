#!/bin/python3

import os


#
# Complete the bonetrousle function below.
#
def bonetrousle(n, k, b):
    #
    # Write your code here.
    #
    min_val = b * (b + 1) // 2
    max_val = b * (2 * k - b + 1) // 2
    if n < min_val or n > max_val:
        return [-1]
    q = (n - min_val) // b
    r = (n - max_val) % b
    answer = [i + q for i in range(1, b + 1)]
    for i in range(1, r + 1):
        answer[-i] += 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nkb = input().split()

        n = int(nkb[0])

        k = int(nkb[1])

        b = int(nkb[2])

        result = bonetrousle(n, k, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
