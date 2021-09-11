#!/bin/python3

import os


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    # every city has space station
    if n == len(c):
        return 0
    # get a list of indices corresponding to adjacent stations
    stations = sorted(c)
    # Distance from first city to first space station is (stations[0] - 0).
    # Distance from last city to last space station is ((n-1) - stations[-1])
    # - subtract 1 because our indexing system is half-open, [0, n).
    maximum = max(stations[0], n - 1 - stations[-1])
    # iterate over space stations only.
    for i in range(1, len(c)):
        # the distance between space stations
        d = stations[i] - stations[i - 1]
        # d//2 corresponds to the distance of the middle city to either station, with no remainder.
        # If d//2 > maximum, make it the new max.
        maximum = max(d // 2, maximum)
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
