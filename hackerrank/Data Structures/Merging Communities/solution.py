def find(i, p):
    arr = []
    while p[i] > 0:
        arr.append(i)
        i = p[i]
    for j in arr:
        p[j] = i
    return i


def union(u, v, p):
    if p[u] > p[v]:
        p[v] += p[u]
        p[u] = v
    else:
        p[u] += p[v]
        p[v] = u


n, q = map(int, input().strip().split())
parents = {i: -1 for i in range(1, n + 1)}
for _ in range(q):
    query = input().strip().split()
    if query[0] == 'Q':
        a = int(query[1])
        x = find(a, parents)
        print(abs(parents[x]))
    else:
        a, b = int(query[1]), int(query[-1])
        x, y = find(a, parents), find(b, parents)
        if x != y:
            union(x, y, parents)
