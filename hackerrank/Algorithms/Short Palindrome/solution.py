#!/bin/python3

import os


# Complete the shortPalindrome function below.
def shortPalindrome(s):
    mod = 10 ** 9 + 7
    c1 = [0] * 26
    c2 = [0] * 26 * 26
    c3 = [0] * 26 * 26
    count = 0
    r26 = list(range(26))
    ord_a = ord('a')
    for c in s:
        k = ord(c) - ord_a
        p = 26 * k - 1
        q = k - 26
        for i in r26:
            q += 26
            p += 1
            count += c3[q]
            c3[p] += c2[p]
            c2[p] += c1[i]
        c1[k] += 1
    return count % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
