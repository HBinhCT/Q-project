"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n, m, q = map(int, input().strip().split())
costs = list(map(int, input().strip().split()))
type1 = []
type2 = defaultdict(list)
for _ in range(q):
    type_pie = list(map(int, input().strip().split()))
    if type_pie[0] == 1:
        x, k = map(lambda i: int(i) - 1, type_pie[1:])
        type1.append((x, k))
    elif type_pie[0] == 2:
        u, v = map(lambda i: int(i) - 1, type_pie[1:])
        type2[u].append(v)
        type2[v].append(u)


def figure_out(node, cost, adjacency, seen, pays):
    seen[node] = True
    stack = [node]
    nodes = [x]
    count = 1
    while stack:
        curr = stack.pop()
        for neighbor in adjacency[curr]:
            if not visited[neighbor]:
                seen[neighbor] = True
                stack.append(neighbor)
                nodes.append(neighbor)
                count += 1
    for i in nodes:
        pays[i] = cost / count


visited = [False] * n
amounts = [0] * n
total = 0
for x, k in type1:
    if not visited[x]:
        figure_out(x, costs[k], type2, visited, amounts)
        total += 1
print(total)
for amount in amounts:
    print(f'{amount:.10f}')
