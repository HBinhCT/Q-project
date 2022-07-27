def solve(query, arr):
    # Your Code Here
    def find(a, parents):
        while a != parents[a]:
            parents[a] = parents[parents[a]]
            a = parents[a]
        return a

    def union(a, b, parents, ranks, minimums, maximums):
        pa = find(a, parents)
        pb = find(b, parents)
        if pa == pb:
            return minimums[pa], maximums[pa]
        elif ranks[pa] < ranks[pb]:
            parents[pa] = pb
            minimums[pb] = min(minimums[pa], minimums[pb])
            maximums[pb] = max(maximums[pa], maximums[pb])
            return minimums[pb], maximums[pb]
        else:
            ranks[pa] += ranks[pa] == ranks[pb]
            parents[pb] = pa
            minimums[pa] = min(minimums[pa], minimums[pb])
            maximums[pa] = max(maximums[pa], maximums[pb])
            return minimums[pa], maximums[pa]

    ln = len(arr)
    roots = list(range(ln))
    sizes = [0] * ln
    min_list = arr.copy()
    max_list = arr.copy()
    for x, y in query:
        yield union(x - 1, y - 1, roots, sizes, min_list, max_list)


n = int(input())
arr = list(map(int, input().split()))
Q = int(input())
col = 2
query = []
for _ in range(Q):
    query.append(map(int, input().split()))

out_ = solve(query, arr)
for i_out_ in out_:
    print(' '.join(map(str, i_out_)))
