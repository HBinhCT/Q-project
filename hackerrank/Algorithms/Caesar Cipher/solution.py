#!/bin/python3

import os


# Complete the caesarCipher function below.
def caesarCipher(s, k):
    import functools
    @functools.lru_cache(maxsize=26)
    def get_trans(k):
        from string import ascii_lowercase, ascii_uppercase
        return str.maketrans(
            ascii_lowercase + ascii_uppercase,
            ascii_lowercase[k:] + ascii_lowercase[:k] +
            ascii_uppercase[k:] + ascii_uppercase[:k]
        )

    return s.translate(get_trans(k % 26))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
