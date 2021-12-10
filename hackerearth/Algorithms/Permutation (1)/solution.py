"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict


def mark_component(adj, u, path, seen=None):
    if seen is None:
        seen = {}
    seen[u] = True
    total = 1
    for v in adj[u]:
        path.append(v)
        if v not in seen:
            total += mark_component(adj, v, path, seen)
    return total


def remove_adjacent(nums):
    diff = []
    ln = len(nums)
    for i in range(ln - 1):
        if nums[i] != nums[i + 1]:
            diff.append(nums[i])
    if len(nums):
        diff.append(nums[ln - 1])
    return diff


k = int(input())
p = list(map(int, input().strip().split()))
graph = defaultdict(dict)
for i in range(k):
    line = input().strip()
    match = False
    for j in range(len(line)):
        if line[j] == 'Y':
            graph[i][j] = True
            graph[j][i] = True
            match = True
        if not match:
            graph[i][i] = True
marked = {}
permutation = p.copy()
for node in graph:
    res = []
    if node not in marked:
        mark_component(graph, node, res)
    if len(res):
        res = sorted(res)
        res = remove_adjacent(res)
        temp = sorted(permutation[i] for i in res)
        for i in range(len(res)):
            permutation[res[i]] = temp[i]
print(*permutation)
