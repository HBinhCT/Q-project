#!/bin/python3

import os


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    from collections import Counter
    sss = Counter(''.join(sorted(s[i:j])) for i in range(0, len(s)) for j in range(i + 1, len(s) + 1))
    return sum(sss[key] * (sss[key] - 1) // 2 for key in sss)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
