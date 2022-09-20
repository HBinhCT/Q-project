from bisect import bisect

n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = sorted(set(a))
m = len(b)
tree = [0] * (m + 1)
f = []
while a:
    i = bisect(b, a.pop())
    j = i
    total = 0
    while j:
        total += tree[j]
        j -= j & -j
    while i <= m:
        tree[i] += 1
        i += i & -i
    f.append(n - len(a) - 1 - total)
f.sort()
ans = 0
j = n
for i in range(n):
    while j > 0 and f[i] + f[j - 1] >= k:
        j -= 1
    ans += n - max(j, i + 1)
print(ans)
