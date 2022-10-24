from collections import defaultdict


def dfs(adj, ans, node=0, parent=-1):
    res = 1
    for neighbor in adj[node]:
        if neighbor != parent:
            res *= dfs(adj, ans, neighbor, node) + 1
    ans[0] += res
    return res


n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    tree[u].append(v)
    tree[v].append(u)
total = [0]
dfs(tree, total)
print((total[0] + 1) % 1000000007)
