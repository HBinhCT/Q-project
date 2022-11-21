mod = 1000000007
t = int(input())
cases = []
mx = 0
for _ in range(t):
    n, k = map(int, input().strip().split())
    cases.append((n, k))
    mx = max(mx, k)
comp = [1]
for i in range(1, mx + 1):
    comp.append(comp[-1] * i % mod)
for n, k in cases:
    print(comp[k] * pow(comp[k - n], mod - 2, mod) % mod)
