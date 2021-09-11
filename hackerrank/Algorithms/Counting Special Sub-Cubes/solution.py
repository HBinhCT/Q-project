#!/bin/python3

import os


#
# Complete the specialSubCubes function below.
#
def specialSubCubes(n, cube):
    #
    # Write your code here.
    #
    res = []
    n2 = n * n
    for k in range(1, n + 1):
        res.append(0)
        for x in range(n - k + 1):
            for y in range(n - k + 1):
                for z in range(n - k + 1):
                    i = x * n2 + y * n + z
                    if k == 1:
                        if cube[i] == 1:
                            res[-1] += 1
                    else:
                        cube[i] = max(cube[i], cube[i + 1], cube[i + n], cube[i + 1 + n], cube[i + n2],
                                      cube[i + 1 + n2], cube[i + n + n2], cube[i + 1 + n + n2])
                        if cube[i] == k:
                            res[-1] += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        cube = list(map(int, input().rstrip().split()))

        result = specialSubCubes(n, cube)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
