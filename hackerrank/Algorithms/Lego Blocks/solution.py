#!/bin/python3

import os


#
# Complete the legoBlocks function below.
#
def legoBlocks(n, m):
    #
    # Write your code here.
    #
    mod = 1000000007  # 10 ** 9 + 7
    height = n % mod
    width = m % mod
    # The number of combinations to build a single row
    row_combinations = [1, 1, 2, 4]
    # Build row combinations up to this wall's width
    while len(row_combinations) <= width:
        row_combinations.append(sum(row_combinations[-4:]) % mod)
    # Compute total combinations for constructing a wall of height N of varying widths
    total = [pow(c, height, mod) for c in row_combinations]
    # Find the number of unstable wall configurations for a wall of height N of varying widths
    unstable = [0, 0]
    for i in range(2, width + 1):
        unstable.append(sum((total[j] - unstable[j]) * total[i - j] for j in range(1, i)) % mod)
    # Return the number of stable wall combinations
    return (total[width] - unstable[width]) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
