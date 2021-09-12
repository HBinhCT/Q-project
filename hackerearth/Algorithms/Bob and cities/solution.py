"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect
from heapq import heapify, heappop, heappush
from sys import stdin

n, m = map(int, stdin.readline().strip().split())
houses = []
for _ in range(n):
    houses.append(stdin.readline().strip())
l_cost, r_cost, u_cost, d_cost = map(int, stdin.readline().strip().split())
stx, sty = map(lambda i: int(i) - 1, stdin.readline().strip().split())
moves = ((l_cost, (0, -1)), (r_cost, (0, 1)), (u_cost, (-1, 0)), (d_cost, (1, 0)))
visited = [[False] * m for _ in range(n)]
heap = [(0, (stx, sty))]
heapify(heap)
costs = []
while heap:
    cost, (x, y) = heappop(heap)
    if not visited[x][y]:
        visited[x][y] = True
        costs.append(cost)
        for m_cost, (dx, dy) in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and houses[nx][ny] != '#' and not visited[nx][ny]:
                heappush(heap, (cost + m_cost, (nx, ny)))
q = int(stdin.readline())
for _ in range(q):
    x = int(stdin.readline())
    print(bisect(costs, x))
