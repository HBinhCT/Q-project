#!/bin/python3

import os


#
# Complete the xorMatrix function below.
#
def xorMatrix(m, first_row):
    #
    # Write your code here.
    #
    n = len(first_row)
    m -= 1  # now 0 row is first row, 1 row is the first row to compute
    mb = str(bin(m))[2:]
    lmb = len(mb)
    result = first_row.copy()
    for i in range(lmb):
        if mb[i] == '1':
            tmp = result.copy()
            offset = 2 ** (lmb - 1 - i)
            for j in range(n):
                result[j] = tmp[j] ^ tmp[(j + offset) % n]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    first_row = list(map(int, input().rstrip().split()))

    last_row = xorMatrix(m, first_row)

    fptr.write(' '.join(map(str, last_row)))
    fptr.write('\n')

    fptr.close()
