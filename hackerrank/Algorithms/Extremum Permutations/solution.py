#!/bin/python3

import os


#
# Complete the extremumPermutations function below.
#
def extremumPermutations(n, a, b):
    #
    # Write your code here.
    #
    from itertools import islice, accumulate

    mod = 1000000007
    if any(x + 1 == y for c in map(sorted, (a, b)) for x, y in zip(c, c[1:])):
        return 0
    if set(a) & set(b):
        return 0
    going_up = [None] * n
    for c, low in ((a, True), (b, False)):
        for elt in c:
            elt -= 1
            if elt > 0:
                going_up[elt] = not low
            if elt < n - 1:
                going_up[elt + 1] = low
    count = [1]
    for i, inc in islice(enumerate(going_up), 1, n):
        if inc is None:
            count = [sum(count)] * (i + 1)
        elif inc:
            count = [0] + list(accumulate(count))
        else:
            count = list(reversed(list(accumulate(reversed(count))))) + [0]
        count = [elt % mod for elt in count]
    return sum(count) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkl = input().split()

    n = int(nkl[0])

    k = int(nkl[1])

    l = int(nkl[2])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = extremumPermutations(n, a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
