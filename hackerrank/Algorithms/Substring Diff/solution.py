#!/bin/python3

import os
import sys


# Complete the substringDiff function below.
def substringDiff(k, s1, s2):
    size = len(s1)
    ans = k
    start = size - 1 - k
    end = size
    offset = -start  # first offset
    while offset < size - ans:
        curr = start  # Current valid match
        err = k  # Errors still allowed
        for i in range(start, end):
            if s1[i] != s2[i + offset]:
                err -= 1
                if err < 0:  # Current candidate ends
                    ans = max(ans, i - curr)
                    while s1[curr] == s2[curr + offset]:
                        curr += 1
                    curr += 1
                    err += 1
        ans = max(ans, end - curr)
        if offset < 0:
            start -= 1
        else:
            end -= 1
        offset += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        kS1S2 = input().split()

        k = int(kS1S2[0])

        s1 = kS1S2[1]

        s2 = kS1S2[2]

        result = substringDiff(k, s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()
