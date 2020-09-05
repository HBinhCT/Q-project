#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumPeople function below.
def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    import operator

    # make list of cloud tuples with start and end
    clouds = []
    for location_cloud, range_cloud in zip(y, r):
        clouds.append((max(location_cloud - range_cloud, 0), location_cloud + range_cloud))
    # sort by start
    clouds.sort(key=lambda v: v[0])
    # make list of town tuples with position and people
    towns = []
    for location_town, population_town in zip(x, p):
        towns.append((location_town, population_town))
    # sort by start
    towns.sort(key=lambda v: v[0])
    # add a ghost cloud (to do all in one while loop)
    last_town_location = towns[-1][0]
    last_cloud = clouds[-1][1]
    ghost_location = max(last_town_location, last_cloud) + 100
    # insert ghost cloud
    clouds.append((ghost_location, ghost_location))
    # end of the current cloud interval
    current_end = -10 * 9
    # counter to check solely covered people by current cloud
    covered = 0
    # counter for people not covered by a cloud at all
    uncovered = 0
    # to remember maximum count
    max_covered = 0
    # index for the
    t_idx = 0

    # helper function to count people before a certain position
    def count(pos, exc=False):
        res = 0
        nonlocal t_idx
        # uses less than or less or equal operator
        op = operator.lt if exc else operator.le
        while t_idx < len(towns) and op(towns[t_idx][0], pos):
            # op: a<b or a<=b
            res += towns[t_idx][1]
            t_idx += 1
        return res

    # the actual algorithm
    # there are three cases considered:
    for start, end in clouds:
        # next cloud start after the end of old cloud
        if start > current_end:
            covered += count(current_end)
            max_covered = max(max_covered, covered)
            covered = 0
            uncovered += count(start, exc=True)
            current_end = end
        # next cloud starts and ends before the next cloud
        elif start <= current_end and end < current_end:
            covered += count(start, exc=True)
            count(end)
        # or it start before but ends later
        elif start <= current_end <= end:
            covered += count(start, exc=True)
            max_covered = max(max_covered, covered)
            covered = 0
            count(current_end)
            current_end = end
    return max_covered + uncovered


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
