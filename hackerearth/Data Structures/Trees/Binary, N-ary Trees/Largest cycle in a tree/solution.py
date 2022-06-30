from collections import deque, defaultdict


def find_node(edges, start=1):
    res = start
    queue = deque([(start, 0)])
    while queue:
        node, parent = queue.popleft()
        res = node
        for child in edges[node]:
            if child != parent:
                queue.append((child, node))
    return res


n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    tree[a].append(b)
    tree[b].append(a)
node1 = find_node(tree)
node2 = find_node(tree, node1)
print(node1, node2)
