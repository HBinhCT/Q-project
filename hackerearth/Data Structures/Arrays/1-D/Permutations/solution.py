n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
pre = [0] * n
suf = [0] * n
for i in range(1, n):
    pre[i] = max(pre[i - 1], a[i - 1])
for i in range(n - 2, -1, -1):
    suf[i] = max(suf[i + 1], a[i + 1])
for _ in range(q):
    l, r = (int(i) - 1 for i in input().strip().split())
    print(max(pre[l], suf[r]))
