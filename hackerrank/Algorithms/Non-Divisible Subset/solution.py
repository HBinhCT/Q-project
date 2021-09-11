#!/bin/python3

import os


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    counter = [0] * k
    for number in s:
        counter[number % k] += 1
    # max one element with residual 0
    count = min(counter[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(counter[i], counter[k - i])
        else:
            count += min(counter[i], 1)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
