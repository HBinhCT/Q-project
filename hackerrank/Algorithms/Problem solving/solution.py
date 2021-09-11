#!/bin/python3

import os


#
# Complete the problemSolving function below.
#
def problemSolving(k, v):
    #
    # Write your code here.
    #
    from collections import defaultdict

    size = len(v)
    f = [-1] * size
    b = [-1] * size
    d = defaultdict(list)
    for i in range(size):
        for j in range(i + 1, size):
            if abs(v[j] - v[i]) >= k:
                d[i].append(j)

    def solve(x, s):
        for i in d[x]:
            if f[i] != s:
                f[i] = s
                if b[i] == -1 or solve(b[i], s):
                    b[i] = x
                    return 1
        return 0

    count = 0
    for i in range(size):
        count += solve(i, i)
    return size - count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        v = list(map(int, input().rstrip().split()))

        result = problemSolving(k, v)

        fptr.write(str(result) + '\n')

    fptr.close()
