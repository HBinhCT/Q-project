#!/bin/python3

import os


# Complete the anagram function below.
def anagram(s):
    l = len(s)
    if l % 2 != 0:
        return -1
    else:
        from collections import Counter
        return sum((Counter(s[:l // 2]) - Counter(s[l // 2:])).values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
