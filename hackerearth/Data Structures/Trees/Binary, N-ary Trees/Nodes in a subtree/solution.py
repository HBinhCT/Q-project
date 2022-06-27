"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""
from collections import defaultdict
from sys import stdin


def generate(adj, string, res, node=1):
    res[node] = string[node - 1]
    if not adj[node]:
        return res[node]
    else:
        for neighbor in adj[node]:
            adj[neighbor].remove(node)
            res[node] = res[node] + generate(adj, string, res, neighbor)
        return res[node]


n, q = map(int, stdin.readline().strip().split())
s = stdin.readline().strip()
edges = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, stdin.readline().strip().split())
    # Process the Inputs of node details
    edges[u].append(v)
    edges[v].append(u)
tree = {}
generate(edges, s, tree)
for _ in range(q):
    u, c = stdin.readline().strip().split()
    # Process the queries
    u = int(u)
    print(tree[u].count(c))
