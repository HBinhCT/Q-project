from sys import stdin


def find(a, parents):
    while parents[a] > 0:
        a = parents[a]
    return a


def join(a, b, parents, ranks):
    pa = find(a, parents)
    pb = find(b, parents)
    if pa == pb:
        return
    if ranks[pa] > ranks[pb]:
        parents[pb] = pa
        ranks[pa] += ranks[pb]
    else:
        parents[pa] = pb
        ranks[pb] += ranks[pa]


n, k = map(int, stdin.readline().strip().split())
arr = list(stdin.readline().strip())
roots = [0] * n
counts = [0] * n
longest = 0
for i in range(n):
    if arr[i] == '1':
        roots[i] = -1
        counts[i] = 1
        if i and arr[i - 1] == '1':
            join(i, i - 1, roots, counts)
    j = find(i, roots)
    longest = max(longest, counts[j])
for _ in range(k):
    query = stdin.readline().strip().split()
    if query[0] == '1':
        print(longest)
    else:
        _, x = query
        x = int(x) - 1
        if arr[x] != '1':
            arr[x] = '1'
            roots[x] = -1
            counts[x] = 1
            if x and arr[x - 1] == '1':
                join(x, x - 1, roots, counts)
            if x + 1 < n and arr[x + 1] == '1':
                join(x, x + 1, roots, counts)
            j = find(x, roots)
            longest = max(longest, counts[j])
