#!/bin/python3

import os


# Complete the breakingRecords function below.
def breakingRecords(scores):
    best = worst = scores[0]
    best_count = worst_count = 0
    for score in scores[1:]:
        if score > best:
            best = score
            best_count += 1
        if score < worst:
            worst = score
            worst_count += 1
    return [best_count, worst_count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
