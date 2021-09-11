#!/bin/python3

import os
import sys


#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

def shop(n, k, centers, roads):
    # Write your code here
    from heapq import heappush, heappop

    adj = [[] for _ in range(n + 2)] * (n + 2)  # adj array
    goal_fish = (1 << k) - 1
    safe_fish_num = goal_fish + 2
    values = [[0] * safe_fish_num for _ in range(safe_fish_num)]
    for i in range(safe_fish_num):
        for j in range(safe_fish_num):
            values[i][j] = i | j
    fish = [0 for _ in range(n + 2)]  # bitmask
    dist = [[99999999] * safe_fish_num for _ in range(n + 2)]  # ಠ_ಠ
    bit_shifts = [1 << i for i in range(11)]
    for i in range(n):
        for bit in centers[i].split()[1:]:
            fish[i + 1] = values[fish[i + 1]][bit_shifts[int(bit) - 1]]  # 1-indexed nodes
    for i in range(len(roads)):  # ❨╯°□°❩╯︵┻━┻
        adj[roads[i][0]].append((roads[i][1], roads[i][2]))
        adj[roads[i][1]].append((roads[i][0], roads[i][2]))
    heap = []
    heappush(heap, (0, 1, fish[1]))  # (distance, cur_node, fish_equip)
    while heap:
        cur_dist, cur_node, cur_fish = heappop(heap)
        for next_node, next_dist in adj[cur_node]:
            next_fish = fish[next_node]
            combine_fish = values[cur_fish][next_fish]
            total_dist = cur_dist + next_dist
            if total_dist < dist[next_node][combine_fish]:
                dist[next_node][combine_fish] = total_dist
                heappush(heap, (total_dist, next_node, combine_fish))
    ans = float('inf')
    for i in range(safe_fish_num):  # overlaps due to subtraction later but whatever
        for j in range(safe_fish_num):
            if values[i][j] == goal_fish:
                ans = min(ans, max(dist[n][i], dist[n][j]))
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, m, k = map(int, sys.stdin.readline().strip().split())

    centers = []

    for _ in range(n):
        centers.append(sys.stdin.readline().strip())

    roads = []

    for _ in range(m):
        roads.append(list(map(int, sys.stdin.readline().strip().split())))

    res = shop(n, k, centers, roads)

    fptr.write(str(res) + '\n')

    fptr.close()
