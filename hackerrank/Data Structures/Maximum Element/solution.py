#!/bin/python3

import os


#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    ans = []
    items = [0]
    for operation in map(lambda x: list(map(int, x.strip().split())), operations):
        if operation[0] == 1:
            items.append(max(operation[-1], items[-1]))
        elif operation[0] == 2:
            items.pop()
        else:
            ans.append(items[-1])
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
