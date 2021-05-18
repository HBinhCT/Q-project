"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import heapq


def capture_castle(px, py, rows, cols, paths):
    times = [[float('inf')] * cols for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]
    times[0][0] = paths[0][0]
    heap = [(paths[0][0], 0, 0)]
    heapq.heapify(heap)
    while heap:
        time, u, v = heapq.heappop(heap)
        if not visited[u][v]:
            visited[u][v] = True
            for du, dv in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                next_u = u + du
                next_v = v + dv
                if 0 <= next_u < rows and 0 <= next_v < cols and not visited[next_u][next_v]:
                    next_time = time + paths[next_u][next_v]
                    if times[next_u][next_v] > next_time:
                        times[next_u][next_v] = next_time
                        heapq.heappush(heap, (next_time, next_u, next_v))
    return times[px][py]


t = int(input())
for _ in range(t):
    m, n = map(int, input().strip().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().strip().split())))
    x, y, t = map(int, input().strip().split())
    take_time = capture_castle(x - 1, y - 1, m, n, grid)
    if take_time >= t:
        print('NO')
    else:
        print('YES', (t - take_time), sep='\n')
