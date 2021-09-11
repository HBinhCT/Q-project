#!/bin/python3

import os


#
# Complete the fightingPits function below.
#
def fightingPits(k, fighters, queries):
    #
    # Write your code here.
    #
    from itertools import accumulate

    team = [[0] for _ in range(k)]
    for s, t in fighters:
        team[t - 1].append(s)
    team = list(map(lambda x: list(accumulate(sorted(x))), team))
    res = []
    for q_line in queries:
        if q_line[0] == 1:
            p, x = q_line[1], q_line[2]
            team[x - 1].append(team[x - 1][-1] + p)
        else:  # q_line[0] == 2
            x, y = q_line[1], q_line[2]
            team_x = team[x - 1]
            team_y = team[y - 1]
            fighters_x = len(team_x)
            fighters_y = len(team_y)
            while True:
                if team_x[fighters_x - 1] >= team_y[fighters_y - 1]:
                    res.append(x)
                    break
                fighters_y -= team_x[fighters_x - 1] - team_x[fighters_x - 2]
                if fighters_y <= 1:
                    res.append(x)
                    break
                if team_y[fighters_y - 1] > team_x[fighters_x - 1]:
                    res.append(y)
                    break
                fighters_x -= team_y[fighters_y - 1] - team_y[fighters_y - 2]
                if fighters_x <= 1:
                    res.append(y)
                    break
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    fighters = []

    for _ in range(n):
        fighters.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = fightingPits(k, fighters, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
