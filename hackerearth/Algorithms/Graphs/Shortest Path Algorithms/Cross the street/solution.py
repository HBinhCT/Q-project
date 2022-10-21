"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from heapq import heappush, heappop


def solve():
    n, m = map(int, input().strip().split())
    a = [list(map(int, input().strip().split())) for _ in range(n)]
    mx = 1000000000
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_costs = {}  # (u, v, h) -> cost
    heap = []  # (cost, u, v, h)
    for h in range(1, 101):
        c = abs(h - a[0][0])
        heappush(heap, (c, 0, 0, h))
        min_costs[(0, 0, h)] = c
    ans = mx
    while heap:
        c, u, v, h = heappop(heap)
        if c <= ans:
            for x, y in moves:
                next_u = u + x
                next_v = v + y
                if 0 <= next_u < n and 0 <= next_v < m:
                    next_h = a[next_u][next_v]
                    next_c = c + abs(h - next_h)
                    min_cost = min_costs.get((next_u, next_v, h), mx)
                    if next_c < min_cost and next_c < ans:
                        min_costs[(next_u, next_v, h)] = next_c
                        heappush(heap, (next_c, next_u, next_v, h))
                        if next_u == n - 1 and next_v == m - 1 and next_c < ans:
                            ans = next_c
    print(ans)


solve()
