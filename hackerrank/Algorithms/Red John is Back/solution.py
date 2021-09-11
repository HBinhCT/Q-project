#!/bin/python3

import math
import os


# Complete the redJohn function below.
def redJohn(n):
    res = 0
    combos = 1
    for i in range(n // 4):
        combos += (math.factorial(n - 3 * (i + 1)) / (math.factorial(n - 4 * (i + 1)) * math.factorial(i + 1)))
    for j in range(2, int(combos + 1)):
        prime = True
        if (j % 2 == 0 and j > 2) or (j % 3 == 0 and j > 3):
            prime = False
        else:
            for k in range(5, 1 + round(j ** .5), 6):
                if j % k == 0 or j % (k + 2) == 0:
                    prime = False
                    break
        res += 1 if prime else 0
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()
