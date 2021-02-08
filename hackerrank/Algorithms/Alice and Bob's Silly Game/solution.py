#!/bin/python3

import os
import sys

primes = [2]


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x < 2 or x % 2 == 0:
        return False
    if x < 9:
        return True
    if x % 3 == 0:
        return False
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    for f in range(5, int(x ** 0.5) + 1, 6):
        if x % f == 0:
            return False
        if x % (f + 2) == 0:
            return False
    return True


#
# Complete the sillyGame function below.
#
def sillyGame(n):
    #
    # Write your code here.
    #
    biggest_prime = primes[-1]
    if n > biggest_prime:
        for i in range(biggest_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
    return 'Alice' if sum(i <= n for i in primes) % 2 else 'Bob'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        result = sillyGame(n)

        fptr.write(result + '\n')

    fptr.close()
