from collections import defaultdict

n, c = map(int, input().strip().split())
parents = list(map(int, input().strip().split()))
colors = list(map(int, input().strip().split()))
tree = defaultdict(list)
for i, v in enumerate(parents, start=2):
    tree[v].append(i)


def find_color(edges, color_vertices, res, node=1, labels=None):
    if labels is None:
        labels = defaultdict(lambda: -1)
    idx = node - 1
    res[idx] = labels[color_vertices[idx]]
    labels[color_vertices[idx]] = node
    for child in edges[node]:
        find_color(edges, color_vertices, res, child, labels)
    labels[color_vertices[idx]] = res[idx]


ancestors = [-1] * n
find_color(tree, colors, ancestors)
print(*ancestors)
