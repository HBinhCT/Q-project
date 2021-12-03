"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin

n, m = map(int, stdin.readline().strip().split())
metro = defaultdict(list)
for _ in range(m):
    k, t = map(int, stdin.readline().strip().split())
    u = list(map(int, stdin.readline().strip().split()))
    w = list(map(int, stdin.readline().strip().split()))
    time = t
    for i in range(k - 1):
        metro[u[i]].append((u[i + 1], time, w[i]))
        time += w[i]
start, end = map(int, stdin.readline().strip().split())
heap = [(0, start)]
paths = [float('inf')] * (n + 1)
while heap:
    total, station = heappop(heap)
    for next_station, time, seconds in metro[station]:
        if time >= total:
            new_total = total + seconds
            if paths[next_station] >= new_total:
                heappush(heap, (new_total, next_station))
                paths[next_station] = new_total
if paths[end] == float('inf'):
    print(-1)
else:
    print(paths[end])
