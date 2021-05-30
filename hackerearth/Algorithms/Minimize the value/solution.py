"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict


def dfs(src, par, vls, adjacency, s, lvl):
    global mini_sum
    s[src] = vls[src - 1]
    count = 0
    for neigh in adjacency[src]:
        if neigh != par:
            count += 1
            lvl[neigh] = lvl[src] + 1
            dfs(neigh, src, vls, adjacency, s, lvl)
            s[src] += s[neigh]
    if count != 2:
        mini_sum = min(mini_sum, lvl[src])


n, x = map(int, input().strip().split())
tree = defaultdict(set)
values = list(map(int, input().strip().split()))
for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    tree[u].add(v)
    tree[v].add(u)
sums = [0] * (n + 1)
levels = [0] * (n + 1)
mini_sum = n + 1
dfs(1, 1, values, tree, sums, levels)
print(sum(sums) + (mini_sum + 2) * x)
