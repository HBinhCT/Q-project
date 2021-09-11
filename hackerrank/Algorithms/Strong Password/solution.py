#!/bin/python3

import os
import re


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    cases = [r'[a-z]', r'[A-Z]', r'[\d]', r'[!@#$%^&*()\-+]']
    for case in cases:
        if not re.search(case, password):
            count += 1
    return max(count, 6 - n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
