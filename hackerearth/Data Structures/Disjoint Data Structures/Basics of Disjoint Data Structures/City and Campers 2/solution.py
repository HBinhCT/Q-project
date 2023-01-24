from collections import defaultdict


def find(x, p):
    while x != p[x]:
        p[x] = p[p[x]]
        x = p[x]
    return x


n, q = map(int, input().strip().split())
parents = list(range(n + 1))
ranks = [1] * (n + 1)
groups = defaultdict(int)
groups[1] = n
ans = 0
for _ in range(q):
    a, b = map(int, input().strip().split())
    pa = find(a, parents)
    pb = find(b, parents)
    if pa != pb:
        if ranks[pa] > ranks[pb]:
            pa, pb = pb, pa
        groups[ranks[pa]] -= 1
        groups[ranks[pb]] -= 1
        if not groups[ranks[pa]]:
            del groups[ranks[pa]]
        if not groups[ranks[pb]]:
            del groups[ranks[pb]]
        groups[ranks[pa] + ranks[pb]] += 1
        ranks[pb] += ranks[pa]
        parents[pa] = pb
        if len(groups) == 1:
            res = 0
        else:
            res = float('inf')
            j = -1
            for i in sorted(groups):
                if groups[i] > 1:
                    res = 0
                    break
                if j != -1:
                    res = min(res, abs(j - i))
                j = i
        ans = res
    print(ans)
