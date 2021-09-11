#!/bin/python3

import os


# Complete the alternate function below.
def alternate(s):
    m = 0
    st = set(s)
    length = len(st)
    if length > 1:
        from itertools import combinations
        for combos in combinations(st, length - 2):
            temp = s
            for c in combos:
                temp = temp.replace(c, '')
            if len([i for i in range(len(temp) - 1) if temp[i] == temp[i + 1]]) == 0:
                if len(temp) > m:
                    m = len(temp)
    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
