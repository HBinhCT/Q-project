from math import factorial


def find(x, parents):
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y, parents, ranks):
    px = find(x, parents)
    py = find(y, parents)
    if px != py:
        if ranks[px] < ranks[py]:
            parents[px] = py
            ranks[py] += ranks[px]
        else:
            parents[py] = px
            ranks[px] += ranks[py]


n, k = map(int, input().strip().split())
roots = list(range(n))
sizes = [1] * n
for _ in range(k):
    student1, student2 = map(int, input().strip().split())
    union(student1, student2, roots, sizes)
total = 1
for i in range(n):
    p = find(i, roots)
    if p == i:
        total *= factorial(sizes[p])
        total %= 1000000007
print(total)
