from collections import defaultdict, deque
from sys import stdin


def dfs(node, par, adj, pars):
    stack = deque([(node, par)])
    while stack:
        node, par = stack.pop()
        for neigh in adj[node]:
            if neigh != par:
                pars[node].append(neigh)
                stack.append((neigh, node))


def update(node, val, lim, pars, vals):
    stack = deque([node])
    while stack:
        node = stack.pop()
        if vals[node] < lim:
            vals[node] += val
            for child in pars[node]:
                stack.append(child)


t = int(stdin.readline())
for _ in range(t):
    n, q, y = map(int, stdin.readline().strip().split())
    tree = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, stdin.readline().strip().split())
        tree[u].append(v)
        tree[v].append(u)
    parents = defaultdict(list)
    dfs(1, 0, tree, parents)
    values = defaultdict(int)
    for _ in range(q):
        p, *data = map(int, stdin.readline().strip().split())
        if 0 == p:
            v, x = data
            update(v, x, y, parents, values)
        elif 1 == p:
            print(values[data[0]])
