from collections import deque


def find(u, parents):
    while u != parents[u]:
        parents[u] = parents[parents[u]]
        u = parents[u]
    return u


def union(u, v, parents, ranks):
    pu = find(u, parents)
    pv = find(v, parents)
    if pu == pv:
        return
    if ranks[pu] < ranks[pv]:
        parents[pu] = pv
        ranks[pv] += ranks[pu]
    else:
        parents[pv] = pu
        ranks[pu] += ranks[pv]


n, m = map(int, input().strip().split())
roots = list(range(n + 1))
sizes = [0] + [1] * n
for _ in range(m):
    a, b = map(int, input().strip().split())
    union(a, b, roots, sizes)
queue = deque()
for _ in range(n):
    query = input().strip().split()
    if query[0] == 'E':
        x = int(query[1])
        if m > 0:
            for i in range(len(queue) - 1, -1, -1):
                if find(x, roots) == find(queue[i], roots):
                    queue.insert(i + 1, x)
                    break
            else:
                queue.append(x)
        else:
            queue.append(x)
    elif query[0] == 'D':
        print(queue.popleft())
