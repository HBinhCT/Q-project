#!/bin/python3

import os


# Complete the pangrams function below.
def pangrams(s):
    return 'pangram' if len(set(s.lower().replace(' ', ''))) == 26 else 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
