#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    # The existing leaderboard, scores, is in descending order.
    # Alice's scores, alice, are in ascending order.
    ranked = []
    for score in scores:
        if score not in ranked:
            ranked.append(score)
    res = []
    cursor = len(ranked) - 1
    for score in alice:
        if score > ranked[0]:
            res.append(1)
        else:
            while cursor >= 0:
                if score < ranked[cursor]:
                    res.append(cursor + 2)
                    break
                elif score == ranked[cursor]:
                    res.append(cursor + 1)
                    break
                cursor -= 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
