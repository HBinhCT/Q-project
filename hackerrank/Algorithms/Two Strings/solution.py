#!/bin/python3

import os


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    return 'NO' if set(s1).isdisjoint(set(s2)) else 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
