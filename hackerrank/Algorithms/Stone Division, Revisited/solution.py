#!/bin/python3

import os


# Complete the stoneDivision function below.
def stoneDivision(n, s):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def moves(size):
        next_moves = [0]
        for i in s:
            if size > i and size % i == 0:
                next_moves.append(1 + size // i * moves(i))
        return max(next_moves)

    return moves(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        s = list(map(int, input().rstrip().split()))

        result = stoneDivision(n, s)

        fptr.write(str(result) + '\n')

    fptr.close()
