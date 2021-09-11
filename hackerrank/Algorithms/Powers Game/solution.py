#!/bin/python3

import os


#
# Complete the powersGame function below.
#
def powersGame(n):
    #
    # Write your code here.
    #
    return 'First' if n % 8 else 'Second'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = powersGame(n)

        fptr.write(result + '\n')

    fptr.close()
