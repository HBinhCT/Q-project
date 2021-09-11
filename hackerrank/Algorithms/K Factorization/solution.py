#!/bin/python3

import os


# Complete the kFactorization function below.
def kFactorization(n, A):
    def fact_rec(num, numbers, res=None):
        if res is None:
            res = []
        if not len(numbers):
            return res
        elif num % numbers[0] == 0:
            if not len(res):
                res.append(num)
            pivot = num // numbers[0]
            res.append(pivot)
            return fact_rec(pivot, numbers, res)
        else:
            numbers.pop(0)
            return fact_rec(num, numbers, res)

    steps = fact_rec(n, sorted(A, reverse=True))
    if not len(steps) or steps[-1] != 1:
        return [-1]
    else:
        steps.reverse()
        return steps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = kFactorization(n, A)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
