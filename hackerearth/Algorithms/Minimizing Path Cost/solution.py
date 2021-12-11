"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from sys import stdin


def floyd_warshall(graph, size):
    for k in range(0, size):
        for i in range(0, size):
            for j in range(0, size):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


n, m = map(int, stdin.readline().strip().split())
stations = stdin.readline().strip().split()
indexes = {}
for i, v in enumerate(stations):
    indexes[v] = i
adj = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
for _ in range(m):
    station1, station2, d = stdin.readline().strip().split()
    adj[indexes[station1]][indexes[station2]] = adj[indexes[station2]][indexes[station1]] = int(d)
floyd_warshall(adj, n)
q = int(stdin.readline())
for _ in range(q):
    source, destination = stdin.readline().strip().split()
    print(adj[indexes[source]][indexes[destination]])
