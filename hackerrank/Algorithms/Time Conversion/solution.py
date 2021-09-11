#!/bin/python3

import os


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    h = s[:2]
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if s[-2:] == 'AM' and s[:2] == '12':
        h = '00'
    # Checking if last two elements of time
    # is PM and first two elements aren't 12
    # add 12 to hours
    elif s[-2:] == 'PM' and s[:2] != '12':
        h = str(int(h) + 12)
    # remove AM / PM
    return h + s[2:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
