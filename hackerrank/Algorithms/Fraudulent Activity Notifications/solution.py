#!/bin/python3

import os


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0
    e_max = 200
    c = [0] * e_max
    for e in expenditure[:d]:
        c[e] += 1

    def median(arr, r):
        s = x = 0
        for j in range(len(arr)):
            s += arr[j]
            if 2 * s >= r:
                x = j
                break
        if r % 2 == 1 or 2 * s > r:
            return x
        y = 0
        for j in range(x + 1, len(arr)):
            if arr[j]:
                y = j
                break
        return (x + y) / 2

    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2 * median(c, d):
            notifications += 1
        c[expenditure[i - d]] -= 1
        c[expenditure[i]] += 1
    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
