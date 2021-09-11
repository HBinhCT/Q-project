#!/bin/python3

import os


#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Write your code here
    primes, primality = [], [True] * 10001
    for i in range(2, 10001):
        if primality[i]:
            primes.append(i)
            primality[2 * i:10001:i] = [False] * (10000 // i - 1)
    a, b, answers, plates = [], [], [], number[:]
    for prime in primes[:q]:
        while plates:
            plate = plates.pop()
            if plate % prime:
                a.append(plate)
            else:
                b.append(plate)
        if b:
            answers += b[::-1]
        plates, a, b = a[:], [], []
    if plates:
        answers += plates[::-1]
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
