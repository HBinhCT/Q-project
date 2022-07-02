from collections import defaultdict, deque


def get_path(node_x, num_of_child):
    path = deque([node_x])
    while node_x != 1:
        node_x //= num_of_child
        path.append(node_x)
    return path


def get_lca(node_u, node_v, num_of_child):  # LCA is the lowest common ancestor
    path_u = get_path(node_u, num_of_child)
    path_v = get_path(node_v, num_of_child)
    while path_u and path_v and path_u[-1] == path_v[-1]:
        path_u.pop()
        path_v.pop()
    return path_u, path_v


k, q = map(int, input().strip().split())
weights = defaultdict(lambda: 1)
for _ in range(q):
    p, *query = map(int, input().strip().split())
    if p == 1:
        u, v = query
        du, dv = get_lca(u, v, k)
        shortest_distance = 0
        for x in du:
            shortest_distance += weights[x]
        for x in dv:
            shortest_distance += weights[x]
        print(shortest_distance)
    else:
        u, v, w = query
        du, dv = get_lca(u, v, k)
        for x in du:
            weights[x] += w
        for x in dv:
            weights[x] += w
