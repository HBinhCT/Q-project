#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the angryProfessor function below.
def angryProfessor(k, a):
    """
    Given the arrival time of each student and a threshold number of attendees, determine if the class is canceled.
    :param k: the threshold number of students
    :param a: an array of integers representing arrival times
    :return: string 'YES' if class is cancelled, or 'NO' otherwise
    """
    return 'YES' if len([x for x in a if x <= 0]) < k else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
