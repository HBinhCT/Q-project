def find(x, parents):
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y, parents, ranks):
    if ranks[x] > ranks[y]:
        parents[y] = x
    else:
        parents[x] = y
        ranks[x] = max(ranks[x], ranks[y] + 1)


n, q = map(int, input().strip().split())
leaders = list(range(n))
levels = [1] * n
groups = [1] * n
counts = [0] * (n + 1)
counts[1] = n
largest = smallest = 1
for _ in range(q):
    a, b = map(lambda x: int(x) - 1, input().strip().split())
    pa = find(a, leaders)
    pb = find(b, leaders)
    if pa != pb:
        union(pa, pb, leaders, levels)
        counts[groups[pa]] -= 1
        counts[groups[pb]] -= 1
        new_size = groups[pa] + groups[pb]
        groups[pa] = groups[pb] = new_size
        counts[new_size] += 1
        largest = max(largest, new_size)
        while not counts[smallest]:
            smallest += 1
    print(largest - smallest)
