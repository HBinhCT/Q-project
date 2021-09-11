#!/bin/python3

import os


# Complete the flippingMatrix function below.
def flippingMatrix(matrix):
    ln = len(matrix)
    ans = 0
    for i in range(ln // 2):
        for j in range(ln // 2):
            ans += max(matrix[i][j], matrix[i][ln - j - 1], matrix[ln - i - 1][j], matrix[ln - i - 1][ln - j - 1])
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
