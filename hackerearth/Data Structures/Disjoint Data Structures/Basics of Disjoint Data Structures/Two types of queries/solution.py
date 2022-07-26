from collections import defaultdict
from sys import stdin


def find(x, parents):
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y, parents, ranks):
    px = find(x, parents)
    py = find(y, parents)
    if px == py:
        return
    if ranks[px] < ranks[py]:
        parents[px] = py
    else:
        parents[py] = px
        if ranks[px] == ranks[py]:
            ranks[px] += 1


n = int(stdin.readline())
s = stdin.readline().strip()
q = int(stdin.readline())
roots = list(range(26))
sizes = list(range(26))
pairs = defaultdict(int)
base_idx = 97  # ord('a') = 97
cost = 0
for i in range(n // 2):
    j = n - 1 - i
    if s[i] != s[j]:
        a = ord(s[i]) - base_idx
        b = ord(s[j]) - base_idx
        if a > b:
            a, b = b, a
        pairs[(a, b)] += 1
        cost += 1
for _ in range(q):
    line = list(stdin.readline().strip().split())
    if line[0] == '1':
        a = ord(line[1]) - base_idx
        b = ord(line[2]) - base_idx
        union(a, b, roots, sizes)
        new_cost = 0
        new_pairs = defaultdict(int)
        for k, v in pairs.items():
            a, b = k
            if find(a, roots) != find(b, roots):
                new_pairs[(a, b)] += v
                new_cost += v
        pairs = new_pairs
        cost = new_cost
    elif line[0] == '2':
        print(cost)
