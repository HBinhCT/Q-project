"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict


def check(vertex, size, seen, count=1):
    if count == size:
        return True
    for next_vertex in range(size):
        if next_vertex in graph[vertex] and not seen[next_vertex]:
            seen[next_vertex] = True
            if check(next_vertex, size, seen, count + 1):
                return True
    return False


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    graph = defaultdict(list)
    for _ in range(m):
        x, y = map(lambda z: int(z) - 1, input().strip().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * n
    for i in range(n):
        visited[i] = True
        if check(i, n, visited):
            print('Yes')
            break
        visited[i] = False
    else:
        print('No')
