"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
import threading
from collections import defaultdict


def dfs(adj, node, seen, parent_list, low_list, disc_list, bridge_list, time=0):
    seen[node] = True
    low_list[node] = disc_list[node] = time
    for child in adj[node]:
        if not seen[child]:
            parent_list[child] = node
            dfs(adj, child, seen, parent_list, low_list, disc_list, bridge_list, time + 1)
            low_list[node] = min(low_list[node], low_list[child])
            if low_list[child] > disc_list[node]:
                bridge_list.add((node, child))
                bridge_list.add((child, node))
        elif child != parent_list[node]:
            low_list[node] = min(low_list[node], disc_list[child])


def solve():
    n, m = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(list)
    edges = {}
    for i in range(1, m + 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        edges[i] = (a, b)
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    disc = [float('inf')] * (n + 1)
    low = [float('inf')] * (n + 1)
    bridges = set()
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited, parent, low, disc, bridges)
    q = int(sys.stdin.readline())
    for _ in range(q):
        p = int(sys.stdin.readline())
        print('Unhappy' if edges[p] in bridges else 'Happy')


sys.setrecursionlimit(10 ** 6)
threading.stack_size(10 ** 8)
t = threading.Thread(target=solve)
t.start()
t.join()
