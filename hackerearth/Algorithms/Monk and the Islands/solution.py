"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque, defaultdict


def bfs(nodes, adjacency):
    level = [0] * nodes
    queue = deque([0])
    while queue:
        cur_island = queue.popleft()
        if cur_island == nodes - 1:
            break
        for next_island in adjacency[cur_island]:
            if next_island and not level[next_island]:
                queue.append(next_island)
                level[next_island] = level[cur_island] + 1
    return level[nodes - 1]


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    islands = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().strip().split())
        islands[x - 1].append(y - 1)
        islands[y - 1].append(x - 1)
    print(bfs(n, islands))
