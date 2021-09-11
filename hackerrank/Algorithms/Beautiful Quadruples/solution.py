#!/bin/python3

import os


#
# Complete the beautifulQuadruples function below.
#
def beautifulQuadruples(a, b, c, d):
    #
    # Write your code here.
    #
    a, b, c, d = sorted([a, b, c, d])
    max_num = 2 ** len('{:b}'.format(d))
    cnt = [0] * max_num
    all_cnt = 0
    for i in range(1, c + 1):
        for j in range(i, d + 1):
            cnt[i ^ j] += 1
            all_cnt += 1
    ret = 0
    for i in range(1, b + 1):
        for j in range(1, min(a + 1, i + 1)):
            ret += all_cnt - cnt[i ^ j]
        for k in range(i, d + 1):
            cnt[i ^ k] -= 1
            all_cnt -= 1
    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    abcd = input().split()

    a = int(abcd[0])

    b = int(abcd[1])

    c = int(abcd[2])

    d = int(abcd[3])

    result = beautifulQuadruples(a, b, c, d)

    fptr.write(str(result) + '\n')

    fptr.close()
