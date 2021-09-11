#!/bin/python3

import os


# Complete the primeXor function below.
def primeXor(a):
    from collections import defaultdict

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    max_bits = 8192
    mod = 1000000007
    values = defaultdict(int)
    for i in a:
        values[i] += 1
    res = [[0] * max_bits for _ in range(len(values) + 1)]
    res[0][0] = 1  # empty set
    i = 1
    for x, nx in values.items():
        nx_even = nx // 2 + 1  # includes empty set
        nx_odd = (nx + 1) // 2
        for j in range(max_bits):
            # Can create bit pattern j from either
            # - The multisets with bit pattern j formed from arr[:i-1] + an even number of items with value x
            # _ Appending an odd number of items with value x to the multisets with bit pattern k such that k^x
            # has pattern j
            res[i][j] = (res[i - 1][j] * nx_even + res[i - 1][j ^ x] * nx_odd) % mod
        i += 1
    return sum(res[-1][x] for x in range(2, max_bits) if is_prime(x)) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = primeXor(a)

        fptr.write(str(result) + '\n')

    fptr.close()
