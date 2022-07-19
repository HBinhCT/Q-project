def find_ans(roads, new_roads, n):
    # Write your code here
    def find(x, parents):
        while x != parents[x]:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x

    roots = list(range(n + 1))
    res = n - 1
    for a, b in roads:
        pa = find(a, roots)
        pb = find(b, roots)
        if pa != pb:
            roots[pb] = pa
            res -= 1
    for a, b in new_roads:
        pa = find(a, roots)
        pb = find(b, roots)
        if pa != pb:
            roots[pb] = pa
            res -= 1
        yield res


n = int(input())
m = int(input())
s = int(input())
roads = []
for _ in range(m):
    roads.append(map(int, input().split()))
q = int(input())
s1 = int(input())
new_roads = []
for _ in range(q):
    new_roads.append(map(int, input().split()))

out_ = find_ans(roads, new_roads, n)
print(' '.join(map(str, out_)))
