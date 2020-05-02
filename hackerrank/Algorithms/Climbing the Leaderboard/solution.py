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
    ranked = [scores[0]]
    for score in scores[1:]:
        if score != ranked[-1]:
            ranked.append(score)
    cursor = len(ranked) - 1
    for score in alice:
        if score > ranked[0]:
            yield 1
        else:
            while cursor >= 0:
                if score < ranked[cursor]:
                    yield cursor + 2
                    break
                elif score == ranked[cursor]:
                    yield cursor + 1
                    break
                cursor -= 1


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
