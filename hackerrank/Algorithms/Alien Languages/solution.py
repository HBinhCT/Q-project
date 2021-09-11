#!/bin/python3

import os


#
# Complete the alienLanguages function below.
#
def alienLanguages(n, m):
    #
    # Write your code here.
    #
    mod = 100000007  # 10 ** 8 + 7
    v = [2 * i > n for i in range(n + 1)]
    for i in range(n - 1, -1, -1):
        v[i] += v[i + 1]
    c = []
    while v[1]:
        c.append(v[1])
        for i in range(1, n // 2 + 1):
            v[i] = v[2 * i]
        for i in range(n // 2 + 1, n + 1):
            v[i] = 0
        for i in range(n - 1, -1, -1):
            v[i] = (v[i] + v[i + 1]) % mod
    f = [1] + [0] * (len(c) - 1)
    for k in range(1, m + 1):
        f = [sum(f_item * c_item for f_item, c_item in zip(f, c)) % mod] + f[:-1]
    return f[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = alienLanguages(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
