#!/bin/python3

import os


# Complete the towerBreakers function below.
def towerBreakers(n, m):
    return 2 if m == 1 or n % 2 == 0 else 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
