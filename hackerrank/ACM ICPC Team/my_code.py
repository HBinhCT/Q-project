#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the acmTeam function below.
def acmTeam(topic):
    from collections import Counter
    from itertools import combinations
    bin_topic = [int(s, 2) for s in topic]
    return max(Counter(bin(a | b).count('1') for a, b in combinations(bin_topic, 2)).items())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
