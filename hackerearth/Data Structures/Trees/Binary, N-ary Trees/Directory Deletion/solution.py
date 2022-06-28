from collections import defaultdict


def count_deleted(edges, deleted_ids, node=1):
    if deleted_ids[node]:
        return 1
    res = 0
    for neighbor in edges[node]:
        res += count_deleted(edges, deleted_ids, neighbor)
    return res


n = int(input())
parent_ids = list(map(int, input().strip().split()))
m = int(input())
directory_ids = list(map(int, input().strip().split()))
tree = defaultdict(list)
for i, v in enumerate(parent_ids, start=1):
    tree[v].append(i)
deletion = defaultdict(bool)
for i in directory_ids:
    deletion[i] = True
print(count_deleted(tree, deletion))
