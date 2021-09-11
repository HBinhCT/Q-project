#!/bin/python3

import os


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    return sum([s[i] == s[i + 1] for i in range(len(s) - 1)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
