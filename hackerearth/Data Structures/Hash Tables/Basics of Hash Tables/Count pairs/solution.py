from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k, p = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    counts = defaultdict(int)
    for i in a:
        counts[i % p] += 1
    ans = 0
    pairs = {}
    for i, v in counts.items():
        if 3 * i * i % p == k:
            ans += v * (v - 1) // 2
        j = (i * i * i - k * i) % p
        if j in pairs:
            ans += counts[i] * pairs[j]
            pairs[j] += counts[i]
        else:
            pairs[j] = counts[i]
    print(ans)
