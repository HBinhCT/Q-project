#!/bin/python3

import os


#
# Complete the acessoryCollection function below.
#
def acessoryCollection(L, A, N, D):
    #
    # Write your code here.
    #
    if D > A or D > N or N > L:
        return 'SAD'
    if D == 1:
        return str(L * A)
    n_rest_max = (N - 1) // (D - 1)
    max_result = -1
    for n_rest in range(n_rest_max, 0, -1):
        n_highest = N + (n_rest - 1) - n_rest * (D - 1)
        rest, n_lowest = divmod(L - n_highest, n_rest)
        if rest > A - 1 or (rest == A - 1 and n_lowest > 0):
            break
        res = n_highest * A + n_rest * (2 * A - rest - 1) * rest // 2 + n_lowest * (A - rest - 1)
        if max_result >= res:
            break
        max_result = res
    if max_result == -1:
        return 'SAD'
    return str(max_result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        LAND = input().split()

        L = int(LAND[0])

        A = int(LAND[1])

        N = int(LAND[2])

        D = int(LAND[3])

        result = acessoryCollection(L, A, N, D)

        fptr.write(result + '\n')

    fptr.close()
