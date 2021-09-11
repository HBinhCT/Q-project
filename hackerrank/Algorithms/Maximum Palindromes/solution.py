#!/bin/python3

import os


#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def initialize(s):
    # This function is called once before all queries.
    global lc, mod
    n = len(s)
    ascii_a = ord('a')
    arr = [[0] * lc for _ in range(n + 1)]
    for i, v in enumerate(s, 1):
        for j in range(lc):  # 2D array of character counts
            arr[i][j] = arr[i - 1][j] + (j == ord(v) - ascii_a)
    fac = [1] * n  # modular factorial
    i_fac = [1] * n  # modular inverse of factorial
    for i in range(1, n):
        fac[i] = fac[i - 1] * i % mod
        i_fac[i] = pow(fac[i], mod - 2, mod)
    return arr, fac, i_fac


#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    global array, factorial, inverse_factorial, lc, mod
    odd, even, divs = 0, 0, 1
    for i in range(lc):
        value = array[r][i] - array[l - 1][i]
        odd += value % 2  # count of center characters
        even += value // 2  # count of side characters
        divs *= inverse_factorial[value // 2]  # "denominators"
    return (odd or 1) * factorial[even] * divs % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    lc, mod = 26, 1000000007

    array, factorial, inverse_factorial = initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
