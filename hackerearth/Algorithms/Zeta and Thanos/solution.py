"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import heapq


def move(x, y, n, m, grid, visited):
    # LEFT
    if y != 0 and grid[x][y - 1] != '*' and not visited[x][y - 1]:
        yield x, y - 1
    # RIGHT
    if y != m - 1 and grid[x][y + 1] != '*' and not visited[x][y + 1]:
        yield x, y + 1
    # UP
    if x != 0 and grid[x - 1][y] != '*' and not visited[x - 1][y]:
        yield x - 1, y
    # DOWN
    if x != n - 1 and grid[x + 1][y] != '*' and not visited[x + 1][y]:
        yield x + 1, y


n, m = map(int, input().strip().split())
grid = []
for _ in range(n):
    grid.append(list(map(lambda x: x if x == '*' else int(x), input().strip().split())))
x, y = map(lambda x: int(x) - 1, input().strip().split())
q = int(input())
positions = []
for _ in range(q):
    positions.append(tuple(map(lambda x: int(x) - 1, input().strip().split())))
visited = [[False] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]
block_sum = [[0] * m for _ in range(n)]
heap = []
visited[x][y] = True
distance[x][y] = 0
block_sum[x][y] = grid[x][y]
heapq.heappush(heap, (distance[x][y], -block_sum[x][y], x, y))
while heap:
    cur_dist, cur_sum, cur_x, cur_y = heapq.heappop(heap)
    cur_sum *= -1
    for next_x, next_y in move(cur_x, cur_y, n, m, grid, visited):
        visited[next_x][next_y] = True
        distance[next_x][next_y] = cur_dist + 1
        block_sum[next_x][next_y] = cur_sum + grid[next_x][next_y]
        heapq.heappush(heap, (distance[next_x][next_y], -block_sum[next_x][next_y], next_x, next_y))
for tx, ty in positions:
    if visited[tx][ty]:
        print(distance[tx][ty], block_sum[tx][ty])
    else:
        print('-1 -1')
