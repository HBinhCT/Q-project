"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque


def update(vertex):
    queue = deque()
    queue.append(vertex)
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if distance[y] > distance[x] + 1:
                distance[y] = distance[x] + 1
                queue.append(y)


n, m = map(int, input().strip().split())
distance = [1005] * (n + 1)
distance[1] = 0
graph = defaultdict(list)
for _ in range(m):
    q_type, *vertexes = map(int, input().strip().split())
    if q_type == 1:
        if distance[vertexes[0]] == 1005:
            print(-1)
        else:
            print(distance[vertexes[0]])
    elif q_type == 2:
        graph[vertexes[0]].append(vertexes[1])
        if distance[vertexes[1]] > distance[vertexes[0]] + 1:
            distance[vertexes[1]] = distance[vertexes[0]] + 1
            update(vertexes[1])
